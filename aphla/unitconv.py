"""
Unit Conversion
----------------
"""

# :author: Lingyun Yang <lyyang@bnl.gov>

import numpy as np
from collections import Iterable
import logging
import re

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

class UcAbstract(object):
    """an identity conversion with unit names.

    - *direction*, i.e. (src, dst) from src unit, to dst unit.
    - *invertible*, in case of linear, has both f(x) and f^{-1}(y).

    This src, dst are unit name, e.g. Tesla, T-m. They are helpful for
    display, but not essential for unit conversion.  They are not unit system
    names. Unit system is a concept in higher level managed by element (and
    action)

    See CaElement and CaAction for unit system.
    """
    def __init__(self, src, dst):
        self.direction = (src, dst)
        self.srcunit = None
        self.dstunit = None

    def __str__(self):
        src, dst = self.direction[0], self.direction[1]
        return "%s -> %s: identity" % (src, dst)

    def eval(self, x, inv = False):
        return x

class UcPoly(UcAbstract):
    """a polynomial unit conversion"""
    def __init__(self, src, dst, coef):
        super(UcPoly, self).__init__(src, dst)
        self.p = np.poly1d(coef)

    def __str__(self):
        src, dst = self.direction[0], self.direction[1]
        return "%s -> %s: %s" % (src, dst, str(self.p))

    def _inv_eval(self, x):
        """evaluate the inverse"""
        if not self.invertible:
            raise RuntimeError("inverse is not permitted for (%s -> %s)" % 
                               self.direction)
        if self.p.order == 1:
            # y = ax + b
            # x = 1/a * y - b/a
            a, b = self.p.coeffs
            ar, br = 1.0/a, -b*1.0/a
            if isinstance(x, Iterable):
                # keep None to None 
                return [ar*v + br if v is not None else None for v in x]
            else:
                return ar*x + br
        elif self.p.order == 0:
            raise RuntimeError("can not inverse a constant for (%s -> %s)" %
                               self.direction)
        else:
            raise RuntimeError("can not inverse polynomial order > 2 "
                               "for (%s -> %s)" % self.direction)

            
    def eval(self, x, inv = False):
        if x is None: return None

        if inv: return self._inv_eval(x)
        
        if isinstance(x, Iterable):
            return [self.p(v) if v is not None else None for v in x]
        else:
            return self.p(x)

class UcInterp1(UcAbstract):
    """linear interpolation"""
    def __init__(self, src, dst, x, y):
        super(UcInterp1, self).__init__(src, dst)
        #self.f = np.interpolate.interp1d(x, y)
        self.xp, self.fp = x, y

    def _inv_eval(self, x):
        if x is None: return None
        elif x < min(self.fp[0], self.fp[-1]): return None
        elif x > max(self.fp[0], self.fp[-1]): return None
        else:
            # interp returns boundary if x is outside of fp
            return np.interp(x, self.fp, self.xp)

    def eval(self, x, inv = False):
        if x is None: return None
        elif x < self.xp[0] or x > self.xp[-1]: return None
        else:
            # interp returns boundary if x is outside of xp
            return np.interp(x, self.xp, self.fp)

class UcInterpN(UcAbstract):
    """n-D linear interpolation"""
    def __init__(self, src, dst, x, y):
        """
        :param x: a list of x-data for interpolation
        :param y: a list of y-data for interpolation

        x[i] and y[i] are a list of measurement.
        """
        super(UcInterpN, self).__init__(src, dst)
        self.xp, self.fp = x, y

    def eval(self, x, inv = False):
        """if None, returns None"""
        if inv: raise RuntimeError("inverse not supported for (%s -> %s)" %
                                   self.direction)

        if not isinstance(x, Iterable):
            raise RuntimeError("expecting an iterable input")
        ret = []
        for i,v in enumerate(x):
            if x is None or x < self.xp[i][0] or x > self.xp[i][-1]:
                ret.append(None)
            else:
                ret.append(np.interp(x[i], self.xp[i], self.fp[i]))
        return ret


def loadUnitConversionH5(lat, h5file, group):
    """set the unit conversion for lattice with input from hdf5 file"""
    import h5py
    g = h5py.File(h5file, 'r')[group]
    _logger.info("setting unit conversion for lattice {0} "
                 "from data file {1}:{2}".format(
        lat.name, h5file, g.items()))
    for k,v in g.items():
        if not v.attrs.get('_class_', None): continue 

        # use separated three attrs first, otherwise, use 'unitsys' attr.
        fld = v.attrs.get('field', None)
        usrcsys = v.attrs.get('src_unit_sys', None)
        udstsys = v.attrs.get('dst_unit_sys', None)
        if fld is None:
            fld, usrcsys, udstsys = v.attrs.get('unitsys', ",,").split(',')
        if not fld: continue

        # instead of '', None is the unit for lower level(epics) data
        if usrcsys == '': usrcsys = None
        if udstsys == '': udstsys = None
        # the unit name, e.g., A, T/m, ...
        # check src_unit/dst_unit first, then direction as a backup
        usrc = v.attrs.get('src_unit', None)
        udst = v.attrs.get('dst_unit', None)
        if usrc is None and udst is None:
            usrc, udst = v.attrs.get('direction', (None, None))

        if v.attrs['_class_'] == 'polynomial':
            uc = UcPoly(usrc, udst, list(v))
        elif v.attrs['_class_'] == 'interpolation':
            uc = UcInterp1(usrc, udst, v[:,0], v[:,1])
        else:
            raise RuntimeError("unknow unit converter")

        # integer - invertible
        uc.invertible = v.attrs.get('invertible')
        # find the element list
        elems = v.attrs.get('elements', [])

        eobjs = []
        #lat._find_exact_element(ename) for ename in elems if lat.hasElement(ename)]
        for ename in elems:
            eobj = lat._find_exact_element(ename)
            if not eobj: 
                _logger.warn("dataset '{0}': element {1} not found. ignored".format(
                    k, ename))
                continue
            eobjs.append(eobj)

        fams = v.attrs.get('groups', [])
        for fam in fams:
            egrps = lat.getElementList(fam)
            if not egrps:
                _logger.warn("dataset '{0}': group {1} not found. ignored".format(
                    k, fam))
            eobjs += egrps

        _logger.info("unitconversion data for elems={0}, fams={1}".format(elems, fams))
        _logger.info("unitconversion will be updated for {0}".format([e.name for e in eobjs]))
        for eobj in eobjs:
            if fld not in eobj.fields():
                realfld = v.attrs.get('rawfield', None)
                if realfld is None:
                    _logger.warn("'%s' has no field '%s' for unit conversion" % (
                        ename, fld))
                    continue
                else:
                    eobj.addAliasField(fld, realfld)

            _logger.info("adding unit conversion for {0}.{1}, from {2} to {3}".format(
                ename, fld, usrcsys, udstsys))
            eobj.addUnitConversion(fld, uc, usrcsys, udstsys)

