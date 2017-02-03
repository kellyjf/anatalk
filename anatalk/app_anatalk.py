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
from app_format import AudioFormat
from pyqtgraph import PlotWidget

import alsaaudio as aa
import wave
import numpy
import sys
import signal
import struct
import time
import collections

class Audio(QObject):
	def __init__(self, parent=None):
		super(Audio,self).__init__()
		self.parent=parent

	def capture(self):
		QThread.setTerminationEnabled(True)

		format=str(self.parent.fmtdlg.recEncCombo.currentText())
		rate=int(self.parent.fmtdlg.recRateCombo.currentText())
		fftwin=int(self.parent.fftCombo.currentText())
		channels=1

		norm=fftwin**(-1)
		
		if format=="U8":
			sampwidth=1
			format=aa.PCM_FORMAT_U8
			fmtcode="B"
		else:
			sampwidth=2
			format=aa.PCM_FORMAT_S16_LE
			fmtcode="h"


		rec=aa.PCM(aa.PCM_CAPTURE)
		rec.setchannels(channels)
		rec.setrate(rate)
		rec.setformat(format)
		rec.setperiodsize(channels*fftwin)

		self.parent.pcm.setchannels(channels)
		self.parent.pcm.setrate(rate)

		self.parent.pcm.setformat(format)
		self.parent.pcm.setperiodsize(channels*fftwin)
		
		size,data=rec.read()
		start=time.time()
		fcnt=0
		while True:
			fcnt=fcnt+fftwin
			delta=time.time()-start
			size,chunk=rec.read()
			if size>0:
			    data=data+chunk
			if len(data)>=fftwin*sampwidth*channels:
				self.parent.deque.append(abs(numpy.fft.rfft([norm*struct.unpack(fmtcode,data[i:i+sampwidth])[0] for i in range(0,sampwidth*channels*fftwin,sampwidth*channels)])))
				self.emit(SIGNAL("update()"))
				self.parent.pcm.write(data[0:fftwin*sampwidth*channels])
				data=data[fftwin*sampwidth*channels:]
		

	def playback(self):
		QThread.setTerminationEnabled(True)
		channels=self.parent.channels
		framerate=self.parent.framerate
		fftwin=self.parent.fftwin
		sampwidth=self.parent.sampwidth
		norm=fftwin**(-0.5)
		norm=fftwin**(-1)
		
		if sampwidth==1:
		    format=aa.PCM_FORMAT_U8
		    fmtcode="B"
		else:
		    format=aa.PCM_FORMAT_S16_LE
		    fmtcode="h"


		if self.parent.filename:
			self.parent.pcm.setchannels(channels)
			self.parent.pcm.setrate(framerate)

			self.parent.pcm.setformat(format)
			self.parent.pcm.setperiodsize(channels*fftwin)
			
			data=self.parent.wave.readframes(fftwin)
                        start=time.time()
                        fcnt=0
			while data:
				self.parent.pcm.write(data)
                                fcnt=fcnt+fftwin
                                delta=time.time()-start
				data=self.parent.wave.readframes(fftwin)
				if len(data)==fftwin*sampwidth*channels:
					self.parent.deque.append(abs(numpy.fft.rfft([norm*struct.unpack(fmtcode,data[i:i+sampwidth])[0] for i in range(0,sampwidth*channels*fftwin,sampwidth*channels)])))
					self.emit(SIGNAL("update()"))
                                if (fcnt-fftwin)>delta*framerate: 
                                    #print delta, fcnt,delta*framerate,"Sleep ",fftwin,framerate,float(fftwin)/framerate
                                    time.sleep(float(fftwin)/framerate)
		
		print "Done", self.parent.filename

