# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anatalk.ui'
#
# Created: Sat Jan 28 11:28:22 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_format import Ui_AudioFormat

import sys
import signal

class AudioFormat(Ui_AudioFormat,QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self,parent)
		self.setupUi(self)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	main = AudioFormat()
	main.show()
	sys.exit(app.exec_())

