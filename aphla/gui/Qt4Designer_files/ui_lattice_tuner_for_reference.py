# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_lattice_tuner_for_reference.ui'
#
# Created: Thu Dec  6 15:25:07 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1015, 766)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtGui.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuLoad = QtGui.QMenu(self.menuFile)
        self.menuLoad.setObjectName("menuLoad")
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_example = QtGui.QDockWidget(MainWindow)
        self.dockWidget_example.setObjectName("dockWidget_example")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtGui.QSplitter(self.dockWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.stackedWidget = QtGui.QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_tree = QtGui.QWidget()
        self.page_tree.setObjectName("page_tree")
        self.gridLayout = QtGui.QGridLayout(self.page_tree)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtGui.QTreeView(self.page_tree)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_tree)
        self.page_table = QtGui.QWidget()
        self.page_table.setObjectName("page_table")
        self.gridLayout_2 = QtGui.QGridLayout(self.page_table)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtGui.QTableView(self.page_table)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_table)
        self.tabWidget_mode = QtGui.QTabWidget(self.splitter)
        self.tabWidget_mode.setObjectName("tabWidget_mode")
        self.tab_step_mode = QtGui.QWidget()
        self.tab_step_mode.setObjectName("tab_step_mode")
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_step_mode)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_tab_step_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_step_2.setObjectName("horizontalLayout_tab_step_2")
        self.pushButton_step_up = QtGui.QPushButton(self.tab_step_mode)
        self.pushButton_step_up.setObjectName("pushButton_step_up")
        self.horizontalLayout_tab_step_2.addWidget(self.pushButton_step_up)
        self.pushButton_step_down = QtGui.QPushButton(self.tab_step_mode)
        self.pushButton_step_down.setObjectName("pushButton_step_down")
        self.horizontalLayout_tab_step_2.addWidget(self.pushButton_step_down)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_tab_step_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_tab_step_2)
        self.horizontalLayout_tab_step_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_step_1.setObjectName("horizontalLayout_tab_step_1")
        self.pushButton_update = QtGui.QPushButton(self.tab_step_mode)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_tab_step_1.addWidget(self.pushButton_update)
        self.checkBox_auto = QtGui.QCheckBox(self.tab_step_mode)
        self.checkBox_auto.setMinimumSize(QtCore.QSize(141, 0))
        self.checkBox_auto.setObjectName("checkBox_auto")
        self.horizontalLayout_tab_step_1.addWidget(self.checkBox_auto)
        self.lineEdit_auto_update_interval = QtGui.QLineEdit(self.tab_step_mode)
        self.lineEdit_auto_update_interval.setObjectName("lineEdit_auto_update_interval")
        self.horizontalLayout_tab_step_1.addWidget(self.lineEdit_auto_update_interval)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_tab_step_1.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_tab_step_1)
        self.tabWidget_mode.addTab(self.tab_step_mode, "")
        self.tab_ramp_mode = QtGui.QWidget()
        self.tab_ramp_mode.setObjectName("tab_ramp_mode")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_ramp_mode)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_tab_ramp_1 = QtGui.QVBoxLayout()
        self.verticalLayout_tab_ramp_1.setObjectName("verticalLayout_tab_ramp_1")
        self.horizontalLayout_tab_ramp_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_ramp_2.setObjectName("horizontalLayout_tab_ramp_2")
        self.pushButton_copy = QtGui.QPushButton(self.tab_ramp_mode)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.horizontalLayout_tab_ramp_2.addWidget(self.pushButton_copy)
        self.comboBox_setpoint_copy_source = QtGui.QComboBox(self.tab_ramp_mode)
        self.comboBox_setpoint_copy_source.setObjectName("comboBox_setpoint_copy_source")
        self.comboBox_setpoint_copy_source.addItem("")
        self.comboBox_setpoint_copy_source.addItem("")
        self.comboBox_setpoint_copy_source.addItem("")
        self.horizontalLayout_tab_ramp_2.addWidget(self.comboBox_setpoint_copy_source)
        self.label_tab_ramp_3 = QtGui.QLabel(self.tab_ramp_mode)
        self.label_tab_ramp_3.setObjectName("label_tab_ramp_3")
        self.horizontalLayout_tab_ramp_2.addWidget(self.label_tab_ramp_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_tab_ramp_2.addItem(spacerItem2)
        self.verticalLayout_tab_ramp_1.addLayout(self.horizontalLayout_tab_ramp_2)
        self.horizontalLayout_tab_ramp_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_ramp_1.setObjectName("horizontalLayout_tab_ramp_1")
        self.label_tab_ramp_1 = QtGui.QLabel(self.tab_ramp_mode)
        self.label_tab_ramp_1.setObjectName("label_tab_ramp_1")
        self.horizontalLayout_tab_ramp_1.addWidget(self.label_tab_ramp_1)
        self.lineEdit_nSteps = QtGui.QLineEdit(self.tab_ramp_mode)
        self.lineEdit_nSteps.setObjectName("lineEdit_nSteps")
        self.horizontalLayout_tab_ramp_1.addWidget(self.lineEdit_nSteps)
        self.label_tab_ramp_2 = QtGui.QLabel(self.tab_ramp_mode)
        self.label_tab_ramp_2.setObjectName("label_tab_ramp_2")
        self.horizontalLayout_tab_ramp_1.addWidget(self.label_tab_ramp_2)
        self.lineEdit_wait_after_each_step = QtGui.QLineEdit(self.tab_ramp_mode)
        self.lineEdit_wait_after_each_step.setObjectName("lineEdit_wait_after_each_step")
        self.horizontalLayout_tab_ramp_1.addWidget(self.lineEdit_wait_after_each_step)
        self.verticalLayout_tab_ramp_1.addLayout(self.horizontalLayout_tab_ramp_1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_tab_ramp_1)
        self.pushButton_start = QtGui.QPushButton(self.tab_ramp_mode)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.pushButton_stop = QtGui.QPushButton(self.tab_ramp_mode)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        self.pushButton_revert = QtGui.QPushButton(self.tab_ramp_mode)
        self.pushButton_revert.setObjectName("pushButton_revert")
        self.horizontalLayout_2.addWidget(self.pushButton_revert)
        spacerItem3 = QtGui.QSpacerItem(137, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.tabWidget_mode.addTab(self.tab_ramp_mode, "")
        self.tabWidget_metadata = QtGui.QTabWidget(self.splitter)
        self.tabWidget_metadata.setObjectName("tabWidget_metadata")
        self.tab_config_metadata = QtGui.QWidget()
        self.tab_config_metadata.setObjectName("tab_config_metadata")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_config_metadata)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_tab_conf_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_conf_2.setObjectName("horizontalLayout_tab_conf_2")
        self.label_tab_conf_2 = QtGui.QLabel(self.tab_config_metadata)
        self.label_tab_conf_2.setObjectName("label_tab_conf_2")
        self.horizontalLayout_tab_conf_2.addWidget(self.label_tab_conf_2)
        self.lineEdit_config_username = QtGui.QLineEdit(self.tab_config_metadata)
        self.lineEdit_config_username.setObjectName("lineEdit_config_username")
        self.horizontalLayout_tab_conf_2.addWidget(self.lineEdit_config_username)
        self.label_tab_conf_3 = QtGui.QLabel(self.tab_config_metadata)
        self.label_tab_conf_3.setObjectName("label_tab_conf_3")
        self.horizontalLayout_tab_conf_2.addWidget(self.label_tab_conf_3)
        self.lineEdit_config_timestamp = QtGui.QLineEdit(self.tab_config_metadata)
        self.lineEdit_config_timestamp.setObjectName("lineEdit_config_timestamp")
        self.horizontalLayout_tab_conf_2.addWidget(self.lineEdit_config_timestamp)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_tab_conf_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_tab_conf_2)
        self.horizontalLayout_tab_conf_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_conf_1.setObjectName("horizontalLayout_tab_conf_1")
        self.verticalLayout_tab_conf_1 = QtGui.QVBoxLayout()
        self.verticalLayout_tab_conf_1.setObjectName("verticalLayout_tab_conf_1")
        self.label_tab_conf_1 = QtGui.QLabel(self.tab_config_metadata)
        self.label_tab_conf_1.setObjectName("label_tab_conf_1")
        self.verticalLayout_tab_conf_1.addWidget(self.label_tab_conf_1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_tab_conf_1.addItem(spacerItem5)
        self.horizontalLayout_tab_conf_1.addLayout(self.verticalLayout_tab_conf_1)
        self.textEdit_config_description = QtGui.QTextEdit(self.tab_config_metadata)
        self.textEdit_config_description.setObjectName("textEdit_config_description")
        self.horizontalLayout_tab_conf_1.addWidget(self.textEdit_config_description)
        self.verticalLayout_3.addLayout(self.horizontalLayout_tab_conf_1)
        self.tabWidget_metadata.addTab(self.tab_config_metadata, "")
        self.tab_snapshot_metadata = QtGui.QWidget()
        self.tab_snapshot_metadata.setObjectName("tab_snapshot_metadata")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_snapshot_metadata)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_tab_snap_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_snap_2.setObjectName("horizontalLayout_tab_snap_2")
        self.label_tab_snap_2 = QtGui.QLabel(self.tab_snapshot_metadata)
        self.label_tab_snap_2.setObjectName("label_tab_snap_2")
        self.horizontalLayout_tab_snap_2.addWidget(self.label_tab_snap_2)
        self.lineEdit_snapshot_username = QtGui.QLineEdit(self.tab_snapshot_metadata)
        self.lineEdit_snapshot_username.setObjectName("lineEdit_snapshot_username")
        self.horizontalLayout_tab_snap_2.addWidget(self.lineEdit_snapshot_username)
        self.label_tab_snap_3 = QtGui.QLabel(self.tab_snapshot_metadata)
        self.label_tab_snap_3.setObjectName("label_tab_snap_3")
        self.horizontalLayout_tab_snap_2.addWidget(self.label_tab_snap_3)
        self.lineEdit_snapshot_timestamp = QtGui.QLineEdit(self.tab_snapshot_metadata)
        self.lineEdit_snapshot_timestamp.setObjectName("lineEdit_snapshot_timestamp")
        self.horizontalLayout_tab_snap_2.addWidget(self.lineEdit_snapshot_timestamp)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_tab_snap_2.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_tab_snap_2)
        self.horizontalLayout_tab_snap_1 = QtGui.QHBoxLayout()
        self.horizontalLayout_tab_snap_1.setObjectName("horizontalLayout_tab_snap_1")
        self.verticalLayout_tab_snap_1 = QtGui.QVBoxLayout()
        self.verticalLayout_tab_snap_1.setObjectName("verticalLayout_tab_snap_1")
        self.label_tab_snap_1 = QtGui.QLabel(self.tab_snapshot_metadata)
        self.label_tab_snap_1.setObjectName("label_tab_snap_1")
        self.verticalLayout_tab_snap_1.addWidget(self.label_tab_snap_1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_tab_snap_1.addItem(spacerItem7)
        self.horizontalLayout_tab_snap_1.addLayout(self.verticalLayout_tab_snap_1)
        self.textEdit_snapshot_description = QtGui.QTextEdit(self.tab_snapshot_metadata)
        self.textEdit_snapshot_description.setObjectName("textEdit_snapshot_description")
        self.horizontalLayout_tab_snap_1.addWidget(self.textEdit_snapshot_description)
        self.verticalLayout_5.addLayout(self.horizontalLayout_tab_snap_1)
        self.tabWidget_metadata.addTab(self.tab_snapshot_metadata, "")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.dockWidget_example.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_example)
        self.actionNewConfig = QtGui.QAction(MainWindow)
        self.actionNewConfig.setObjectName("actionNewConfig")
        self.actionLoadConfigFileInNewTab = QtGui.QAction(MainWindow)
        self.actionLoadConfigFileInNewTab.setObjectName("actionLoadConfigFileInNewTab")
        self.actionLoadSnapshotFileInNewTab = QtGui.QAction(MainWindow)
        self.actionLoadSnapshotFileInNewTab.setObjectName("actionLoadSnapshotFileInNewTab")
        self.actionLoadConfigFileInCurrentTab = QtGui.QAction(MainWindow)
        self.actionLoadConfigFileInCurrentTab.setObjectName("actionLoadConfigFileInCurrentTab")
        self.actionLoadSnapshotFileInCurrentTab = QtGui.QAction(MainWindow)
        self.actionLoadSnapshotFileInCurrentTab.setObjectName("actionLoadSnapshotFileInCurrentTab")
        self.actionSaveConfigFile = QtGui.QAction(MainWindow)
        self.actionSaveConfigFile.setObjectName("actionSaveConfigFile")
        self.actionSaveSnapshotFile = QtGui.QAction(MainWindow)
        self.actionSaveSnapshotFile.setObjectName("actionSaveSnapshotFile")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionConfig_from_file = QtGui.QAction(MainWindow)
        self.actionConfig_from_file.setObjectName("actionConfig_from_file")
        self.actionSnapshot_from_file = QtGui.QAction(MainWindow)
        self.actionSnapshot_from_file.setObjectName("actionSnapshot_from_file")
        self.actionGrouped = QtGui.QAction(MainWindow)
        self.actionGrouped.setObjectName("actionGrouped")
        self.actionUngrouped = QtGui.QAction(MainWindow)
        self.actionUngrouped.setObjectName("actionUngrouped")
        self.actionConfig_Metadata = QtGui.QAction(MainWindow)
        self.actionConfig_Metadata.setObjectName("actionConfig_Metadata")
        self.actionSnapshot_Metadata = QtGui.QAction(MainWindow)
        self.actionSnapshot_Metadata.setObjectName("actionSnapshot_Metadata")
        self.actionDefault_config_columns = QtGui.QAction(MainWindow)
        self.actionDefault_config_columns.setObjectName("actionDefault_config_columns")
        self.actionDefault_snapshot_columns = QtGui.QAction(MainWindow)
        self.actionDefault_snapshot_columns.setObjectName("actionDefault_snapshot_columns")
        self.actionUser_defined_config_columns = QtGui.QAction(MainWindow)
        self.actionUser_defined_config_columns.setObjectName("actionUser_defined_config_columns")
        self.actionUser_defined_snapshot_columns = QtGui.QAction(MainWindow)
        self.actionUser_defined_snapshot_columns.setObjectName("actionUser_defined_snapshot_columns")
        self.menuSave.addAction(self.actionSaveConfigFile)
        self.menuSave.addAction(self.actionSaveSnapshotFile)
        self.menuLoad.addAction(self.actionConfig_from_file)
        self.menuLoad.addAction(self.actionSnapshot_from_file)
        self.menuFile.addAction(self.actionNewConfig)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuLoad.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menu_View.addAction(self.actionGrouped)
        self.menu_View.addAction(self.actionUngrouped)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionConfig_Metadata)
        self.menu_View.addAction(self.actionSnapshot_Metadata)
        self.menu_View.addSeparator()
        self.menu_View.addAction(self.actionDefault_config_columns)
        self.menu_View.addAction(self.actionDefault_snapshot_columns)
        self.menu_View.addAction(self.actionUser_defined_config_columns)
        self.menu_View.addAction(self.actionUser_defined_snapshot_columns)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_mode.setCurrentIndex(1)
        self.tabWidget_metadata.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Lattice Tuner", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSave.setTitle(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLoad.setTitle(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_View.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_step_up.setText(QtGui.QApplication.translate("MainWindow", "Up", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_step_down.setText(QtGui.QApplication.translate("MainWindow", "Down", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_update.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_auto.setText(QtGui.QApplication.translate("MainWindow", "Auto: Interval [s]", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_mode.setTabText(self.tabWidget_mode.indexOf(self.tab_step_mode), QtGui.QApplication.translate("MainWindow", "Step Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_copy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_setpoint_copy_source.setItemText(0, QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_setpoint_copy_source.setItemText(1, QtGui.QApplication.translate("MainWindow", "Initial", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_setpoint_copy_source.setItemText(2, QtGui.QApplication.translate("MainWindow", "Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_ramp_3.setText(QtGui.QApplication.translate("MainWindow", "setpoints into target setpoints", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_ramp_1.setText(QtGui.QApplication.translate("MainWindow", "Number of Steps:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_ramp_2.setText(QtGui.QApplication.translate("MainWindow", "Wait after Each Step [s]:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_revert.setText(QtGui.QApplication.translate("MainWindow", "Revert", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_mode.setTabText(self.tabWidget_mode.indexOf(self.tab_ramp_mode), QtGui.QApplication.translate("MainWindow", "Ramp Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_conf_2.setText(QtGui.QApplication.translate("MainWindow", "Created by", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_conf_3.setText(QtGui.QApplication.translate("MainWindow", "Created on", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_conf_1.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_metadata.setTabText(self.tabWidget_metadata.indexOf(self.tab_config_metadata), QtGui.QApplication.translate("MainWindow", "Config Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_snap_2.setText(QtGui.QApplication.translate("MainWindow", "Created by", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_snap_3.setText(QtGui.QApplication.translate("MainWindow", "Created on", None, QtGui.QApplication.UnicodeUTF8))
        self.label_tab_snap_1.setText(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_metadata.setTabText(self.tabWidget_metadata.indexOf(self.tab_snapshot_metadata), QtGui.QApplication.translate("MainWindow", "Snapshot Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewConfig.setText(QtGui.QApplication.translate("MainWindow", "&New Config...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewConfig.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadConfigFileInNewTab.setText(QtGui.QApplication.translate("MainWindow", "Config file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadSnapshotFileInNewTab.setText(QtGui.QApplication.translate("MainWindow", "Snapshot file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadConfigFileInCurrentTab.setText(QtGui.QApplication.translate("MainWindow", "Config file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadSnapshotFileInCurrentTab.setText(QtGui.QApplication.translate("MainWindow", "Snapshot file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveConfigFile.setText(QtGui.QApplication.translate("MainWindow", "Config to file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveSnapshotFile.setText(QtGui.QApplication.translate("MainWindow", "Snapshot to file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest.setText(QtGui.QApplication.translate("MainWindow", "Load Snapshot File...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_from_file.setText(QtGui.QApplication.translate("MainWindow", "Config from file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnapshot_from_file.setText(QtGui.QApplication.translate("MainWindow", "Snapshot from file...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGrouped.setText(QtGui.QApplication.translate("MainWindow", "&Grouped", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUngrouped.setText(QtGui.QApplication.translate("MainWindow", "&Ungrouped", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfig_Metadata.setText(QtGui.QApplication.translate("MainWindow", "Config Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnapshot_Metadata.setText(QtGui.QApplication.translate("MainWindow", "Snapshot Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefault_config_columns.setText(QtGui.QApplication.translate("MainWindow", "Default config columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDefault_snapshot_columns.setText(QtGui.QApplication.translate("MainWindow", "Default snapshot columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUser_defined_config_columns.setText(QtGui.QApplication.translate("MainWindow", "User-defined config columns", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUser_defined_snapshot_columns.setText(QtGui.QApplication.translate("MainWindow", "User-defined snapshot columns", None, QtGui.QApplication.UnicodeUTF8))
