#!/usr/bin/env python

"""
:author: Lingyun Yang <lyyang@bnl.gov>

A dialog for picking elements.
"""
# Copyright (c) 2011 Lingyun Yang @ BNL.

from PyQt4.QtCore import (Qt, SIGNAL)
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox,
        QGridLayout, QLabel, QSpinBox, QListWidget, QListWidgetItem,
        QAbstractItemView)


class ElementPickDlg(QDialog):

    def __init__(self, allelems, unchecked, parent=None,
                 title='Choose Elements:'):
        """elemobj"""
        super(ElementPickDlg, self).__init__(parent)
        self.setWindowTitle(title)
        self.elemlst = QListWidget()
        # enable multi-selection
        self.elemlst.setSelectionMode(QAbstractItemView.MultiSelection)
        for e in allelems:
            w = QListWidgetItem(e)
            w.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsSelectable |
                       Qt.ItemIsEnabled)
            if e not in unchecked: w.setCheckState(Qt.Checked)
            else: w.setCheckState(Qt.Unchecked)
            self.elemlst.addItem(w)
        #self.elemlst.setSortingEnabled(True)

        elemLabel = QLabel(title)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                     QDialogButtonBox.Cancel)

        layout = QGridLayout()
        layout.addWidget(elemLabel, 0, 0)
        layout.addWidget(self.elemlst, 1, 0)
        layout.addWidget(buttonBox, 2, 0)
        self.setLayout(layout)

        self.connect(buttonBox, SIGNAL("accepted()"), self.accept)
        self.connect(buttonBox, SIGNAL("rejected()"), self.reject)



    def result(self):
        #print self.elemlst.selectedItems()
        ret = []
        for i in range(self.elemlst.count()):
            if self.elemlst.item(i).checkState() == Qt.Checked:
                ret.append(str(self.elemlst.item(i).text()))
        return ret


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = ElementPickDlg([('elem 1', Qt.Unchecked), ('elem 2', Qt.Checked)])
    form.show()
    app.exec_()

    print "selected: ", form.result()
