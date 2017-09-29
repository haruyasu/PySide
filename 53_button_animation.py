import sys
from PySide import QtCore
from PySide import QtGui

class GUI(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Animation")
        self.resize(600, 400)
        button = QtGui.QPushButton("Animation Button", self)
        button.setGeometry(QtCore.QRect(0, 100, 100, 50))

def main():
    app = QtGui.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
