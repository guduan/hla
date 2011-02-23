#!/usr/bin/env python

# for debugging, requires: python configure.py --trace ...
if 0:
    import sip
    sip.settracemask(0x3f)

import sys
from PyQt4 import Qt, QtCore, QtGui
import PyQt4.Qwt5 as Qwt
from PyQt4.Qwt5.anynumpy import *
class Spy(Qt.QObject):
    
    def __init__(self, parent):
        Qt.QObject.__init__(self, parent)
        parent.setMouseTracking(True)
        parent.installEventFilter(self)

    # __init__()

    def eventFilter(self, _, event):
        if event.type() == Qt.QEvent.MouseMove:
            self.emit(Qt.SIGNAL("MouseMove"), event.pos())
        return False

    # eventFilter()

# class Spy

class OrbitData(Qt.QObject):
    def __init__(self, parent = None):
        super(OrbitData, self).__init__(parent)
        self.nsample = 10
        self.isample = 0
        self.points = 20
        self.__x = zeros((self.nsample, self.points), 'd')
        self.__y = zeros((self.nsample, self.points), 'd')
        self.__dx = zeros(self.points, 'd')
        self.__dy = zeros(self.points, 'd')

        self.timerId = self.startTimer(200)

    def timerEvent(self, e):
        self.isample = (self.isample + 1) % self.nsample
        
        t = arange(self.points)
        self.__x[self.isample, :] = t + .1*random.random(self.points)
        self.__y[self.isample, :] = sin(0.3*t) + 0.3*random.random(self.points)
        
    def setSamples(self, n):
        if n == self.nsample: return
        tx, ty = self.__x, self.__y
        self.__x = zeros((n, self.points), 'd')
        self.__y = zeros((n, self.points), 'd')
        self.__x[:self.nsample, :] = tx[:, :]
        self.__y[:self.nsample, :] = ty[:, :]
        self.nsample = n

    def x(self):
        return self.__x[self.isample,:]

    def y(self):
        return self.__y[self.isample,:]

    def dx(self):
        return std(self.__x[:,:], axis=0)

    def dy(self):
        return std(self.__y[:,:], axis=0)

    def stop(self):
        self.killTimer(self.timerId)
        self.timerId = -1

    def start(self):
        if self.timerId > 0:
            self.killTimer(self.timerId)
        self.timerId = self.startTimer() 