class AnatalkWindow(Ui_AnatalkWindow,QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.viewBox=self.mainPlot.getViewBox()
		self.viewBox.setRange(xRange=[0,3000],yRange=[0,35000])
		self.pcm=aa.PCM(aa.PCM_PLAYBACK)
		self.deque=collections.deque()
		self.opendlg=QFileDialog(self)
		self.opendlg.setFilter("Sound files (*.wav)")
		self.opendlg.resize(480, 300)

		self.fmtdlg=AudioFormat(self)
                self.fmtdlg.playEncCombo.setCurrentIndex(self.fmtdlg.playEncCombo.findText("S16_LE"))
                self.fmtdlg.playRateCombo.setCurrentIndex(self.fmtdlg.playRateCombo.findText("44100"))
                self.fmtdlg.recEncCombo.setCurrentIndex(self.fmtdlg.recEncCombo.findText("S16_LE"))
                self.fmtdlg.recRateCombo.setCurrentIndex(self.fmtdlg.recRateCombo.findText("16000"))

		self.vertZoomSlider.connect(self.vertZoomSlider, SIGNAL("valueChanged(int)"), self.vzoom)
		self.horiZoomSlider.connect(self.horiZoomSlider, SIGNAL("valueChanged(int)"), self.hzoom)

		self.action_Quit.connect(self.action_Quit, SIGNAL("triggered()"), self.close)
		self.action_Open.connect(self.action_Open, SIGNAL("triggered()"), self.pickfile)
		self.action_Play.connect(self.action_Play, SIGNAL("triggered()"), self.play)
		self.action_Record.connect(self.action_Record, SIGNAL("triggered()"), self.record)
		self.action_Stop.connect(self.action_Stop, SIGNAL("triggered()"), self.stopplay)
		self.action_Halt.connect(self.action_Halt, SIGNAL("triggered()"), self.halt)
		self.action_Reboot.connect(self.action_Halt, SIGNAL("triggered()"), self.reboot)
		self.action_Format.connect(self.action_Format, SIGNAL("triggered()"), self.fmtdlg.show)

	def halt(self):
		os.system("halt")

	def reboot(self):
		os.system("halt")

	def hzoom(self, maxval):
		self.viewBox.setRange(xRange=[0,maxval])

	def vzoom(self, maxval):
		self.viewBox.setRange(yRange=[0,maxval])

	def pickfile(self):
		self.opendlg.show()
		self.opendlg.exec_()
		if self.opendlg.result()==1:
			filename=str(self.opendlg.selectedFiles()[0])
			self.openfile(filename)


	def setfreqs(self,rate):
		self.fftwin=int(self.fftCombo.currentText())
		fs=numpy.fft.fftfreq(self.fftwin)
		self.fs1=rate*fs[0:self.fftwin/2]

	def openfile(self,filename):
		self.filename=filename
		if self.filename:
			self.wave=wave.open(str(self.filename),"r")
			self.channels=self.wave.getnchannels()
			self.framerate=self.wave.getframerate()
			self.sampwidth=self.wave.getsampwidth()
			self.statusbar.showMessage("%s (%d,%d,%d)"%(self.filename,self.framerate,self.channels,self.sampwidth))
			if self.fmtdlg.playSetCheck.checkState():
				self.fmtdlg.playRateCombo.setCurrentIndex(self.fmtdlg.playRateCombo.findText(str(self.framerate)))
				if self.sampwidth==1:
					self.fmtdlg.playEncCombo.setCurrentIndex(self.fmtdlg.playEncCombo.findText("U8"))
				else:
					self.fmtdlg.playEncCombo.setCurrentIndex(self.fmtdlg.playEncCombo.findText("S16_LE"))
			else:
				self.framerate=int(self.fmtdlg.playRateCombo.currentText())

			self.setfreqs(self.framerate)

	def plot(self):
		ff=self.deque.popleft()
		self.mainPlot.clear()
		self.mainPlot.plot(self.fs1,ff[0:self.fftwin/2])
		
	def play(self):
		self.vertZoomSlider.setMaximum(5000)
		self.vertZoomSlider.setValue(2000)
		self.horiZoomSlider.setMaximum(22050)
		self.horiZoomSlider.setValue(22050)

                self.fftCombo.setCurrentIndex(self.fftCombo.findText("4096"))
		rate=int(self.fmtdlg.playRateCombo.currentText())
		self.setfreqs(rate)

		self.audio=Audio(self)
		self.audioThread=QThread()
		self.audio.moveToThread(self.audioThread)
		self.audioThread.connect(self.audio, SIGNAL("update()"), self.plot)
		self.audioThread.connect(self.audioThread, SIGNAL("started()"), self.audio.playback)
		self.audioThread.start()

	def record(self):
		self.vertZoomSlider.setMaximum(2000)
		self.vertZoomSlider.setValue(500)
		self.horiZoomSlider.setMaximum(8000)
		self.horiZoomSlider.setValue(8000)

                self.fftCombo.setCurrentIndex(self.fftCombo.findText("1024"))
                self.fmtdlg.recEncCombo.setCurrentIndex(self.fmtdlg.recEncCombo.findText("S16_LE"))
                self.fmtdlg.recRateCombo.setCurrentIndex(self.fmtdlg.recRateCombo.findText("16000"))

		self.fftwin=int(self.fftCombo.currentText())
		rate=int(self.fmtdlg.recRateCombo.currentText())
		self.setfreqs(rate,self.fftwin)

		self.audio=Audio(self)
		self.audioThread=QThread()
		self.audio.moveToThread(self.audioThread)
		self.audioThread.connect(self.audio, SIGNAL("update()"), self.plot)
		self.audioThread.connect(self.audioThread, SIGNAL("started()"), self.audio.capture)
		self.audioThread.start()

	def stopplay(self):
		if self.audioThread.isRunning():
			self.audioThread.terminate()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	main = AnatalkWindow()
	if len(sys.argv)>1:
		main.openfile(sys.argv[1])
	main.show()
	sys.exit(app.exec_())

