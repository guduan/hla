# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_channel_explorer_startup_set_dialog.ui'
#
# Created: Wed Feb 26 12:57:31 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(678, 497)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.listWidget_group = QtGui.QListWidget(self.splitter)
        self.listWidget_group.setObjectName(_fromUtf8("listWidget_group"))
        item = QtGui.QListWidgetItem()
        self.listWidget_group.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget_group.addItem(item)
        self.stackedWidget = QtGui.QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_misc = QtGui.QWidget()
        self.page_misc.setObjectName(_fromUtf8("page_misc"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_misc)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.page_misc)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_filter_mode = QtGui.QComboBox(self.page_misc)
        self.comboBox_filter_mode.setObjectName(_fromUtf8("comboBox_filter_mode"))
        self.comboBox_filter_mode.addItem(_fromUtf8(""))
        self.comboBox_filter_mode.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_filter_mode, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.page_misc)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_case_sensitivity = QtGui.QComboBox(self.page_misc)
        self.comboBox_case_sensitivity.setObjectName(_fromUtf8("comboBox_case_sensitivity"))
        self.comboBox_case_sensitivity.addItem(_fromUtf8(""))
        self.comboBox_case_sensitivity.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_case_sensitivity, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.page_misc)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_column_sorting = QtGui.QComboBox(self.page_misc)
        self.comboBox_column_sorting.setObjectName(_fromUtf8("comboBox_column_sorting"))
        self.comboBox_column_sorting.addItem(_fromUtf8(""))
        self.comboBox_column_sorting.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_column_sorting, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.page_misc)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_machine = QtGui.QComboBox(self.page_misc)
        self.comboBox_machine.setObjectName(_fromUtf8("comboBox_machine"))
        self.comboBox_machine.addItem(_fromUtf8(""))
        self.comboBox_machine.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_machine, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.page_misc)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_lattice_name = QtGui.QComboBox(self.page_misc)
        self.comboBox_lattice_name.setObjectName(_fromUtf8("comboBox_lattice_name"))
        self.gridLayout.addWidget(self.comboBox_lattice_name, 4, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 281, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_misc)
        self.page_column_visibility_order = QtGui.QWidget()
        self.page_column_visibility_order.setObjectName(_fromUtf8("page_column_visibility_order"))
        self.stackedWidget.addWidget(self.page_column_visibility_order)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.pushButton_restore_default = QtGui.QPushButton(Dialog)
        self.pushButton_restore_default.setObjectName(_fromUtf8("pushButton_restore_default"))
        self.horizontalLayout_7.addWidget(self.pushButton_restore_default)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_7.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Startup Settings", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.listWidget_group.isSortingEnabled()
        self.listWidget_group.setSortingEnabled(False)
        item = self.listWidget_group.item(0)
        item.setText(QtGui.QApplication.translate("Dialog", "Columns", None, QtGui.QApplication.UnicodeUTF8))
        item = self.listWidget_group.item(1)
        item.setText(QtGui.QApplication.translate("Dialog", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.listWidget_group.setSortingEnabled(__sortingEnabled)
        self.label.setText(QtGui.QApplication.translate("Dialog", "Filter Mode:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_mode.setItemText(0, QtGui.QApplication.translate("Dialog", "Simple", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_filter_mode.setItemText(1, QtGui.QApplication.translate("Dialog", "Advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Case-Sensitivity:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_case_sensitivity.setItemText(0, QtGui.QApplication.translate("Dialog", "sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_case_sensitivity.setItemText(1, QtGui.QApplication.translate("Dialog", "insensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Column Sorting:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_column_sorting.setItemText(0, QtGui.QApplication.translate("Dialog", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_column_sorting.setItemText(1, QtGui.QApplication.translate("Dialog", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Machine:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_machine.setItemText(0, QtGui.QApplication.translate("Dialog", "NSLS2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_machine.setItemText(1, QtGui.QApplication.translate("Dialog", "NSLS2V2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Lattice Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_restore_default.setText(QtGui.QApplication.translate("Dialog", "Restore Default", None, QtGui.QApplication.UnicodeUTF8))