class OrbitPlotCurve(Qwt.QwtPlotCurve):

    def __init__(self,
                 curvePen = Qt.QPen(Qt.Qt.NoPen),
                 curveStyle = Qwt.QwtPlotCurve.Lines,
                 curveSymbol = Qwt.QwtSymbol(),
                 errorPen = Qt.QPen(Qt.Qt.NoPen),
                 errorCap = 0,
                 errorOnTop = False,
                 ):
        """A curve of x versus y data with error bars in dx and dy.

        Horizontal error bars are plotted if dx is not None.
        Vertical error bars are plotted if dy is not None.

        - curvePen is the pen used to plot the curve
        - curveStyle is the style used to plot the curve
        - curveSymbol is the symbol used to plot the symbols
        - errorPen is the pen used to plot the error bars
        - errorCap is the size of the error bar caps
        - errorOnTop is a boolean:

            - if True, plot the error bars on top of the curve,
            - if False, plot the curve on top of the error bars.
        """

        Qwt.QwtPlotCurve.__init__(self)
        self.setPen(curvePen)
        self.setStyle(curveStyle)
        self.setSymbol(curveSymbol)
        self.errorPen = errorPen
        self.errorCap = errorCap
        self.errorOnTop = errorOnTop

        self.__x = None
        self.__y = None
        self.__dx = None
        self.__dy = None

    # __init__()

    def setData(self, x, y, dx = None, dy = None):
        """Set x versus y data with error bars in dx and dy.

        Horizontal error bars are plotted if dx is not None.
        Vertical error bars are plotted if dy is not None.

        x and y must be sequences with a shape (N,) and dx and dy must be
        sequences (if not None) with a shape (), (N,), or (2, N):
        - if dx or dy has a shape () or (N,), the error bars are given by
          (x-dx, x+dx) or (y-dy, y+dy),
        - if dx or dy has a shape (2, N), the error bars are given by
          (x-dx[0], x+dx[1]) or (y-dy[0], y+dy[1]).
        """
        
        self.__x = asarray(x, Float)
        if len(self.__x.shape) != 1:
            raise RuntimeError, 'len(asarray(x).shape) != 1'

        self.__y = asarray(y, Float)
        if len(self.__y.shape) != 1:
            raise RuntimeError, 'len(asarray(y).shape) != 1'
        if len(self.__x) != len(self.__y):
            raise RuntimeError, 'len(asarray(x)) != len(asarray(y))' 

        if dx is None:
            self.__dx = None
        else:
            self.__dx = asarray(dx, Float)
        if len(self.__dx.shape) not in [0, 1, 2]:
            raise RuntimeError, 'len(asarray(dx).shape) not in [0, 1, 2]'
            
        if dy is None:
            self.__dy = dy
        else:
            self.__dy = asarray(dy, Float)
        if len(self.__dy.shape) not in [0, 1, 2]:
            raise RuntimeError, 'len(asarray(dy).shape) not in [0, 1, 2]'
        
        Qwt.QwtPlotCurve.setData(self, self.__x, self.__y)

    # setData()
        
    def boundingRect(self):
        """Return the bounding rectangle of the data, error bars included.
        """
        if self.__x is None and self.__y is None:
            return Qt.QRectF(.0, 1.0, 1.0, 0.0)

        if self.__dx is None:
            xmin = min(self.__x)
            xmax = max(self.__x)
        elif len(self.__dx.shape) in [0, 1]:
            xmin = min(self.__x - self.__dx)
            xmax = max(self.__x + self.__dx)
        else:
            xmin = min(self.__x - self.__dx[0])
            xmax = max(self.__x + self.__dx[1])

        if self.__dy is None:
            ymin = min(self.__y)
            ymax = max(self.__y)
        elif len(self.__dy.shape) in [0, 1]:
            ymin = min(self.__y - self.__dy)
            ymax = max(self.__y + self.__dy)
        else:
            ymin = min(self.__y - self.__dy[0])
            ymax = max(self.__y + self.__dy[1])

        return Qt.QRectF(xmin, ymin, xmax-xmin, ymax-ymin)
        
    # boundingRect()

    def drawFromTo(self, painter, xMap, yMap, first, last = -1):
        """Draw an interval of the curve, including the error bars

        painter is the QPainter used to draw the curve

        xMap is the Qwt.QwtDiMap used to map x-values to pixels

        yMap is the Qwt.QwtDiMap used to map y-values to pixels
        
        first is the index of the first data point to draw

        last is the index of the last data point to draw. If last < 0, last
        is transformed to index the last data point
        """

        if last < 0:
            last = self.dataSize() - 1

        if self.errorOnTop:
            Qwt.QwtPlotCurve.drawFromTo(self, painter, xMap, yMap, first, last)

        # draw the error bars
        painter.save()
        painter.setPen(self.errorPen)

        # draw the error bars with caps in the x direction
        if self.__dx is not None:
            # draw the bars
            if len(self.__dx.shape) in [0, 1]:
                xmin = (self.__x - self.__dx)
                xmax = (self.__x + self.__dx)
            else:
                xmin = (self.__x - self.__dx[0])
                xmax = (self.__x + self.__dx[1])
            y = self.__y
            n, i = len(y), 0
            lines = []
            while i < n:
                yi = yMap.transform(y[i])
                lines.append(Qt.QLine(xMap.transform(xmin[i]), yi,
                                          xMap.transform(xmax[i]), yi))
                i += 1
            painter.drawLines(lines)
            if self.errorCap > 0:
                # draw the caps
                cap = self.errorCap/2
                n, i, = len(y), 0
                lines = []
                while i < n:
                    yi = yMap.transform(y[i])
                    lines.append(
                        Qt.QLine(xMap.transform(xmin[i]), yi - cap,
                                     xMap.transform(xmin[i]), yi + cap))
                    lines.append(
                        Qt.QLine(xMap.transform(xmax[i]), yi - cap,
                                     xMap.transform(xmax[i]), yi + cap))
                    i += 1
            painter.drawLines(lines)

        # draw the error bars with caps in the y direction
        if self.__dy is not None:
            # draw the bars
            if len(self.__dy.shape) in [0, 1]:
                ymin = (self.__y - self.__dy)
                ymax = (self.__y + self.__dy)
            else:
                ymin = (self.__y - self.__dy[0])
                ymax = (self.__y + self.__dy[1])
            x = self.__x
            n, i, = len(x), 0
            lines = []
            while i < n:
                xi = xMap.transform(x[i])
                lines.append(
                    Qt.QLine(xi, yMap.transform(ymin[i]),
                                 xi, yMap.transform(ymax[i])))
                i += 1
            painter.drawLines(lines)
            # draw the caps
            if self.errorCap > 0:
                cap = self.errorCap/2
                n, i, j = len(x), 0, 0
                lines = []
                while i < n:
                    xi = xMap.transform(x[i])
                    lines.append(
                        Qt.QLine(xi - cap, yMap.transform(ymin[i]),
                                     xi + cap, yMap.transform(ymin[i])))
                    lines.append(
                        Qt.QLine(xi - cap, yMap.transform(ymax[i]),
                                     xi + cap, yMap.transform(ymax[i])))
                    i += 1
            painter.drawLines(lines)

        painter.restore()

        if not self.errorOnTop:
            Qwt.QwtPlotCurve.drawFromTo(self, painter, xMap, yMap, first, last)

    # drawFromTo()

