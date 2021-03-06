#!/usr/bin/env python
"""
:author: Lingyun Yang lyyang@bnl.gov

This is the main file for GUI app `mleap`. A high level viewer and editor.
"""

from pkg_resources import require
require('cothread>=2.2')

import cothread
app = cothread.iqt()

import re
import aphla
from aphla.catools import camonitor, FORMAT_TIME, FORMAT_CTRL

import mleapresources
from elempickdlg import ElementPickDlg
#from orbitconfdlg import OrbitPlotConfig
from aporbitplot import ApMdiSubPlot, ApSvdPlot, ApCaTunesPlot
from aporbitdata import ApVirtualElemData, ManagedPvData
from aporbitphy import *
from elemeditor import ElementEditor
from pvmanager import CaDataMonitor
from latviewer import LatSnapshotMain

import logging
import os, sys
import platform
from functools import partial
import datetime,time
import numpy as np

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QSize, SIGNAL, QThread, Qt, QObject
from PyQt4.QtGui import (QMainWindow, QAction, QActionGroup, QMenu, QTableView,
    QVBoxLayout, QPen, QSizePolicy, QMessageBox, QSplitter, QPushButton,
    QHBoxLayout, QGridLayout, QWidget, QTabWidget, QLabel, QIcon, QActionGroup,
    QPlainTextEdit, QMdiArea, QMdiSubWindow, QDockWidget, QTextCursor,
                         QWhatsThis, QDialog)
import PyQt4.Qwt5 as Qwt

SUBWIN_ALL     = -1
SUBWIN_CURRENT = 0

class QTextEditLoggingHandler(logging.Handler):
    def __init__(self, textedit):
        logging.Handler.__init__(self)
        self.textedit = textedit
        _lgfmt = logging.Formatter("%(asctime)s - %(name)s [%(levelname)s]: "
                                   "%(message)s")
        self.setFormatter(_lgfmt)

    def emit(self, record):
        self.textedit.appendPlainText(self.format(record))
        #self.textedit.moveCursor(QTextCursor.End)


