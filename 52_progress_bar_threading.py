from PySide import QtCore, QtGui
import sys
import time

class Example(QtGui.QDialog):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("Dialog")
        self.resize(400, 133)

        self.progressBar = QtGui.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 360, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.minimum = 1
        self.progressBar.maximum = 100

        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 330, 30))
        self.pushButton.setObjectName("pushButton")

        self.worker = Worker()
        self.worker.updateProgress.connect(self.setProgress)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setValue(0)
        self.pushButton.clicked.connect(self.worker.start)

    def setProgress(self, progress):
        self.progressBar.setValue(progress)

class Worker(QtCore.QThread):
    updateProgress = QtCore.Signal(int)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        for i in range(1, 101):
            self.updateProgress.emit(i)
            time.sleep(0.1)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
