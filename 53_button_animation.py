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

        move_anim = self.create_move_anim(button)

        def start_move_anim():
            move_anim.start()

        button.clicked.connect(start_move_anim)

    def create_move_anim(self, button):
        animation = QtCore.QPropertyAnimation(button, "pos")
        animation.setDuration(1000)
        animation.setEndValue(QtCore.QPoint(button.x() + 400, button.y()))
        return animation

def main():
    app = QtGui.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
