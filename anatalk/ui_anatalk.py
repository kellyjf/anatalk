# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anatalk.ui'
#
# Created: Sat Feb  4 09:57:33 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_AnatalkWindow(object):
	def setupUi(self, AnatalkWindow):
		AnatalkWindow.setObjectName(_fromUtf8("AnatalkWindow"))
		AnatalkWindow.resize(735, 469)
		self.centralwidget = QtGui.QWidget(AnatalkWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.horiZoomSlider = QtGui.QSlider(self.centralwidget)
		self.horiZoomSlider.setMinimum(100)
		self.horiZoomSlider.setMaximum(10000)
		self.horiZoomSlider.setProperty("value", 3000)
		self.horiZoomSlider.setOrientation(QtCore.Qt.Horizontal)
		self.horiZoomSlider.setObjectName(_fromUtf8("horiZoomSlider"))
		self.horizontalLayout.addWidget(self.horiZoomSlider)
		self.label_6 = QtGui.QLabel(self.centralwidget)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.horizontalLayout.addWidget(self.label_6)
		self.fftCombo = QtGui.QComboBox(self.centralwidget)
		self.fftCombo.setObjectName(_fromUtf8("fftCombo"))
		self.fftCombo.addItem(_fromUtf8(""))
		self.fftCombo.addItem(_fromUtf8(""))
		self.fftCombo.addItem(_fromUtf8(""))
		self.fftCombo.addItem(_fromUtf8(""))
		self.fftCombo.addItem(_fromUtf8(""))
		self.fftCombo.addItem(_fromUtf8(""))
		self.horizontalLayout.addWidget(self.fftCombo)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
		self.vertZoomSlider = QtGui.QSlider(self.centralwidget)
		self.vertZoomSlider.setOrientation(QtCore.Qt.Vertical)
		self.vertZoomSlider.setObjectName(_fromUtf8("vertZoomSlider"))
		self.horizontalLayout_2.addWidget(self.vertZoomSlider)
		self.mainPlot = PlotWidget(self.centralwidget)
		self.mainPlot.setObjectName(_fromUtf8("mainPlot"))
		self.horizontalLayout_2.addWidget(self.mainPlot)
		self.verticalLayout.addLayout(self.horizontalLayout_2)
		AnatalkWindow.setCentralWidget(self.centralwidget)
		self.statusbar = QtGui.QStatusBar(AnatalkWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		AnatalkWindow.setStatusBar(self.statusbar)
		self.menuBar = QtGui.QMenuBar(AnatalkWindow)
		self.menuBar.setGeometry(QtCore.QRect(0, 0, 735, 27))
		self.menuBar.setObjectName(_fromUtf8("menuBar"))
		self.menu_File = QtGui.QMenu(self.menuBar)
		self.menu_File.setObjectName(_fromUtf8("menu_File"))
		self.menuSystem = QtGui.QMenu(self.menuBar)
		self.menuSystem.setObjectName(_fromUtf8("menuSystem"))
		self.menu_Audio = QtGui.QMenu(self.menuBar)
		self.menu_Audio.setObjectName(_fromUtf8("menu_Audio"))
		AnatalkWindow.setMenuBar(self.menuBar)
		self.toolBar = QtGui.QToolBar(AnatalkWindow)
		self.toolBar.setObjectName(_fromUtf8("toolBar"))
		AnatalkWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
		self.action_Open = QtGui.QAction(AnatalkWindow)
		self.action_Open.setObjectName(_fromUtf8("action_Open"))
		self.action_Quit = QtGui.QAction(AnatalkWindow)
		self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
		self.action_Play = QtGui.QAction(AnatalkWindow)
		self.action_Play.setObjectName(_fromUtf8("action_Play"))
		self.action_Stop = QtGui.QAction(AnatalkWindow)
		self.action_Stop.setObjectName(_fromUtf8("action_Stop"))
		self.action_Record = QtGui.QAction(AnatalkWindow)
		self.action_Record.setObjectName(_fromUtf8("action_Record"))
		self.action_Halt = QtGui.QAction(AnatalkWindow)
		self.action_Halt.setObjectName(_fromUtf8("action_Halt"))
		self.action_Reboot = QtGui.QAction(AnatalkWindow)
		self.action_Reboot.setObjectName(_fromUtf8("action_Reboot"))
		self.action_Save_As = QtGui.QAction(AnatalkWindow)
		self.action_Save_As.setObjectName(_fromUtf8("action_Save_As"))
		self.action_Format = QtGui.QAction(AnatalkWindow)
		self.action_Format.setObjectName(_fromUtf8("action_Format"))
		self.menu_File.addAction(self.action_Open)
		self.menu_File.addAction(self.action_Save_As)
		self.menu_File.addSeparator()
		self.menu_File.addAction(self.action_Quit)
		self.menuSystem.addAction(self.action_Halt)
		self.menuSystem.addAction(self.action_Reboot)
		self.menu_Audio.addAction(self.action_Format)
		self.menu_Audio.addSeparator()
		self.menu_Audio.addAction(self.action_Play)
		self.menu_Audio.addAction(self.action_Record)
		self.menu_Audio.addSeparator()
		self.menu_Audio.addAction(self.action_Stop)
		self.menuBar.addAction(self.menu_File.menuAction())
		self.menuBar.addAction(self.menu_Audio.menuAction())
		self.menuBar.addAction(self.menuSystem.menuAction())
		self.toolBar.addAction(self.action_Record)
		self.toolBar.addAction(self.action_Stop)
		self.toolBar.addAction(self.action_Play)
		self.toolBar.addAction(self.action_Halt)

		self.retranslateUi(AnatalkWindow)
		QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("activated()")), AnatalkWindow.close)
		QtCore.QMetaObject.connectSlotsByName(AnatalkWindow)

	def retranslateUi(self, AnatalkWindow):
		AnatalkWindow.setWindowTitle(_translate("AnatalkWindow", "Anatalk", None))
		self.label_6.setText(_translate("AnatalkWindow", "FFT", None))
		self.fftCombo.setItemText(0, _translate("AnatalkWindow", "512", None))
		self.fftCombo.setItemText(1, _translate("AnatalkWindow", "1024", None))
		self.fftCombo.setItemText(2, _translate("AnatalkWindow", "2048", None))
		self.fftCombo.setItemText(3, _translate("AnatalkWindow", "4096", None))
		self.fftCombo.setItemText(4, _translate("AnatalkWindow", "8192", None))
		self.fftCombo.setItemText(5, _translate("AnatalkWindow", "16384", None))
		self.menu_File.setTitle(_translate("AnatalkWindow", "&File", None))
		self.menuSystem.setTitle(_translate("AnatalkWindow", "System", None))
		self.menu_Audio.setTitle(_translate("AnatalkWindow", "&Audio", None))
		self.toolBar.setWindowTitle(_translate("AnatalkWindow", "toolBar", None))
		self.action_Open.setText(_translate("AnatalkWindow", "&Open", None))
		self.action_Quit.setText(_translate("AnatalkWindow", "&Quit", None))
		self.action_Play.setText(_translate("AnatalkWindow", "&Play", None))
		self.action_Play.setShortcut(_translate("AnatalkWindow", "Alt+P", None))
		self.action_Stop.setText(_translate("AnatalkWindow", "&Stop", None))
		self.action_Stop.setShortcut(_translate("AnatalkWindow", "Alt+S", None))
		self.action_Record.setText(_translate("AnatalkWindow", "&Record", None))
		self.action_Record.setShortcut(_translate("AnatalkWindow", "Alt+R", None))
		self.action_Halt.setText(_translate("AnatalkWindow", "&Halt", None))
		self.action_Reboot.setText(_translate("AnatalkWindow", "&Reboot", None))
		self.action_Save_As.setText(_translate("AnatalkWindow", "&Save As...", None))
		self.action_Format.setText(_translate("AnatalkWindow", "&Format", None))
		self.action_Format.setShortcut(_translate("AnatalkWindow", "Alt+F", None))

from pyqtgraph import PlotWidget