def loadUnitConversion(lat, fname):
    """load the unit conversion for lattice from INI file"""
    _logger.info("loading unit conversion for lattice {0} from "
                 "file {1}".format(lat.name, fname))
    import ConfigParser
    cfg = ConfigParser.ConfigParser(allow_no_value=False)
    cfg.readfp(open(fname), 'r')
    for sec in cfg.sections():
        if not cfg.has_option(sec, 'field'):
            raise RuntimeError("section [%s] has no 'field'" % sec)
        d = dict(cfg.items(sec))
        # use separated three attrs first, otherwise, use 'unitsys' attr.
        fld = d.get('field', None)
        usrcsys = d.get('src_unit_sys', None)
        udstsys = d.get('dst_unit_sys', None)
        if fld is None:
            fld, usrcsys, udstsys = re.findall(r'\w+', d.get('unitsys', ",,"))
        if not fld: continue

        # instead of '', None is the unit for lower level(epics) data
        if usrcsys == '': usrcsys = None
        if udstsys == '': udstsys = None
        # the unit name, e.g., A, T/m, ...
        # check src_unit/dst_unit first, then direction as a backup
        usrc = d.get('src_unit', None)
        udst = d.get('dst_unit', None)
        if usrc is None and udst is None:
            usrc, udst = d.get('direction', (None, None))

        _logger.debug("{0}[{1}] -> {2}[{3}]".format(usrcsys, usrc, udstsys, udst))

        if 'polynomial' in d:
            p = [float(v) for v in re.findall(r'[^ ,;]+', d['polynomial'])]
            _logger.debug("field '{0}' polynomial {1}".format(fld, p))
            uc = UcPoly(usrc, udst, p)
        elif 'interpolation' in d:
            ix, iy = re.findall(r'\w+', d.get('interpolation_cols', "0 1"))
            v = np.loadtxt(d['interpolation'])
            uc = UcInterp1(usrc, udst, v[:,int(ix)], v[:,int(iy)])
        else:
            raise RuntimeError("unknow unit converter")
        
        # the unit symbol
        uc.srcunit = usrc
        uc.dstunit = udst

        # find the element list
        elems = re.findall(r'\w+', d.get('elements', ""))

        eobjs = []
        for ename in elems:
            eobj = lat._find_exact_element(ename)
            if not eobj: 
                _logger.warn("element {0} not found. ignored".format(ename))
                continue
            eobjs.append(eobj)

        fams = re.findall(r'\w+', d.get('groups', ""))
        for fam in fams:
            egrps = lat.getElementList(fam)
            if not egrps:
                _logger.warn("group '{0}' not found. ignored".format(fam))
            eobjs += egrps

        _logger.info("unitconversion data for field= '{0}' elems={1}, "
                     "fams={2}".format(fld, elems, fams))
        _logger.info("unitconversion will be updated for {0}".format(
            [e.name for e in eobjs]))
        for eobj in eobjs:
            if fld not in eobj.fields():
                # fld is the converted value.
                realfld = d.get('rawfield', None)
                if realfld is None:
                    _logger.warn("'%s' has no field '%s' for unit conversion" % 
                                 (eobj.name, fld))
                    continue
                else:
                    # the fld is not available, but it will be an alias to
                    # rawfield, i.e. it only holds the result of unit
                    # conversion from real field.
                    eobj.addAliasField(fld, realfld)

            _logger.info("adding unit conversion for {0}.{1}, "
                         "from {2} to {3}".format(
                             eobj.name, fld, usrcsys, udstsys))
            eobj.addUnitConversion(fld, uc, usrcsys, udstsys)


def addIdentityUnitConversion(elem, fld, usrcsys, udstsys):
    """set unit conversion for two unitsys which are equivalent

    This is usually the case for BPM where raw data are in physics unit.
    """
    uc = UcAbstract(usrcsys, udstsys)
    uc.dstunit = elem.getUnit(fld, usrcsys)
    uc.srcunit = uc.dstunit
    elem.addUnitConversion(fld, uc, usrcsys, udstsys)
    
