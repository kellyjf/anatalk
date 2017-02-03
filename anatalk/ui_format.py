# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_format.ui'
#
# Created: Thu Feb  2 22:08:38 2017
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

class Ui_AudioFormat(object):
	def setupUi(self, AudioFormat):
		AudioFormat.setObjectName(_fromUtf8("AudioFormat"))
		AudioFormat.resize(484, 340)
		self.verticalLayout_2 = QtGui.QVBoxLayout(AudioFormat)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.tabWidget = QtGui.QTabWidget(AudioFormat)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.verticalLayout = QtGui.QVBoxLayout(self.tab_2)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.gridLayout_2 = QtGui.QGridLayout()
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.recRateCombo = QtGui.QComboBox(self.tab_2)
		self.recRateCombo.setObjectName(_fromUtf8("recRateCombo"))
		self.recRateCombo.addItem(_fromUtf8(""))
		self.recRateCombo.addItem(_fromUtf8(""))
		self.recRateCombo.addItem(_fromUtf8(""))
		self.recRateCombo.addItem(_fromUtf8(""))
		self.gridLayout_2.addWidget(self.recRateCombo, 2, 1, 1, 1)
		self.recEncCombo = QtGui.QComboBox(self.tab_2)
		self.recEncCombo.setObjectName(_fromUtf8("recEncCombo"))
		self.recEncCombo.addItem(_fromUtf8(""))
		self.recEncCombo.addItem(_fromUtf8(""))
		self.gridLayout_2.addWidget(self.recEncCombo, 0, 1, 1, 1)
		self.label_5 = QtGui.QLabel(self.tab_2)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
		self.label_4 = QtGui.QLabel(self.tab_2)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
		self.verticalLayout.addLayout(self.gridLayout_2)
		spacerItem = QtGui.QSpacerItem(20, 26, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout.addItem(spacerItem)
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.playbackTab = QtGui.QWidget()
		self.playbackTab.setObjectName(_fromUtf8("playbackTab"))
		self.verticalLayout_3 = QtGui.QVBoxLayout(self.playbackTab)
		self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
		self.playSetCheck = QtGui.QCheckBox(self.playbackTab)
		self.playSetCheck.setObjectName(_fromUtf8("playSetCheck"))
		self.verticalLayout_3.addWidget(self.playSetCheck)
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.playEncCombo = QtGui.QComboBox(self.playbackTab)
		self.playEncCombo.setObjectName(_fromUtf8("playEncCombo"))
		self.playEncCombo.addItem(_fromUtf8(""))
		self.playEncCombo.addItem(_fromUtf8(""))
		self.gridLayout.addWidget(self.playEncCombo, 0, 1, 1, 1)
		self.label = QtGui.QLabel(self.playbackTab)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.label_3 = QtGui.QLabel(self.playbackTab)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
		self.playRateCombo = QtGui.QComboBox(self.playbackTab)
		self.playRateCombo.setObjectName(_fromUtf8("playRateCombo"))
		self.playRateCombo.addItem(_fromUtf8(""))
		self.playRateCombo.addItem(_fromUtf8(""))
		self.playRateCombo.addItem(_fromUtf8(""))
		self.playRateCombo.addItem(_fromUtf8(""))
		self.gridLayout.addWidget(self.playRateCombo, 1, 1, 1, 1)
		self.verticalLayout_3.addLayout(self.gridLayout)
		spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		self.verticalLayout_3.addItem(spacerItem1)
		self.tabWidget.addTab(self.playbackTab, _fromUtf8(""))
		self.verticalLayout_2.addWidget(self.tabWidget)
		self.buttonBox = QtGui.QDialogButtonBox(AudioFormat)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
		self.verticalLayout_2.addWidget(self.buttonBox)

		self.retranslateUi(AudioFormat)
		self.tabWidget.setCurrentIndex(1)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AudioFormat.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AudioFormat.reject)
		QtCore.QMetaObject.connectSlotsByName(AudioFormat)

	def retranslateUi(self, AudioFormat):
		AudioFormat.setWindowTitle(_translate("AudioFormat", "Audio Format", None))
		self.recRateCombo.setItemText(0, _translate("AudioFormat", "8000", None))
		self.recRateCombo.setItemText(1, _translate("AudioFormat", "16000", None))
		self.recRateCombo.setItemText(2, _translate("AudioFormat", "32000", None))
		self.recRateCombo.setItemText(3, _translate("AudioFormat", "44100", None))
		self.recEncCombo.setItemText(0, _translate("AudioFormat", "U8", None))
		self.recEncCombo.setItemText(1, _translate("AudioFormat", "S16_LE", None))
		self.label_5.setText(_translate("AudioFormat", "Framerate", None))
		self.label_4.setText(_translate("AudioFormat", "Encoding", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AudioFormat", "Record", None))
		self.playSetCheck.setText(_translate("AudioFormat", "Use File Settings", None))
		self.playEncCombo.setItemText(0, _translate("AudioFormat", "U8", None))
		self.playEncCombo.setItemText(1, _translate("AudioFormat", "S16_LE", None))
		self.label.setText(_translate("AudioFormat", "Encoding", None))
		self.label_3.setText(_translate("AudioFormat", "Framerate", None))
		self.playRateCombo.setItemText(0, _translate("AudioFormat", "8000", None))
		self.playRateCombo.setItemText(1, _translate("AudioFormat", "16000", None))
		self.playRateCombo.setItemText(2, _translate("AudioFormat", "32000", None))
		self.playRateCombo.setItemText(3, _translate("AudioFormat", "44100", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.playbackTab), _translate("AudioFormat", "Playback", None))