# class OrbitPlotCurve

class OrbitPlot(Qwt.QwtPlot):
    def __init__(self, *args):
        Qwt.QwtPlot.__init__(self, *args)
        
        self.data = OrbitData()

        self.setCanvasBackground(Qt.Qt.white)
        #self.alignScales()

        # Initialize data
        errorOnTop = False # uncomment to draw the curve on top of the error bars
        # errorOnTop = True # uncomment to draw the error bars on top of the curve
        
        #self.setTitle("An Orbit Plot")
        #self.insertLegend(Qwt.QwtLegend(), Qwt.QwtPlot.BottomLegend);

        #self.setAxisScale(Qwt.QwtPlot.xBottom, 0, 100)
        self.plotLayout().setAlignCanvasToScales(True)

        self.curve1 = OrbitPlotCurve(
            curvePen = Qt.QPen(Qt.Qt.black, 2),
            curveSymbol = Qwt.QwtSymbol(Qwt.QwtSymbol.Ellipse,
                                        Qt.QBrush(Qt.Qt.red),
                                        Qt.QPen(Qt.Qt.black, 2),
                                        Qt.QSize(9, 9)),
            errorPen = Qt.QPen(Qt.Qt.blue, 2),
            errorCap = 10,
            errorOnTop = errorOnTop,
            )

        self.curve1.setData(self.data.x(), self.data.y(),
                            self.data.dx(), self.data.dy())

        self.curve1.attach(self)
        self.bound = self.curve1.boundingRect()
        #print "BD",self.bound
        #.resize(400, 300)
        grid1 = Qwt.QwtPlotGrid()
        grid1.attach(self)
        grid1.setPen(Qt.QPen(Qt.Qt.black, 0, Qt.Qt.DotLine))

        picker1 = Qwt.QwtPlotPicker(Qwt.QwtPlot.xBottom,
                                   Qwt.QwtPlot.yLeft,
                                   Qwt.QwtPicker.NoSelection,
                                   Qwt.QwtPlotPicker.CrossRubberBand,
                                   Qwt.QwtPicker.AlwaysOn,
                                   self.canvas())
        picker1.setTrackerPen(Qt.QPen(Qt.Qt.red))
        
        
        self.timerId = self.startTimer(300)

        #self.phase = 0.0

    def alignScales(self):
        self.canvas().setFrameStyle(Qt.QFrame.Box | Qt.QFrame.Plain)
        self.canvas().setLineWidth(1)
        for i in range(Qwt.QwtPlot.axisCnt):
            scaleWidget = self.axisWidget(i)
            if scaleWidget:
                scaleWidget.setMargin(0)
            scaleDraw = self.axisScaleDraw(i)
            if scaleDraw:
                scaleDraw.enableComponent(
                    Qwt.QwtAbstractScaleDraw.Backbone, False)

    # alignScales()

    def timerEvent(self, e):
        # y moves from left to right:
        # shift y array right and assign new value y[0]
        #self.y = concatenate((self.y[:1], self.y[:-1]), 1)

        self.curve1.setData(self.data.x(), self.data.y(),
                            self.data.dx(), self.data.dy())

        #self.setAxisScale(Qwt.QwtPlot.xBottom, min(self.x), max(self.x))
        #self.setAxisScale(Qwt.QwtPlot.yLeft, 0, 2)

        #self.setAxisAutoScale(Qwt.QwtPlot.xBottom)
        #self.setAxisAutoScale(Qwt.QwtPlot.yLeft)
        #print self.curve1.boundingRect()
        #print self.bound

        #self.bound.united(self.curve1.boundingRect())
        #bd = self.curve1.boundingRect()
        #print "returned", bd.left(), bd.right(), bd.top(), bd.bottom()
        #self.bound = self.bound.united(self.curve1.boundingRect())
        #print self.bound.left(), self.bound.right()
        #print "B-T",self.bound.bottom(), self.bound.top()

        #self.setAxisScale(Qwt.QwtPlot.xBottom,
        #                  self.bound.left(), self.bound.right())
        #self.setAxisScale(Qwt.QwtPlot.yLeft,
        #                  self.bound.top(), self.bound.bottom())
        
        #self.setAxisScale(Qwt.QwtPlot.yLeft, 0, 2)

        self.replot()
        #self.zoomer1.setZoomBase()


    def liveData(self, on):
        #print "Working on timer:", self.timerId, 
        if on:
            self.timerId = self.startTimer(100)
            #print "Enable timer:", self.timerId
        else:
            self.killTimer(self.timerId)
            #print "Disabled timer:", self.timerId
            self.timerId = 0
            
    def scaleVertical(self, factor):
        scalediv = self.axisScaleDiv(Qwt.QwtPlot.yLeft)
        sr, sl = scalediv.upperBound(), scalediv.lowerBound()
        dy = (sr - sl)*(factor - 1)/2.0
        #print "bound:",scalediv.lowerBound(), scalediv.upperBound()
        self.setAxisScale(Qwt.QwtPlot.yLeft, sl - dy, sr + dy)

    def zoomAuto(self):
        bound = self.curve1.boundingRect()
        w = bound.width()
        h = bound.height()
        xmin = bound.left() - w*.05
        xmax = bound.right() + w*.05
        ymin = bound.top() - h*.08
        ymax = bound.bottom() + h*.08

        self.setAxisScale(Qwt.QwtPlot.xBottom, xmin, xmax)
        self.setAxisScale(Qwt.QwtPlot.yLeft, ymin, ymax)

