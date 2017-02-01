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

class Audio(QObject):
	def __init__(self, parent=None):
		super(Audio,self).__init__()
		self.parent=parent

	def capture(self):
		QThread.setTerminationEnabled(True)
		channels=self.parent.channels
		framerate=self.parent.framerate
		magic=self.parent.magic
		sampwidth=self.parent.sampwidth
		norm=magic**(-0.5)
		
		fs=numpy.fft.fftfreq(magic)
		fs1=framerate*fs[0:magic/2]

		if sampwidth==1:
		    format=aa.PCM_FORMAT_U8
		    fmtcode="B"
		else:
		    format=aa.PCM_FORMAT_S16_LE
		    fmtcode="h"


                rec=aa.PCM(aa.PCM_CAPTURE)
                rec.setchannels(channels)
                rec.setrate(framerate)
                rec.setformat(format)
                rec.setperiodsize(channels*magic)

                self.parent.pcm.setchannels(channels)
                self.parent.pcm.setrate(framerate)

                self.parent.pcm.setformat(format)
                self.parent.pcm.setperiodsize(channels*magic)
                
                size,data=rec.read()
                start=time.time()
                fcnt=0
                while True:
                        fcnt=fcnt+magic
                        delta=time.time()-start
                        size,chunk=rec.read()
                        if size>0:
                            data=data+chunk
                        if len(data)>=magic*sampwidth*channels:
                                self.parent.deque.append(abs(numpy.fft.rfft([norm*struct.unpack(fmtcode,data[i:i+sampwidth])[0] for i in range(0,sampwidth*channels*magic,sampwidth*channels)])))
                                self.emit(SIGNAL("update()"))
                                self.parent.pcm.write(data[0:magic*sampwidth*channels])
                                data=data[magic*sampwidth*channels:]
		

	def audio(self):
		QThread.setTerminationEnabled(True)
		channels=self.parent.channels
		framerate=self.parent.framerate
		magic=self.parent.magic
		sampwidth=self.parent.sampwidth
		norm=magic**(-0.5)
		
		fs=numpy.fft.fftfreq(magic)
		fs1=framerate*fs[0:magic/2]

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
			self.parent.pcm.setperiodsize(channels*magic)
			
			data=self.parent.wave.readframes(magic)
                        start=time.time()
                        fcnt=0
			while data:
				self.parent.pcm.write(data)
                                fcnt=fcnt+magic
                                delta=time.time()-start
				data=self.parent.wave.readframes(magic)
				if len(data)==magic*sampwidth*channels:
					self.parent.deque.append(abs(numpy.fft.rfft([norm*struct.unpack(fmtcode,data[i:i+sampwidth])[0] for i in range(0,sampwidth*channels*magic,sampwidth*channels)])))
					self.emit(SIGNAL("update()"))
                                if (fcnt-magic)>delta*framerate: 
                                    print delta, fcnt,delta*framerate,"Sleep ",magic,framerate,float(magic)/framerate
                                    time.sleep(float(magic)/framerate)
		
		print "Done", self.parent.filename

class AnatalkWindow(Ui_AnatalkWindow,QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.viewBox=self.mainPlot.getViewBox()
		self.viewBox.setRange(xRange=[0,3000],yRange=[0,35000])
		self.pcm=aa.PCM(aa.PCM_PLAYBACK)
		self.deque=collections.deque()
		self.opendlg=QFileDialog()
		self.opendlg.setFilter("Sound files (*.wav)")

                self.framerate=8000
                self.sampwidth=1
		self.magic=int(self.windowCombo.currentText())

		self.windowCombo.connect(self.windowCombo, SIGNAL("currentIndexChanged(int)"), self.setwindow)
		self.zoomSlider.connect(self.zoomSlider, SIGNAL("valueChanged(int)"), self.zoom)
		self.action_Quit.connect(self.action_Quit, SIGNAL("triggered()"), self.close)
		self.action_Open.connect(self.action_Open, SIGNAL("triggered()"), self.pickfile)
		self.action_Play.connect(self.action_Play, SIGNAL("triggered()"), self.record)
		self.action_Stop.connect(self.action_Stop, SIGNAL("triggered()"), self.stopplay)

	def zoom(self, maxval):
		self.viewBox.setRange(xRange=[0,maxval])

	def pickfile(self):
		self.opendlg.show()
		self.opendlg.exec_()
		if self.opendlg.result()==1:
			filename=str(self.opendlg.selectedFiles()[0])
			self.openfile(filename)

	def setfreqs(self):
		self.fs1=self.framerate*self.fs[0:self.magic/2]

	def setwindow(self, val=None):
		self.magic=int(self.windowCombo.currentText())
		self.fs=numpy.fft.fftfreq(self.magic)
		self.setfreqs()
		self.viewBox.setRange(yRange=[0,256**self.sampwidth])

	def openfile(self,filename):
		self.filename=filename
		if self.filename:
			self.wave=wave.open(str(self.filename),"r")
			self.channels=self.wave.getnchannels()
			self.framerate=self.wave.getframerate()
			self.sampwidth=self.wave.getsampwidth()
			self.statusbar.showMessage("%s (%d,%d,%d)"%(self.filename,self.framerate,self.channels,self.sampwidth))
			self.setwindow()
			self.play()

	def plot(self):
		ff=self.deque.popleft()
		self.mainPlot.clear()
		self.mainPlot.plot(self.fs1,ff[0:self.magic/2])
		
	def play(self):
		self.audio=Audio(self)
		self.audioThread=QThread()
		self.audio.moveToThread(self.audioThread)
		self.audioThread.connect(self.audio, SIGNAL("update()"), self.plot)
		self.audioThread.connect(self.audioThread, SIGNAL("started()"), self.audio.audio)
		self.audioThread.start()

	def record(self):
                self.channels=1
                self.framerate=16000
                self.sampwidth=2
                self.statusbar.showMessage("Recording (%d,%d,%d)"%(self.framerate,self.channels,self.sampwidth))
                self.setwindow()
		self.audio=Audio(self)
		self.audioThread=QThread()
		self.audio.moveToThread(self.audioThread)
		self.audioThread.connect(self.audio, SIGNAL("update()"), self.plot)
		self.audioThread.connect(self.audioThread, SIGNAL("started()"), self.audio.capture)
		self.audioThread.start()

	def stopplay(self):
		print self.audioThread.isRunning()
		if self.audioThread.isRunning():
			self.audioThread.terminate()

		print self.audioThread.isRunning()
		

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	main = AnatalkWindow()
	if len(sys.argv)>1:
		main.openfile(sys.argv[1])
	main.show()
	sys.exit(app.exec_())

