# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tinkerConfigDBSelector.ui'
#
# Created: Thu Mar  6 12:12:11 2014
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
        Dialog.resize(1070, 725)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem = QtGui.QSpacerItem(412, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 1, 1, 1)
        self.pushButton_preferences = QtGui.QPushButton(Dialog)
        self.pushButton_preferences.setObjectName(_fromUtf8("pushButton_preferences"))
        self.gridLayout_3.addWidget(self.pushButton_preferences, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_3.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.splitter_2 = QtGui.QSplitter(self.splitter)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.groupBox_search_params = QtGui.QGroupBox(self.splitter_2)
        self.groupBox_search_params.setObjectName(_fromUtf8("groupBox_search_params"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_search_params)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox_search_params)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_config_id_1 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_config_id_1.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_config_id_1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_config_id_1.setObjectName(_fromUtf8("comboBox_config_id_1"))
        self.comboBox_config_id_1.addItem(_fromUtf8(""))
        self.comboBox_config_id_1.setItemText(0, _fromUtf8(""))
        self.comboBox_config_id_1.addItem(_fromUtf8(""))
        self.comboBox_config_id_1.addItem(_fromUtf8(""))
        self.comboBox_config_id_1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_config_id_1, 0, 1, 1, 1)
        self.lineEdit_config_id_1 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_config_id_1.setObjectName(_fromUtf8("lineEdit_config_id_1"))
        self.gridLayout.addWidget(self.lineEdit_config_id_1, 0, 2, 1, 2)
        self.comboBox_config_id_2 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_config_id_2.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_config_id_2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_config_id_2.setObjectName(_fromUtf8("comboBox_config_id_2"))
        self.comboBox_config_id_2.addItem(_fromUtf8(""))
        self.comboBox_config_id_2.setItemText(0, _fromUtf8(""))
        self.comboBox_config_id_2.addItem(_fromUtf8(""))
        self.comboBox_config_id_2.addItem(_fromUtf8(""))
        self.comboBox_config_id_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_config_id_2, 0, 4, 1, 1)
        self.lineEdit_config_id_2 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_config_id_2.setObjectName(_fromUtf8("lineEdit_config_id_2"))
        self.gridLayout.addWidget(self.lineEdit_config_id_2, 0, 5, 1, 2)
        self.label_6 = QtGui.QLabel(self.groupBox_search_params)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.comboBox_ref_step_size_1 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_ref_step_size_1.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_ref_step_size_1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_ref_step_size_1.setObjectName(_fromUtf8("comboBox_ref_step_size_1"))
        self.comboBox_ref_step_size_1.addItem(_fromUtf8(""))
        self.comboBox_ref_step_size_1.setItemText(0, _fromUtf8(""))
        self.comboBox_ref_step_size_1.addItem(_fromUtf8(""))
        self.comboBox_ref_step_size_1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_ref_step_size_1, 1, 1, 1, 1)
        self.lineEdit_ref_step_size_1 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_ref_step_size_1.setObjectName(_fromUtf8("lineEdit_ref_step_size_1"))
        self.gridLayout.addWidget(self.lineEdit_ref_step_size_1, 1, 2, 1, 2)
        self.comboBox_ref_step_size_2 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_ref_step_size_2.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_ref_step_size_2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_ref_step_size_2.setObjectName(_fromUtf8("comboBox_ref_step_size_2"))
        self.comboBox_ref_step_size_2.addItem(_fromUtf8(""))
        self.comboBox_ref_step_size_2.setItemText(0, _fromUtf8(""))
        self.comboBox_ref_step_size_2.addItem(_fromUtf8(""))
        self.comboBox_ref_step_size_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_ref_step_size_2, 1, 4, 1, 1)
        self.lineEdit_ref_step_size_2 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_ref_step_size_2.setObjectName(_fromUtf8("lineEdit_ref_step_size_2"))
        self.gridLayout.addWidget(self.lineEdit_ref_step_size_2, 1, 5, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox_search_params)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_config_name = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_config_name.setObjectName(_fromUtf8("lineEdit_config_name"))
        self.gridLayout.addWidget(self.lineEdit_config_name, 2, 1, 1, 6)
        self.label_4 = QtGui.QLabel(self.groupBox_search_params)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_config_description = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_config_description.setObjectName(_fromUtf8("lineEdit_config_description"))
        self.gridLayout.addWidget(self.lineEdit_config_description, 3, 1, 1, 6)
        self.label_5 = QtGui.QLabel(self.groupBox_search_params)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_username = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.gridLayout.addWidget(self.lineEdit_username, 4, 1, 1, 6)
        self.label_8 = QtGui.QLabel(self.groupBox_search_params)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.comboBox_time_created_1 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_time_created_1.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_time_created_1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_time_created_1.setObjectName(_fromUtf8("comboBox_time_created_1"))
        self.comboBox_time_created_1.addItem(_fromUtf8(""))
        self.comboBox_time_created_1.setItemText(0, _fromUtf8(""))
        self.comboBox_time_created_1.addItem(_fromUtf8(""))
        self.comboBox_time_created_1.addItem(_fromUtf8(""))
        self.comboBox_time_created_1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_time_created_1, 5, 1, 1, 1)
        self.dateTimeEdit_time_created_1 = QtGui.QDateTimeEdit(self.groupBox_search_params)
        self.dateTimeEdit_time_created_1.setCalendarPopup(True)
        self.dateTimeEdit_time_created_1.setObjectName(_fromUtf8("dateTimeEdit_time_created_1"))
        self.gridLayout.addWidget(self.dateTimeEdit_time_created_1, 5, 2, 1, 2)
        self.comboBox_time_created_2 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_time_created_2.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_time_created_2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_time_created_2.setObjectName(_fromUtf8("comboBox_time_created_2"))
        self.comboBox_time_created_2.addItem(_fromUtf8(""))
        self.comboBox_time_created_2.setItemText(0, _fromUtf8(""))
        self.comboBox_time_created_2.addItem(_fromUtf8(""))
        self.comboBox_time_created_2.addItem(_fromUtf8(""))
        self.comboBox_time_created_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_time_created_2, 5, 4, 1, 1)
        self.dateTimeEdit_time_created_2 = QtGui.QDateTimeEdit(self.groupBox_search_params)
        self.dateTimeEdit_time_created_2.setCalendarPopup(True)
        self.dateTimeEdit_time_created_2.setObjectName(_fromUtf8("dateTimeEdit_time_created_2"))
        self.gridLayout.addWidget(self.dateTimeEdit_time_created_2, 5, 5, 1, 2)
        self.label_9 = QtGui.QLabel(self.groupBox_search_params)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.comboBox_masar_id_1 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_masar_id_1.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_masar_id_1.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_masar_id_1.setObjectName(_fromUtf8("comboBox_masar_id_1"))
        self.comboBox_masar_id_1.addItem(_fromUtf8(""))
        self.comboBox_masar_id_1.setItemText(0, _fromUtf8(""))
        self.comboBox_masar_id_1.addItem(_fromUtf8(""))
        self.comboBox_masar_id_1.addItem(_fromUtf8(""))
        self.comboBox_masar_id_1.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_masar_id_1, 6, 1, 1, 1)
        self.lineEdit_masar_id_1 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_masar_id_1.setObjectName(_fromUtf8("lineEdit_masar_id_1"))
        self.gridLayout.addWidget(self.lineEdit_masar_id_1, 6, 2, 1, 2)
        self.comboBox_masar_id_2 = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_masar_id_2.setMinimumSize(QtCore.QSize(55, 0))
        self.comboBox_masar_id_2.setMaximumSize(QtCore.QSize(46, 16777215))
        self.comboBox_masar_id_2.setObjectName(_fromUtf8("comboBox_masar_id_2"))
        self.comboBox_masar_id_2.addItem(_fromUtf8(""))
        self.comboBox_masar_id_2.setItemText(0, _fromUtf8(""))
        self.comboBox_masar_id_2.addItem(_fromUtf8(""))
        self.comboBox_masar_id_2.addItem(_fromUtf8(""))
        self.comboBox_masar_id_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_masar_id_2, 6, 4, 1, 1)
        self.lineEdit_masar_id_2 = QtGui.QLineEdit(self.groupBox_search_params)
        self.lineEdit_masar_id_2.setObjectName(_fromUtf8("lineEdit_masar_id_2"))
        self.gridLayout.addWidget(self.lineEdit_masar_id_2, 6, 5, 1, 2)
        self.label_7 = QtGui.QLabel(self.groupBox_search_params)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.comboBox_synced_group_weight = QtGui.QComboBox(self.groupBox_search_params)
        self.comboBox_synced_group_weight.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_synced_group_weight.setMaximumSize(QtCore.QSize(51, 16777215))
        self.comboBox_synced_group_weight.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBox_synced_group_weight.setModelColumn(0)
        self.comboBox_synced_group_weight.setObjectName(_fromUtf8("comboBox_synced_group_weight"))
        self.comboBox_synced_group_weight.addItem(_fromUtf8(""))
        self.comboBox_synced_group_weight.addItem(_fromUtf8(""))
        self.comboBox_synced_group_weight.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_synced_group_weight, 7, 1, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(327, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 3, 1, 3)
        self.pushButton_search = QtGui.QPushButton(self.groupBox_search_params)
        self.pushButton_search.setObjectName(_fromUtf8("pushButton_search"))
        self.gridLayout.addWidget(self.pushButton_search, 7, 6, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 303, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 3, 1, 1)
        self.groupBox_search_result = QtGui.QGroupBox(self.splitter_2)
        self.groupBox_search_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_search_result.setFlat(False)
        self.groupBox_search_result.setCheckable(False)
        self.groupBox_search_result.setObjectName(_fromUtf8("groupBox_search_result"))
        self.groupBox_selected_conf = QtGui.QGroupBox(self.splitter)
        self.groupBox_selected_conf.setObjectName(_fromUtf8("groupBox_selected_conf"))
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.comboBox_config_id_1.setCurrentIndex(1)
        self.comboBox_ref_step_size_1.setCurrentIndex(1)
        self.comboBox_ref_step_size_2.setCurrentIndex(2)
        self.comboBox_time_created_1.setCurrentIndex(2)
        self.comboBox_masar_id_1.setCurrentIndex(1)
        self.comboBox_synced_group_weight.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Import Tinker Configuration from Database", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_preferences.setText(QtGui.QApplication.translate("Dialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_search_params.setTitle(QtGui.QApplication.translate("Dialog", "Search Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Config ID", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_1.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_1.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_1.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_2.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_2.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_config_id_2.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Reference Step Size", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ref_step_size_1.setItemText(1, QtGui.QApplication.translate("Dialog", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ref_step_size_1.setItemText(2, QtGui.QApplication.translate("Dialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ref_step_size_2.setItemText(1, QtGui.QApplication.translate("Dialog", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ref_step_size_2.setItemText(2, QtGui.QApplication.translate("Dialog", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Config Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Config Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Time Created", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_1.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_1.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_1.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEdit_time_created_1.setDisplayFormat(QtGui.QApplication.translate("Dialog", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_2.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_2.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_time_created_2.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.dateTimeEdit_time_created_2.setDisplayFormat(QtGui.QApplication.translate("Dialog", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "MASAR ID", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_1.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_1.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_1.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_2.setItemText(1, QtGui.QApplication.translate("Dialog", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_2.setItemText(2, QtGui.QApplication.translate("Dialog", ">=", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_masar_id_2.setItemText(3, QtGui.QApplication.translate("Dialog", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "Synced Group Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_synced_group_weight.setItemText(0, QtGui.QApplication.translate("Dialog", "True", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_synced_group_weight.setItemText(1, QtGui.QApplication.translate("Dialog", "False", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_synced_group_weight.setItemText(2, QtGui.QApplication.translate("Dialog", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_search_result.setTitle(QtGui.QApplication.translate("Dialog", "Search Result", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_selected_conf.setTitle(QtGui.QApplication.translate("Dialog", "Selected Configuration", None, QtGui.QApplication.UnicodeUTF8))

