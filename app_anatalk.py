# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_anatalk.ui'
#
# Created: Sat Jan 28 11:28:22 2017
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_anatalk import Ui_AnatalkWindow
from pyqtgraph import PlotWidget

import alsaaudio as aa
import wave
import numpy
import sys
import signal
import struct
import time
import collections

class PlayThread(QThread):
	def __init__(self, parent=None):
		super(PlayThread,self).__init__(parent)
		print "PlayThread",parent
		self.parent=parent

	def run(self):
		channels=self.parent.channels
		framerate=self.parent.framerate
		magic=self.parent.magic
		sampwidth=self.parent.sampwidth
		fs=numpy.fft.fftfreq(magic)
		fs1=framerate*fs[0:magic/2]

		if self.parent.filename:
			self.parent.pcm.setchannels(channels)
			self.parent.pcm.setrate(framerate)

                        if sampwidth==1:
                            format=aa.PCM_FORMAT_U8
                            fmtcode="B"
                        else:
                            format=aa.PCM_FORMAT_S16_LE
                            fmtcode="h"

			self.parent.pcm.setformat(format)
			self.parent.pcm.setperiodsize(channels*magic)
			
			data=self.parent.wave.readframes(magic)
                        start=time.time()
                        fcnt=0
			while data:
				self.parent.pcm.write(data)
                                fcnt=fcnt+magic
                                delta=time.time()-start
				data=self.parent.wave.readframes(magic)
				self.parent.deque.append(abs(numpy.fft.rfft([struct.unpack(fmtcode,data[i:i+sampwidth])[0] for i in range(0,sampwidth*channels*magic,sampwidth*channels)])))
				self.emit(SIGNAL("update()"))
			#	QThread.yieldCurrentThread()
                                if fcnt>delta*framerate: 
                                    time.sleep(magic/framerate)
		
		print "Done", self.parent.filename

class AnatalkWindow(Ui_AnatalkWindow,QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.viewBox=self.mainPlot.getViewBox()
		self.viewBox.setRange(xRange=[0,8000],yRange=[0,2000000])
		self.pcm=aa.PCM(aa.PCM_PLAYBACK)
		self.deque=collections.deque()


		self.action_Open.connect(self.action_Quit, SIGNAL("triggered()"), self.close)
		self.action_Open.connect(self.action_Open, SIGNAL("triggered()"), self.pickfile)
		self.action_Play.connect(self.action_Play, SIGNAL("triggered()"), self.play)
		self.action_Play.connect(self.action_Stop, SIGNAL("triggered()"), self.stopplay)

	def pickfile(self):
		self.filename=QFileDialog.getOpenFileName(self, "Select a .wav file",filter="Sound files (*.wav)")
		self.openfile(self.filename)

	def openfile(self,filename):
		self.filename=filename
		if self.filename:
			self.wave=wave.open(str(self.filename),"r")
			self.channels=self.wave.getnchannels()
			self.framerate=self.wave.getframerate()
			self.sampwidth=self.wave.getsampwidth()
			self.statusbar.showMessage("%s (%d,%d,%d)"%(self.filename,self.framerate,self.channels,self.sampwidth))
			self.magic=8192
			fs=numpy.fft.fftfreq(self.magic)
			self.fs1=self.framerate*fs[0:self.magic/2]

	def plot(self):
		ff=self.deque.popleft()
		self.mainPlot.clear()
		self.mainPlot.plot(self.fs1,ff[0:self.magic/2])
		
	def play(self):
		print "play()"
		self.playThread = PlayThread(self)
		self.playThread.connect(self.playThread, SIGNAL("update()"),self.plot)
		self.playThread.start()

	def stopplay(self):
		self.playThread.terminate()

		

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	main = AnatalkWindow()
	if len(sys.argv)>1:
		main.openfile(sys.argv[1])
	main.show()
	sys.exit(app.exec_())

