# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_launcher_pref.ui'
#
# Created: Tue Feb 11 14:34:37 2014
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
        Dialog.resize(344, 291)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.comboBox_font_size = QtGui.QComboBox(Dialog)
        self.comboBox_font_size.setEditable(False)
        self.comboBox_font_size.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox_font_size.setObjectName(_fromUtf8("comboBox_font_size"))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.comboBox_font_size.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.comboBox_font_size)
        spacerItem = QtGui.QSpacerItem(210, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(20, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget_visible_columns = QtGui.QListWidget(Dialog)
        self.listWidget_visible_columns.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget_visible_columns.setAlternatingRowColors(True)
        self.listWidget_visible_columns.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.listWidget_visible_columns.setResizeMode(QtGui.QListView.Adjust)
        self.listWidget_visible_columns.setObjectName(_fromUtf8("listWidget_visible_columns"))
        self.horizontalLayout.addWidget(self.listWidget_visible_columns)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_edit_visible_columns = QtGui.QPushButton(Dialog)
        self.pushButton_edit_visible_columns.setMaximumSize(QtCore.QSize(61, 16777215))
        self.pushButton_edit_visible_columns.setObjectName(_fromUtf8("pushButton_edit_visible_columns"))
        self.verticalLayout.addWidget(self.pushButton_edit_visible_columns)
        spacerItem2 = QtGui.QSpacerItem(20, 77, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox_view_mode = QtGui.QComboBox(Dialog)
        self.comboBox_view_mode.setObjectName(_fromUtf8("comboBox_view_mode"))
        self.comboBox_view_mode.addItem(_fromUtf8(""))
        self.comboBox_view_mode.addItem(_fromUtf8(""))
        self.comboBox_view_mode.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_view_mode)
        spacerItem3 = QtGui.QSpacerItem(131, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.checkBox_side_pane_visible = QtGui.QCheckBox(Dialog)
        self.checkBox_side_pane_visible.setChecked(True)
        self.checkBox_side_pane_visible.setObjectName(_fromUtf8("checkBox_side_pane_visible"))
        self.horizontalLayout_4.addWidget(self.checkBox_side_pane_visible)
        spacerItem4 = QtGui.QSpacerItem(191, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.pushButton_restore_default = QtGui.QPushButton(Dialog)
        self.pushButton_restore_default.setObjectName(_fromUtf8("pushButton_restore_default"))
        self.horizontalLayout_6.addWidget(self.pushButton_restore_default)
        spacerItem5 = QtGui.QSpacerItem(92, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_6.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        self.comboBox_font_size.setCurrentIndex(3)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Startup Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Font Size", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(0, QtGui.QApplication.translate("Dialog", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(1, QtGui.QApplication.translate("Dialog", "12", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(2, QtGui.QApplication.translate("Dialog", "14", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(3, QtGui.QApplication.translate("Dialog", "16", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(4, QtGui.QApplication.translate("Dialog", "18", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(5, QtGui.QApplication.translate("Dialog", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(6, QtGui.QApplication.translate("Dialog", "24", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(7, QtGui.QApplication.translate("Dialog", "28", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(8, QtGui.QApplication.translate("Dialog", "32", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(9, QtGui.QApplication.translate("Dialog", "36", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(10, QtGui.QApplication.translate("Dialog", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(11, QtGui.QApplication.translate("Dialog", "45", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_font_size.setItemText(12, QtGui.QApplication.translate("Dialog", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Visible Columns", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_edit_visible_columns.setText(QtGui.QApplication.translate("Dialog", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "View Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_view_mode.setItemText(0, QtGui.QApplication.translate("Dialog", "Icon View", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_view_mode.setItemText(1, QtGui.QApplication.translate("Dialog", "List View", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_view_mode.setItemText(2, QtGui.QApplication.translate("Dialog", "Details View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Side Pane", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_side_pane_visible.setText(QtGui.QApplication.translate("Dialog", "Visible", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_restore_default.setText(QtGui.QApplication.translate("Dialog", "Restore Default", None, QtGui.QApplication.UnicodeUTF8))

