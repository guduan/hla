#!/usr/bin/env python

"""
This script initialized some PVs in channel finder. The PVs are only those
used by HLA.

:author: Lingyun Yang
:date: 2011-05-11 16:22
"""

import os, sys
import re, time

from channelfinder.core.ChannelFinderClient import ChannelFinderClient
from channelfinder.core.Channel import Channel, Property, Tag

import hla

def dump_hla_cfa(out):
    hla._cfa.exportTextRecord(out)

def clean_small_cases_ones():
    pass

def initialize_cfs(out):
    all_keys, all_tags = [], []
    cfsurl = 'http://channelfinder.nsls2.bnl.gov:8080/ChannelFinder'
    cf = ChannelFinderClient(BaseURL = cfsurl, username='boss', password='1234')

    # clean up
    props = cf.getAllProperties()
    #cf.set(properties = [Property('ORDINAL', '85')])
    cfchannels = []
    for line in open(out, 'r').readlines():
        if line.strip()[0] == '#': continue
        # three parts, "pv; properties; tags"
        rec = line.split(';')
        pv, pstr, tagstr = rec
        chs = cf.find(name=pv.strip())
        if not chs:
            print "Did not find", pv
            continue
        if len(chs) > 1:
            print "PV is not unique:", pv
            continue
        
        prop, tags = {}, []
        for r in pstr.split(','):
            if not r: continue
            # all in upper cases
            k,v = r.upper().split('=')
            k = k.strip()
            v = v.strip()
            prop[k] = v
            if not k in all_keys: all_keys.append(k)

        for r in tagstr.split()[1:]:
            if r == 'default.eput': r = 'HLA.EPUT'
            elif r == 'default.eget': r = 'HLA.EGET'
            elif not r.startswith('HLA.'): r = 'HLA.' + r

            if not r in all_tags: all_tags.append(r)
            
            tags.append(r)
        #print pv, prop, tags
        cfprop = [Property(k, 'vioc', v) for k,v in prop.items()]
        cftags = [Tag(t, 'vioc') for t in tags]
        cfchannels.append(Channel(u'%s' % pv, 'vioc', properties=cfprop, tags=cftags))
        #cf.update(channel = Channel(pv, 'vioc'), properties=cfprop,
        #          tags = cftags)
        
    print ""
    print all_keys
    print all_tags
    cfprop = [Property(p, 'vioc', 'N.A.') for p in all_keys]
    cf.set(properties = cfprop)
    cftags = [Tag(t, 'vioc') for t in all_tags]
    cf.set(tags = cftags)    
    cf.set(channels=cfchannels)

def update_cfs(out):
    # same as initi_cfs for now
    #
    all_keys, all_tags = [], []
    cfsurl = 'http://channelfinder.nsls2.bnl.gov:8080/ChannelFinder'
    cf = ChannelFinderClient(BaseURL = cfsurl, username='boss', password='1234')

    # clean up
    props = cf.getAllProperties()
    #cf.set(properties = [Property('ORDINAL', '85')])
    cfchannels = []
    for line in open(out, 'r').readlines():
        if line.strip()[0] == '#': continue
        # three parts, "pv; properties; tags"
        rec = line.split(';')
        pv, pstr, tagstr = rec
        chs = cf.find(name=pv.strip())
        if not chs:
            print "Did not find", pv
            #cf.set(channel=Channel(pv, 'vioc'))
            #continue
        elif len(chs) > 1:
            print "PV is not unique:", pv
            continue
        
        prop, tags = {}, []
        for r in pstr.split(','):
            if not r: continue
            # all in upper cases
            k,v = r.upper().split('=')
            k = k.strip()
            v = v.strip()
            prop[k] = v
            if not k in all_keys: all_keys.append(k)

        for r in tagstr.split()[1:]:
            if r == 'default.eput': r = 'HLA.EPUT'
            elif r == 'default.eget': r = 'HLA.EGET'
            elif not r.startswith('HLA.'): r = 'HLA.' + r

            if not r in all_tags: all_tags.append(r)
            
            tags.append(r)
        #print pv, prop, tags
        cfprop = [Property(k, 'vioc', v) for k,v in prop.items()]
        cftags = [Tag(t, 'vioc') for t in tags]
        cfchannels.append(Channel(u'%s' % pv, 'vioc', properties=cfprop, tags=cftags))
        #cf.update(channel = Channel(pv, 'vioc'), properties=cfprop,
        #          tags = cftags)
        
    print ""
    print "keys:", all_keys
    print "tags:", all_tags
    print "channels:", len(cfchannels)
    if all_keys:
        cfprop = [Property(p, 'vioc', 'N.A.') for p in all_keys]
        cf.set(properties = cfprop)
    if all_tags:
        cftags = [Tag(t, 'vioc') for t in all_tags]
        cf.set(tags = cftags)    
    cf.set(channels=cfchannels)
    
def test():
    cfsurl = 'http://channelfinder.nsls2.bnl.gov:8080/ChannelFinder'
    cf = ChannelFinderClient(BaseURL = cfsurl, username='boss', password='1234')
    ch = cf.find(name='SR*')
    for c in ch:
        print c.name,
        
if __name__ == "__main__":
    #out = 'cfa.txt'
    #dump_hla_cfa(out)
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        #initialize_cfs(sys.argv[1])
        update_cfs(sys.argv[1])
    #test()
    
