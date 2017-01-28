# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anatalk.ui'
#
# Created: Sat Jan 28 11:59:36 2017
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
		AnatalkWindow.resize(568, 502)
		self.centralwidget = QtGui.QWidget(AnatalkWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
		self.label = QtGui.QLabel(self.centralwidget)
		self.label.setObjectName(_fromUtf8("label"))
		self.horizontalLayout.addWidget(self.label)
		self.freqLine = QtGui.QLineEdit(self.centralwidget)
		self.freqLine.setObjectName(_fromUtf8("freqLine"))
		self.horizontalLayout.addWidget(self.freqLine)
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.horizontalLayout.addWidget(self.label_2)
		self.windowCombo = QtGui.QComboBox(self.centralwidget)
		self.windowCombo.setObjectName(_fromUtf8("windowCombo"))
		self.windowCombo.addItem(_fromUtf8(""))
		self.windowCombo.addItem(_fromUtf8(""))
		self.windowCombo.addItem(_fromUtf8(""))
		self.windowCombo.addItem(_fromUtf8(""))
		self.horizontalLayout.addWidget(self.windowCombo)
		spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.mainPlot = PlotWidget(self.centralwidget)
		self.mainPlot.setObjectName(_fromUtf8("mainPlot"))
		self.verticalLayout.addWidget(self.mainPlot)
		AnatalkWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(AnatalkWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 27))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menu_File = QtGui.QMenu(self.menubar)
		self.menu_File.setObjectName(_fromUtf8("menu_File"))
		AnatalkWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(AnatalkWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		AnatalkWindow.setStatusBar(self.statusbar)
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
		self.menu_File.addAction(self.action_Open)
		self.menu_File.addSeparator()
		self.menu_File.addAction(self.action_Play)
		self.menu_File.addAction(self.action_Stop)
		self.menu_File.addSeparator()
		self.menu_File.addAction(self.action_Quit)
		self.menubar.addAction(self.menu_File.menuAction())
		self.toolBar.addAction(self.action_Quit)
		self.toolBar.addAction(self.action_Open)
		self.toolBar.addAction(self.action_Play)
		self.toolBar.addAction(self.action_Stop)
		self.label.setBuddy(self.freqLine)
		self.label_2.setBuddy(self.windowCombo)

		self.retranslateUi(AnatalkWindow)
		QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("activated()")), AnatalkWindow.close)
		QtCore.QMetaObject.connectSlotsByName(AnatalkWindow)

	def retranslateUi(self, AnatalkWindow):
		AnatalkWindow.setWindowTitle(_translate("AnatalkWindow", "Anatalk", None))
		self.label.setText(_translate("AnatalkWindow", "&Freq", None))
		self.label_2.setText(_translate("AnatalkWindow", "&Window", None))
		self.windowCombo.setItemText(0, _translate("AnatalkWindow", "10", None))
		self.windowCombo.setItemText(1, _translate("AnatalkWindow", "20", None))
		self.windowCombo.setItemText(2, _translate("AnatalkWindow", "40", None))
		self.windowCombo.setItemText(3, _translate("AnatalkWindow", "80", None))
		self.menu_File.setTitle(_translate("AnatalkWindow", "&File", None))
		self.toolBar.setWindowTitle(_translate("AnatalkWindow", "toolBar", None))
		self.action_Open.setText(_translate("AnatalkWindow", "&Open", None))
		self.action_Quit.setText(_translate("AnatalkWindow", "&Quit", None))
		self.action_Play.setText(_translate("AnatalkWindow", "&Play", None))
		self.action_Stop.setText(_translate("AnatalkWindow", "&Stop", None))

from pyqtgraph import PlotWidget