class OrbitPlotMainWindow(Qt.QMainWindow):

    def __init__(self, parent = None):
        Qt.QMainWindow.__init__(self, parent)

        # initialize a QwtPlot central widget

        self.plot1 = OrbitPlot(self)
        self.plot2 = OrbitPlot(self)

        self.plot1.plotLayout().setCanvasMargin(4)
        self.plot1.plotLayout().setAlignCanvasToScales(True)
        self.plot1.setTitle("Horizontal Orbit")
        self.plot2.plotLayout().setCanvasMargin(4)
        self.plot2.plotLayout().setAlignCanvasToScales(True)
        self.plot2.setTitle("Vertical Orbit")

        wid = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.plot1)
        vbox.addWidget(self.plot2)
        wid.setLayout(vbox)
        self.setCentralWidget(wid)

        self.zoomer1 = Qwt.QwtPlotZoomer(Qwt.QwtPlot.xBottom,
                                        Qwt.QwtPlot.yLeft,
                                        Qwt.QwtPicker.DragSelection,
                                        Qwt.QwtPicker.AlwaysOff,
                                        self.plot1.canvas())
        self.zoomer1.setRubberBandPen(Qt.QPen(Qt.Qt.black))

        self.zoomer2 = Qwt.QwtPlotZoomer(Qwt.QwtPlot.xBottom,
                                        Qwt.QwtPlot.yLeft,
                                        Qwt.QwtPicker.DragSelection,
                                        Qwt.QwtPicker.AlwaysOff,
                                        self.plot2.canvas())
        self.zoomer2.setRubberBandPen(Qt.QPen(Qt.Qt.black))

        #self.setCentralWidget(OrbitPlot())

        toolbar = Qt.QToolBar(self)
        self.addToolBar(toolbar)
        
        self.statusBar().showMessage('Hello;')

        #
        # file menu
        #
        self.fileMenu = self.menuBar().addMenu("&File")
        fileQuitAction = Qt.QAction("&Quit", self)
        fileQuitAction.setShortcut("Ctrl+Q")
        fileQuitAction.setToolTip("Quit the application")
        fileQuitAction.setStatusTip("Quit the application")
        self.connect(fileQuitAction, Qt.SIGNAL("triggered()"),
                     self.close)
        #
        self.fileMenu.addAction(fileQuitAction)

        # view
        self.viewMenu = self.menuBar().addMenu("&View")
        # live data
        viewLiveAction = Qt.QAction("Live", self)
        viewLiveAction.setCheckable(True)
        viewLiveAction.setChecked(True)
        self.connect(viewLiveAction, Qt.SIGNAL("toggled(bool)"),
                     self.liveData)
        # scale
        viewZoomOut15Action = Qt.QAction("Zoom out x1.5", self)
        self.connect(viewZoomOut15Action, Qt.SIGNAL("triggered()"),
                     self.zoomOut15)
        viewZoomIn15Action = Qt.QAction("Zoom in x1.5", self)
        self.connect(viewZoomIn15Action, Qt.SIGNAL("triggered()"),
                     self.zoomIn15)
        viewZoomAutoAction = Qt.QAction("Auto Fit", self)
        self.connect(viewZoomAutoAction, Qt.SIGNAL("triggered()"),
                     self.zoomAuto)

        self.viewMenu.addAction(viewZoomOut15Action)
        self.viewMenu.addAction(viewZoomIn15Action)
        self.viewMenu.addAction(viewZoomAutoAction)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(viewLiveAction)

        # help
        self.helpMenu = self.menuBar().addMenu("&Help")
        

    def liveData(self, on):
        """Switch on/off live data taking"""
        self.plot1.liveData(on)
        self.plot2.liveData(on)

    def zoomOut15(self):
        self.plot1.scaleVertical(1.5)
        self.plot2.scaleVertical(1.5)

    def zoomIn15(self):
        self.plot1.scaleVertical(1.0/1.5)
        self.plot2.scaleVertical(1.0/1.5)

    def zoomAuto(self):
        self.plot1.zoomAuto()
        self.plot2.zoomAuto()

def main(args):
    app = Qt.QApplication(args)

    demo = OrbitPlotMainWindow()
    demo.resize(800,600)
    demo.show()

    sys.exit(app.exec_())

# main()


# Admire!
if __name__ == '__main__':
    main(sys.argv)

# Local Variables: ***
# mode: python ***
# End: ***