class OrbitPlotMainWindow(QMainWindow):
    """
    the main window has three major widgets: current, orbit tabs and element
    editor.
    """
    def __init__(self, parent = None, machines=[], **kwargs):
        QMainWindow.__init__(self, parent)
        self.iqtApp = kwargs.get("iqt", None)

        self.setIconSize(QSize(32, 32))
        self.error_bar = True
        self._dlgOrbitCor = None
        # logging
        self.logdock = QDockWidget("Log")
        self.logdock.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        textedit = QPlainTextEdit(self.logdock)
        
        self.logger = logging.getLogger(__name__)

        self.guilogger = logging.getLogger("aphla.gui")
        # the "aphla" include lib part logging. When the lib is inside
        # QThread, logging message will be sent to TextEdit which is cross
        # thread.
        # self.guilogger = logging.getLogger("aphla")
        handler = QTextEditLoggingHandler(textedit)
        self.guilogger.addHandler(handler)
        self.guilogger.setLevel(logging.INFO)
        self.logdock.setWidget(textedit)
        self.logdock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.logdock.setFeatures(QDockWidget.DockWidgetMovable|
                                 QDockWidget.DockWidgetClosable)
        self.logdock.setFloating(False)
        self.logdock.setMinimumHeight(20)
        self.logdock.setMaximumHeight(100)
        self.logdock.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.logdock.resize(200, 60)
        #print self.logdock.sizeHint()
        self.addDockWidget(Qt.BottomDockWidgetArea, self.logdock)
        #print self.logdock.sizeHint()
        #print self.logdock.minimumSize()
        #print self.logdock.maximumSize()
        #self.logger.info("INFO")
        #self.logdock.setMinimumHeight(40)
        #self.logdock.setMaximumHeight(160)

        for msg in kwargs.get("infos", []):
            self.logger.info(msg)
        # dict of (machine, (lattice dict, default_lat, pvm))
        self._mach = dict([(v[0], (v[1],v[2],v[3])) for v in machines])
        for m,(lats,lat0,pvm) in self._mach.items():
            self.logger.info("machine '%s' initialized: [%s]" % (
                m, ", ".join([lat.name for k,lat in lats.items()])))
            if pvm:
                for pv in pvm.dead():
                    self.logger.warn("'{0}' is disconnected.".format(pv))
        ## DCCT current plot
        #self.dcct = DcctCurrentPlot()
        #self.dcct.setMinimumHeight(100)
        #self.dcct.setMaximumHeight(150)

        #t0 = time.time()
        #t = np.linspace(t0 - 8*3600*24, t0, 100)
        #self.dcct.curve.t = t
        #v = 500*np.exp((t[0] - t[:50])/(4*3600*24))
        #self.dcct.curve.v = v.tolist()+v.tolist()
        #self.dcct.updatePlot()

        ## MDI area
        self.mdiarea = QMdiArea()
        self.connect(self.mdiarea, SIGNAL("subWindowActivated(QMdiSubWindow)"),
                     self.updateMachineLatticeNames)
        self.mdiarea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.physics = ApOrbitPhysics(self.mdiarea, iqt=self.iqtApp)
        self.live_orbit = True

        self.setCentralWidget(self.mdiarea)

        #self._elemed = ElementPropertyTabs()
        #self.elemeditor = ElementEditorDock(parent=self)
        #self.elemeditor.setAllowedAreas(Qt.RightDockWidgetArea)
        #self.elemeditor.setFeatures(QDockWidget.DockWidgetMovable|
        #                            QDockWidget.DockWidgetClosable)
        #self.elemeditor.setFloating(False)
        #self.elemeditor.setEnabled(False)
        #self.elemeditor.setMinimumWidth(400)
        #self.elemeditor.setWidget(self._elemed)
        #self.elemeditor.show()
        #self.elemeditor.hide()
        #self.connect(self.elemeditor, 
        #             SIGNAL("elementChecked(PyQt_PyObject, bool)"),
        #             self.physics.elementChecked)
        #self.addDockWidget(Qt.RightDockWidgetArea, self.elemeditor)

        self.createMenuToolBar()
        
        # the first machine is the default
        self.machBox.addItems([v for v in self._mach.keys()])
        self.reloadLatticeNames(self.machBox.currentText())
        self.connect(self.machBox, SIGNAL("currentIndexChanged(QString)"),
                     self.reloadLatticeNames)
        
        # update at 1/2Hz
        self.dt, self.itimer = 1500, 0
        #self.timerId = None
        self.timerId = self.startTimer(self.dt)

        self.vbpm = None
        self.statusBar().showMessage("Welcome")

        #self.initMachine("nsls2v2")
        #self._newVelemPlot("V2SR", aphla.machines.HLA_VBPM, 'x', 
        #                   "H Orbit", c = None)
        #print "Thread started", self.machinit.isRunning()

        #self.newElementPlots("BPM", "x, y")
        #self.newElementPlot("BPM", "y")
        #self.newElementPlot("HCOR", "x")
        #self.newElementPlot("VCOR", "y")
        #self.newElementPlot("QUAD", "b1")
        #self.newElementPlot("SEXT", "b2")
        

    def updateMachineLatticeNames(self, wsub):
        i = self.machBox.findText(wsub.machlat[0])
        self.machBox.setCurrentIndex(i)
        self.reloadLatticeNames(wsub.machlat[0])

    def reloadLatticeNames(self, mach):
        self.latBox.clear()
        cur_mach = str(self.machBox.currentText())
        lats, lat0, pvm = self._mach.get(cur_mach, ({}, None, None))
        self.latBox.addItems([lat for lat in lats.keys()])
        if lat0:
            i = self.latBox.findText(lat0.name)
            self.latBox.setCurrentIndex(i)

    def closeEvent(self, event):
        self.physics.close()
        self.mdiarea.closeAllSubWindows()
        event.accept()

    def createMenuToolBar(self):
        #
        # file menu
        #
        #self.machMenu = self.menuBar().addMenu("&Machines")
        #self.connect(self.machMenu, SIGNAL("aboutToShow()"),
        #             self.updateMachMenu)
        self.openMenu = self.menuBar().addMenu("&Open")
        self.openMenu.addAction("New Plot ...", self.openNewPlot)
        self.openMenu.addAction("New Tune Plot", self.openTunePlot)
        self.openMenu.addAction("New BPM Plot", partial(
                self.newElementPlots, "BPM", "x,y"))
        self.openMenu.addAction("New HCOR Plot", partial(
                self.newElementPlots, "HCOR", "x"))
        self.openMenu.addAction("New VCOR Plot", partial(
                self.newElementPlots, "VCOR", "y"))

        self.openMenu.addSeparator()
        self.openMenu.addAction("Open ORM", self.loadOrm)

        self.openMenu.addSeparator()        
        self.openMenu.addAction("Save Lattice ...", self.saveSnapshot)

        fileQuitAction = QAction(QIcon(":/file_quit.png"), "&Quit", self)
        fileQuitAction.setShortcut("Ctrl+Q")
        fileQuitAction.setToolTip("Quit the application")
        fileQuitAction.setStatusTip("Quit the application")
        #fileQuitAction.setIcon(Qt.QIcon(":/filequit.png"))
        self.connect(fileQuitAction, SIGNAL("triggered()"),
                     self.close)
        self.openMenu.addAction(fileQuitAction)

        # view
        self.viewMenu = self.menuBar().addMenu("&View")

        mkmenu = QMenu("&Mark", self.viewMenu)
        for fam in ["BPM", "COR", "QUAD", "SEXT", "INSERTION"]:
            famAct = QAction(fam, self)
            famAct.setCheckable(True)
            self.connect(famAct, SIGNAL("toggled(bool)"), self.click_markfam)
            mkmenu.addAction(famAct)
        # 
        
        # errorbar
        #viewErrorBarAction = QAction(QIcon(":/view_errorbar.png"),
        #                            "Errorbar", self)
        #viewErrorBarAction.setCheckable(True)
        #viewErrorBarAction.setChecked(True)
        #self.connect(viewErrorBarAction, SIGNAL("toggled(bool)"),
        #             self.errorBar)
        #
        #zoomM = QMenu("Zoom", self.viewMenu)

        #
        #
        #drift_from_now = QAction("Drift from Now", self)
        #drift_from_now.setCheckable(True)
        #drift_from_now.setShortcut("Ctrl+N")
        #drift_from_golden = QAction("Drift from Golden", self)
        #drift_from_golden.setCheckable(True)
        #drift_from_none = QAction("None", self)
        #drift_from_none.setCheckable(True)

        #self.viewMenu.addAction(viewLiveAction)
        #self.viewMenu.addAction(viewSingleShotAction)
        #self.viewMenu.addSeparator()

        #self.viewMenu.addAction(drift_from_now)
        #self.viewMenu.addAction(drift_from_golden)
        #self.viewMenu.addAction(drift_from_none)
        #self.viewMenu.addAction(viewAutoScale)
        #self.viewMenu.addAction(viewErrorBarAction)
        #self.viewMenu.addSeparator()

        self.viewMenu.addMenu(mkmenu)

        #drift_group = QActionGroup(self)
        #drift_group.addAction(drift_from_none)
        #drift_group.addAction(drift_from_now)
        #drift_group.addAction(drift_from_golden)
        #drift_from_none.setChecked(True)

        sep = self.viewMenu.addSeparator()
        #sep.setText("Drift")
        #self.connect(drift_from_now, SIGNAL("triggered()"), self.setDriftNow)
        #self.connect(drift_from_none, SIGNAL("triggered()"), self.setDriftNone)
        #self.connect(drift_from_golden, SIGNAL("triggered()"), 
        #             self.setDriftGolden)

        #viewStyle = QMenu("Line Style", self.viewMenu)
        #for act in ["Increase Point Size", "Decrease Point Size", None,
        #            "NoCurve", "Lines", "Sticks", None,
        #            "Solid Line", "Dashed Line", "Dotted Line", None,
        #            "Increase Line Width", "Decrease Line Width", None,
        #            "NoSymbol", "Ellipse", "Rect", "Diamond", "Triangle",
        #            "Cross", "XCross", "HLine", "VLine",
        #            "Star1", "Star2", "Hexagon", None,
        #            "Red", "Blue", "Green"]:
        #    if act is None:
        #        viewStyle.addSeparator()
        #    else:
        #        viewStyle.addAction(act, self.setPlotStyle)
        #self.viewMenu.addMenu(viewStyle)

        #self.viewMenu.addSeparator()
        #self.viewMenu.addAction(viewZoomOut15Action)
        #self.viewMenu.addAction(viewZoomIn15Action)
        #self.viewMenu.addAction(viewZoomAutoAction)
        #self.viewMenu.addSeparator()
        self.viewMenu.addAction("ORM SV", self.plotSVD)
        # a bug in PyQwt5 for datetime x-axis, waiting for Debian 7
        #self.viewMenu.addAction(viewDcct)
        #for ac in self.viewMenu.actions(): ac.setDisabled(True)

        #
        self.controlMenu = self.menuBar().addMenu("&Tools")
        
        self.controlMenu.addAction(
            QIcon(":/control_choosebpm.png"), "En-/Disable BPM",
            partial(chooseElement, 'BPM'))
        self.controlMenu.addAction(
            "En-/Disable COR", partial(chooseElement, 'COR'))
        #self.controlMenu.addAction(controlResetPvDataAction)
        self.controlMenu.addSeparator()
        self.controlMenu.addAction("Lattice Snapshot ...", self.openSnapshot)
        #self.controlMenu.addAction(controlZoomInPlot1Action)
        #self.controlMenu.addAction(controlZoomOutPlot1Action)
        #self.controlMenu.addAction(controlZoomInPlot2Action)
        #self.controlMenu.addAction(controlZoomOutPlot2Action)
        self.controlMenu.addSeparator()
        self.controlMenu.addAction("Correct Hor. orbit",
            partial(aphla.correctOrbit, plane="H"))
        self.controlMenu.addAction("Correct Vert. orbit",
            partial(aphla.correctOrbit, plane="V"))
        self.controlMenu.addAction(
            QIcon(":/control_corrorbit.png"), "Correct orbit",
            partial(aphla.correctOrbit, plane="HV"))
        #steer_orbit.setDisabled(True)
        self.controlMenu.addAction("Local Bump ...", self.createLocalBump)
        self.controlMenu.addAction("Element Editor ...", self.showElementEditor)
        self.controlMenu.addSeparator()
        self.controlMenu.addAction("meas Beta", self.physics.measBeta)
        self.controlMenu.addAction("meas Dispersion", self.physics.measDispersion)
        self.controlMenu.addAction("beam based alignment", self.runBba)
        #for ac in self.controlMenu.actions(): ac.setDisabled(True)

        # Window
        self.windowMenu = self.menuBar().addMenu("&Windows")
        #self.windowMenu.addAction(self.elemeditor.toggleViewAction())
        self.windowMenu.addAction(self.logdock.toggleViewAction())
        #viewDcct = QAction("Beam Current", self)
        #viewDcct.setCheckable(True)
        #viewDcct.setChecked(True)
        #self.connect(viewDcct, SIGNAL("toggled(bool)"), self.dcct.setVisible)
        #self.windowMenu.addAction(viewDcct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction("Cascade", self.mdiarea.cascadeSubWindows)
        self.windowMenu.addAction("Tile", self.mdiarea.tileSubWindows)
        self.windowMenu.addAction("Tile Horizontally",
                                  self.tileSubWindowsHorizontally)
        # "ctrl+page up", "ctrl+page down"
        self.windowMenu.addAction("Previous", self.mdiarea.activatePreviousSubWindow, "Ctrl+Left")
        self.windowMenu.addAction("Next", self.mdiarea.activateNextSubWindow, "Ctrl+Right")
        self.windowMenu.addSeparator()

        # debug
        self.debugMenu = self.menuBar().addMenu("&Debug")
        self.debugMenu.addAction("_Reset Correctors_", self._reset_correctors)
        self.debugMenu.addAction("_Reset Quadrupoles_", self._reset_quadrupoles)
        self.debugMenu.addAction("_Random V Kick_", self._random_vkick)
        self.debugMenu.addAction("_Random H Kick_", self._random_hkick)
        #for ac in self.debugMenu.actions(): ac.setDisabled(True)

        # help
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addAction("About mleap", self.showAbout)
                                                                         
        #toolbar
        machToolBar = self.addToolBar("Machines")
        self.machBox = QtGui.QComboBox()
        self.latBox = QtGui.QComboBox()
        #self.connect(self.latBox, SIGNAL("currentIndexChanged(QString)"), 
        #             self.__setLattice)
        machToolBar.addWidget(self.machBox)
        machToolBar.addWidget(self.latBox)
        #toolbar = QToolBar(self)
        #self.addToolBar(toolbar)
        #fileToolBar = self.addToolBar("File")
        #fileToolBar.setObjectName("FileToolBar")
        #fileToolBar.addAction(fileQuitAction)

        #
        viewToolBar1 = self.addToolBar("Live View")
        #viewToolBar.setObjectName("ViewToolBar")
        #viewToolBar.addAction(viewZoomOut15Action)
        #viewToolBar.addAction(viewZoomIn15Action)
        #viewToolBar.addAction(viewZoomAutoAction)
        #viewToolBar1.addAction(viewLiveAction)
        #viewToolBar1.addAction(viewSingleShotAction)
        #viewToolBar1.addSeparator()
        viewToolBar1.addAction(
            QIcon(":/new_bpm.png"), "Orbits",
            partial(self.newElementPlots, "BPM", "x,y"))
        viewToolBar1.addAction(
            QIcon(":/new_cor.png"), "Correctors",
            partial(self.newElementPlots, "COR", "x,y"))
        viewToolBar1.addAction(
            QIcon(":/new_quad.png"), "Quadrupoles",
            partial(self.newElementPlots, "QUAD", "b1"))
        viewToolBar1.addAction(
            QIcon(":/new_sext.png"), "Sextupoles",
            partial(self.newElementPlots, "SEXT", "b2"))
        #viewToolBar.addAction(viewErrorBarAction)
        #viewToolBar.addAction(QWhatsThis.createAction(self))

        #viewToolBar2 = self.addToolBar("Scale Plot")
        #zoomActions = [(":/view_zoom_xy.png", "Fit", self.scalePlot),
        #               (None, None, None),
        #               (":/view_zoom_y.png", "Fit In Y", self.scalePlot),
        #               (":/view_zoomin_y.png", "Zoom In Y", self.scalePlot),
        #               (":/view_zoomout_y.png", "Zoom Out Y", self.scalePlot),
        #               (":/view_move_up.png", "Move Up", self.scalePlot),
        #               (":/view_move_down.png", "Move Down", self.scalePlot),
        #               (None, None, None),
        #               (":/view_zoom_x.png", "Fit In X", self.scalePlot),
        #               (":/view_zoomin_x.png", "Zoom In X", self.scalePlot),
        #               (":/view_zoomout_x.png", "Zoom Out X", self.scalePlot),
        #               (":/view_move_left.png", "Move Left", self.scalePlot),
        #               (":/view_move_right.png", "Move Right", self.scalePlot),
        #               ]
        #for ico,name,hdl in zoomActions:
        #    if hdl is None: continue
        #    viewToolBar2.addAction(QIcon(ico), name, hdl)

        controlToolBar = self.addToolBar("Control")
        controlToolBar.addAction(
            QIcon(":/control_orbitcor.png"), "Correct Orbit",
            aphla.correctOrbit)
        controlToolBar.addAction(
            QIcon(":/control_localbump.png"), "Local Bump ...",
            self.createLocalBump)
        #controlToolBar.addAction(controlResetPvDataAction)

    def showAbout(self):
        QMessageBox.about(
            self, self.tr("mleap"),
            (self.tr("""<b>Machine/Lattice Editor And Plotter</b> v %1
                <p>Copyright &copy; Lingyun Yang, BNL, 2013-2014. 
                All rights reserved.
                <p>This application can be used to perform
                high level accelerator controls.
                <p>Python %2 - Qt %3 - PyQt %4 
                on %5""").arg(aphla.version.version)
                .arg(platform.python_version()).arg(QtCore.QT_VERSION_STR)
                .arg(QtCore.PYQT_VERSION_STR).arg(platform.system())))

    def showElementEditor(self):
        mach, lat = self.getCurrentMachLattice()
        ed = ElementEditor(lat, parent=self)
        ed.setWindowFlags(Qt.Window)
        ed.setAttribute(Qt.WA_DeleteOnClose)
        ed.show()

    def getCurrentMachLattice(self, cadata = False):
        """return the current machine name and lattice object"""
        mach     = str(self.machBox.currentText())
        latname  = str(self.latBox.currentText())
        lat_dict, lat0, pvm = self._mach[mach]
        if not cadata:
            return mach, lat_dict[latname]
        else:
            return mach, lat_dict[latname], pvm

    def newElementPlots(self, elem, fields, **kw):
        self.logger.info("new plots: %s %s" % (elem, fields))
        _mach, _lat, _pvm = self.getCurrentMachLattice(cadata=True)
        mach, lat = kw.get("machlat", (_mach, _lat))
        handle = kw.get("handle", "readback")
        elems = lat.getElementList(elem)
        x, pvs = [], []
        field_list = re.findall(r'[^ ,]+', fields)
        for fld in field_list:
            si, pvsi = [], []
            for e in elems:
                if not e.isEnabled(): continue
                epv = e.pv(field=fld, handle=handle)
                if not epv: continue
                pvsi.append(epv[0])
                si.append(e.sb)
            x.append(si)
            pvs.append(pvsi)

        if not pvs:
            self.logger.error("no data found for elements '{0}' "
                              "and field '{1}'".format(elem, field))
            return

        p = ApMdiSubPlot(pvs=pvs, x = x, 
                         labels=["%s.%s" % (elem,fld) for fld in field_list],
                         magprof = lat.getBeamlineProfile(),
                         iqt = self.iqtApp,
                         **kw)
        #QObject.installEventFilter(p.aplot)
        #p.data = ManagedPvData(pvm, s, pvs, element=elemnames,
        #                       label="{0}.{1}".format(elem,field))
        p.setAttribute(Qt.WA_DeleteOnClose)
        str_elem = "{0}".format(elem)
        if len(str_elem) > 12: str_elem = str_elem[:9] + "..."
        str_field = "{0}".format(fields)
        if len(str_field) > 12: str_field = str_field[:9] + "..."
        p.setWindowTitle("[%s.%s] %s %s" % (
                mach, lat.name, str_elem, str_field))
        self.connect(p, SIGNAL("elementSelected(PyQt_PyObject)"), 
                     self.elementSelected)
        self.connect(p, SIGNAL("destroyed()"), self.subPlotDestroyed)
        #p.updatePlot()
        # set the zoom stack
        #p.aplot.setErrorBar(self.error_bar)
        #p.wid.autoScaleXY()
        #p.aplot.replot()
        self.mdiarea.addSubWindow(p)
        #print "Show"
        p.show()

        ##print "Enable the buttons"
        #if len(self.mdiarea.subWindowList()) > 0:
        #    self.elemeditor.setEnabled(True)

    def subPlotDestroyed(self):
        #if len(self.mdiarea.subWindowList()) == 0:
        #    self.elemeditor.setEnabled(False)
        pass

    def loadOrm(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
            self, "Open Orbit Response Matrix",
            "",
            "ORM Files (*.h5 *.hdf5);;Text File (*.txt);;All Files(*)")
        fileName = str(fileName)
        try:
            m = np.loadtxt(fileName)
        except:
            QMessageBox.critical(self, "Abort", "Invalid matrix data")
            return
        mach, lat = self.getCurrentMachLattice()
        # assuming we already have the PV, name, field but just want to
        # replace the matrix elements.
        assert np.shape(m) == np.shape(lat.ormdata.m)
        nx, ny = np.shape(lat.ormdata.m)
        for i in range(nx):
            for j in range(ny):
                lat.ormdata.m[i,j] = m[i,j]


    def saveSnapshot(self):
        latdict = dict([(k,v[0]) for k,v in self._mach.items()])
        mach, lat = self.getCurrentMachLattice()
        snapdlg = SaveSnapshotDialog(latdict, mach)
        snapdlg.exec_()

    def saveLatSnapshot(self):
        mach, lat = self.getCurrentMachLattice()
        dpath = self._prepare_parent_dirs(mach)
        if not dpath:
            QMessageBox.warning(self, "Abort", "Aborted")
            return
        dt = datetime.datetime.now()
        fname = os.path.join(dpath,
            dt.strftime("snapshot_%d_%H%M%S_") + lat.name + ".hdf5")
        fileName = QtGui.QFileDialog.getSaveFileName(
            self, "Save Lattice Snapshot Data",
            fname,
            "Data Files (*.h5 *.hdf5);;All Files(*)")
        fileName = str(fileName)
        if not fileName: return
        aphla.catools.save_lat_epics(fileName, lat, mode='a')
        self.logger.info("snapshot created '%s'" % fileName)

    def saveMachSnapshot(self):
        mach, lat = self.getCurrentMachLattice()
        dpath = self._prepare_parent_dirs(mach)
        if not dpath:
            QMessageBox.warning(self, "Abort", "Aborted")
            return
        dt = datetime.datetime.now()
        fname = os.path.join(dpath, dt.strftime("snapshot_%d_%H%M%S.hdf5"))
        fileName = QtGui.QFileDialog.getSaveFileName(
            self, "Save Lattice Snapshot Data",
            fname,
            "Data Files (*.h5 *.hdf5);;All Files(*)")
        if not fileName: return
        fileName = str(fileName)
        import h5py
        f = h5py.File(str(fileName), 'w')
        f.close()
        self.logger.info("clean snapshot file created: '%s'" % fileName)
        for k,lat in self._mach[mach][0].items():
            aphla.catools.save_lat_epics(fileName, lat, mode='a')
            self.logger.info("lattice snapshot appended for '%s'" % lat.name)

    def openSnapshot(self):
        #self.logger.info("loading snapshot?")
        latdict = dict([(k,v[0]) for k,v in self._mach.items()])
        mach, lat = self.getCurrentMachLattice()
        lv = LatSnapshotMain(self, latdict, mach, self.logger)
        lv.setWindowFlags(Qt.Window)
        #self.logger.info("initialized")
        #lv.loadLatSnapshotH5()
        lv.exec_()

    def openTunePlot(self):
        mach, lat = self.getCurrentMachLattice()
        nu = lat.getElementList('tune')
        pvs = [(e.pv(field="x", handle="readback")[0],
                e.pv(field="y", handle="readback")[0])
               for e in nu]
        labels = [e.name for e in nu]
        twiss = lat.getElementList("VA")
        pvs.extend([(e.pv(field="nux", handle="readback")[0],
                     e.pv(field="nuy", handle="readback")[0])
                    for e in twiss])
        labels.extend([e.name for e in twiss])

        p = ApMdiSubPlot(pvs=pvs, labels=labels, dtype = "Tunes")
        #QObject.installEventFilter(p.aplot)
        #p.data = ManagedPvData(pvm, s, pvs, element=elemnames,
        #                       label="{0}.{1}".format(elem,field))
        p.setAttribute(Qt.WA_DeleteOnClose)
        p.setWindowTitle("[%s.%s] Tunes" % (mach, lat.name))
        self.connect(p, SIGNAL("elementSelected(PyQt_PyObject)"), 
                     self.elementSelected)
        self.connect(p, SIGNAL("destroyed()"), self.subPlotDestroyed)
        #p.updatePlot()
        # set the zoom stack
        #p.aplot.setErrorBar(self.error_bar)
        #p.wid.autoScaleXY()
        #p.aplot.replot()
        self.mdiarea.addSubWindow(p)
        #print "Show"
        p.show()

    def openNewPlot(self):
        mach, lat = self.getCurrentMachLattice()
        fl = QtGui.QFormLayout()
        fl.addRow("Machine", QtGui.QLabel("%s" % mach))
        fl.addRow("Lattice", QtGui.QLabel("%s" % lat.name))
        elem, fld = QtGui.QLineEdit(), QtGui.QLineEdit()
        fl.addRow("Elements", elem)
        fl.addRow("Field", fld)
        dtype = QtGui.QComboBox()
        for tx in ["Array", "Waveform", "Time Series"]:
            dtype.addItem(tx)
        fl.addRow("Data Type", dtype)
        dlg = QtGui.QDialog()
        bx = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok |
                                    QtGui.QDialogButtonBox.Cancel)
        self.connect(bx, SIGNAL("accepted()"), dlg.accept)
        self.connect(bx, SIGNAL("rejected()"), dlg.reject)
        h1 = QtGui.QHBoxLayout()
        h1.addStretch()
        h1.addWidget(bx)
        v1 = QtGui.QVBoxLayout()
        v1.addLayout(fl)
        v1.addLayout(h1)
        dlg.setLayout(v1)

        if dlg.exec_():
            self.newElementPlots(str(elem.text()), str(fld.text()),
                                 machlat=(mach, lat),
                                 dtype = str(dtype.currentText()))

    def click_markfam(self, on):
        famname = self.sender().text()
        mks = []
        mach, lat = self.getCurrentMachLattice()
        # need to convert to python str
        for elem in lat.getElementList(str(famname)):
            if elem.family != famname: continue
            if elem.virtual: continue
            mks.append([elem.name, 0.5*(elem.sb+elem.se)])

        for w in self.mdiarea.subWindowList(): w.setMarkers(mks, on)
        #print self._machlat.keys()

    def _reset_correctors(self):
        self.logger.info("reset correctors")
        aphla.hlalib._reset_trims()

    def _reset_quadrupoles(self):
        self.logger.info("reset quadrupoles")
        aphla.hlalib._reset_quad()

    def _random_hkick(self):
        mach, lat = self.getCurrentMachLattice()
        hcors = lat.getElementList('HCOR')
        for k in range(3):
            i = np.random.randint(len(hcors))
            self.logger.info("Setting {0}/{1} HCOR".format(i, len(hcors)))
            hcors[i].x += np.random.rand() * 2e-6


    def _random_vkick(self):
        mach, lat = self.getCurrentMachLattice()
        cors = lat.getElementList('VCOR')
        for k in range(3):
            i = np.random.randint(len(cors))
            cors[i].y += np.random.rand() * 1e-6
            self.logger.info("increased kicker '{0}' by 1e-7 ({1} {2})".format(
                cors[i].name, cors[i].y, cors[i].getUnit('y', None)))

    def viewDcctPlot(self, on):
        self.dcct.setVisible(on)

    def liveData(self, on):
        """Switch on/off live data taking"""
        self.live_orbit = on

    def scalePlot(self):
        w = self.mdiarea.currentSubWindow()
        if not w: return
        st, p = self.sender().text(), w.aplot
        if st == "Fit":
            p.scaleXBottom()
            p.scaleYLeft()
            # a hack
            bound = p.curvesBound()
            p.zoomer1.setZoomStack([bound])
        elif st == "Fit In Y":
            p.scaleYLeft()
        elif st == "Zoom In Y":
            p.scaleYLeft(1./1.5)
        elif st == "Zoom Out Y":
            p.scaleYLeft(1.5)
        elif st == "Move Up":
            p.moveCurves(Qwt.QwtPlot.yLeft, 0.8)
        elif st == "Move Down":
            p.moveCurves(Qwt.QwtPlot.yLeft, -0.8)
        elif st == "Fit In X":
            p.scaleXBottom()
        elif st == "Zoom In X":
            p.scaleXBottom(1.0/1.5)
        elif st == "Zoom Out X":
            p.scaleXBottom(1.5)            
        elif st == "Move Left":
            p.moveCurves(Qwt.QwtPlot.xBottom, 0.8)
        elif st == "Move Right":
            p.moveCurves(Qwt.QwtPlot.xBottom, -0.8)
        else:
            self.logger.error("unknow action '{0}'".format(st))

    def getVisibleRange(self):
        w = self.mdiarea.currentSubWindow()
        if not w: 
            mach, lat = self.getCurrentMachLattice()
            self.logger.warn("no active plot, use full range of {0}.{1}".format(
                mach, lat.name))
            return lat.getLocationRange()
        else:
            return w.currentXlim()
        
    def getVisibleElements(self, elemname, sb = None, se = None):
        w = self.mdiarea.currentSubWindow()
        mach, lat = self.getCurrentMachLattice()
        elems = lat.getElementList(elemname)
        if sb is not None: 
            elems = [e for e in elems if e.sb >= sb]
        if se is not None:
            elems = [e for e in elems if e.se <= se]

        self.logger.info("searching for '{0}' in range [{1}, {2}]".format(
            elemname, sb, se))

        return elems

    def timerEvent(self, e):
        if e.timerId() != self.timerId: return

        #if not self.elemeditor.isHidden():
        #    self.elemeditor.updateModelData()

        #if self.live_orbit:
        #    self.itimer += 1
        #    #self.updatePlots()
        #    #self.updateStatus()
        #    for w in self.mdiarea.subWindowList():
        #        if not isinstance(w, ApMdiSubPlot): continue
        #        if not w.live: continue
        #        w.updatePlot()
        #    self.statusBar().showMessage("plot updated: {0}".format(
        #        time.strftime("%F %T")))
        #else:
        #    self.statusBar().showMessage("live update disabled")
            
            
    def singleShot(self):
        for w in self.mdiarea.subWindowList():
            if not isinstance(w, ApMdiSubPlot):  continue
            w.updatePlot()

        self.statusBar().showMessage("plot updated: {0}".format(
            time.strftime("%F %T")))


    def elementSelected(self, elems):
        """this action is ignored"""
        mach, lat, elemnames = elems
        #_lat = self._machlat[mach][lat]
        self.logger.info("element selected")

        #elemobjs = _lat.getElementList(elemnames)
        #self._elemed.addElements(elemobjs)

    def activeOrbitPlot(self, field):
        mach = str(self.machBox.currentText())
        lat = str(self.latBox.currentText())
        for w in self.mdiarea.subWindowList():
            #print w.machine(), w.lattice(), w.data.yfield
            if not isinstance(w, ApMdiSubPlot):  continue
            if w.machine() != mach: continue
            if w.lattice() != lat: continue
            if w.data.yfield != field: continue
            return w

        return None

    def createLocalBump_(self):
        """create local bump"""
        if self._dlgOrbitCor is None:
            bpms = ap.getElements("BPM")
            cors = ap.getElements("COR")
            self._dlgOrbitCor = OrbitCorrDlg(bpms, cors)
            #corbitdlg.resize(600, 500)
            self._dlgOrbitCor.setWindowTitle("Create Local Bump")
        self._dlgOrbitCor.show()
        self._dlgOrbitCor.raise_()
        self._dlgOrbitCor.activateWindow()

    def createLocalBump(self):
        """create local bump"""
        bpms = ap.getElements("BPM")
        cors = ap.getElements("COR")
        dlgOrbitCor = OrbitCorrDlg(bpms, cors, parent=self)
        #corbitdlg.resize(600, 500)
        dlgOrbitCor.setWindowTitle("Create Local Bump")
        dlgOrbitCor.show()
        dlgOrbitCor.raise_()
        dlgOrbitCor.activateWindow()
        dlgOrbitCor.setAttribute(Qt.WA_DeleteOnClose)

    def runBba(self):
        mach, lat = self.getCurrentMachLattice()
        bpms = [e for e in lat.getElementList('BPM') 
                if e not in self.physics.deadelems]
        self.physics.runBba(bpms)

    def plotSVD(self):
        mach, lat = self.getCurrentMachLattice()
        if not lat.ormdata:
            QMessageBox.critical(self, "ORM SVD", 
                                 "machine '%s' ORM data is not available" % \
                                 mach,
                                 QMessageBox.Ok)
            return
        m, brec, trec = lat.ormdata.getMatrix(None, None, full=False, 
                                              ignore=self.getDeadElements())
        U, s, V = np.linalg.svd(m, full_matrices=True)
        #print np.shape(s), s
        self.sp = ApSvdPlot(s)
        self.sp.show()


    def tileSubWindowsHorizontally(self):
        pos = QtCore.QPoint(0, 0)
        subwins = self.mdiarea.subWindowList()
        for w in subwins:
            height = self.mdiarea.height()/len(subwins)
            rect = QtCore.QRect(0, 0, self.mdiarea.width(), height)
            w.setGeometry(rect)
            w.move(pos)
            pos.setY(pos.y() + w.height())

