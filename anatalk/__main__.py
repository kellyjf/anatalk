
from anatalk import *
import signal
import sys
from PyQt4.QtGui import QApplication


def main():
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	main = AnatalkWindow()
	if len(sys.argv)>1:
		main.openfile(sys.argv[1])
	main.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
