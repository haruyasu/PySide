import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("img/beach.jpg")
        pixmap = pixmap.scaled(700, 700, QtCore.Qt.KeepAspectRatio)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)

        #lbl.setScaledContents(True)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Img Test')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()