def main(par=None):
    #app.setStyle(st)
    app.setOverrideCursor(QtGui.QCursor(Qt.WaitCursor))
    app.setWindowIcon(QIcon(":/mainwin_2.png"))

    splash_px = QtGui.QPixmap(':/splash_screen_1.png')
    splash = QtGui.QSplashScreen(splash_px, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_px.mask())
    splash.setWindowFlags(Qt.SplashScreen)
    #splash.setWindowFlags(Qt.WindowStaysOnTopHint)
    rect = app.desktop().availableGeometry()
    splash.move((rect.width() - splash_px.width()) / 2,
                (rect.height() - splash_px.height()) / 2)
    
    mlist = os.environ.get('APHLA_MACHINES', '').split(";")
    splash.showMessage("Initializing {0}".format(mlist),
                       Qt.AlignRight | Qt.AlignBottom)
    splash.show()
    #splash.raise_()
    app.processEvents()
    time.sleep(0.1)
    app.processEvents()

    if not mlist: mlist = aphla.machines.machines()
    machs, infos = [], []
    for m in mlist:
        splash.showMessage("Initializing {0}".format(m),
                           Qt.AlignRight | Qt.AlignBottom)
        app.processEvents()
        lat0, latdict = aphla.machines.load(m, return_lattices=True)
        infos.append("%s initialized" % m)
        splash.showMessage("Connecting to {0}".format(m),
                           Qt.AlignRight | Qt.AlignBottom)
        app.processEvents()
        pvs = set()
        for latname, latobj in latdict.items():
            splash.showMessage("checking {0}.{1}".format(m, latname),
                               Qt.AlignRight | Qt.AlignBottom)            
            app.processEvents()
            for elem in latobj.getElementList("*"):
                pvs.update(elem.pv())


        # pv manager 
        #pvm = CaDataMonitor(timeout=5)
        #pvm.addPv(pvs)
        machs.append((m, latdict, lat0, None))

        #infos.append("%d out of %d PVs are alive" % (
        #    pvm.activeCount(), len(pvm)))
        infos.append("pvm is disabled")
    
    splash.showMessage("Using {0} as default machine".format(m),
                       Qt.AlignRight | Qt.AlignBottom)
    app.processEvents()
    
    mwin = OrbitPlotMainWindow(machines=machs, infos=infos, iqt=app)
    mwin.setWindowTitle("mleap - a high level lattice viewer and editor")
    splash.showMessage("Window created", Qt.AlignRight | Qt.AlignBottom)
    #demo = QtGui.QMainWindow()
    #demo.raise_()
    #demo.setLattice(aphla.machines.getLattice('V2SR'))
    #demo.setWindowTitle("NSLS-II")
    #mwin.resize(1000,600)
    #print aphla.machines.lattices()
    splash.finish(mwin)
    mwin.showMaximized()
    app.processEvents()
    app.restoreOverrideCursor()
    mwin.tileSubWindowsHorizontally()
    # print app.style() # QCommonStyle
    #sys.exit(app.exec_())
    cothread.WaitForQuit()


# Admire!
if __name__ == '__main__':
    # main(sys.argv)
    import cProfile
    cProfile.run('main()', "prfoutput.txt")

# Local Variables: ***
# mode: python ***
# End: ***
