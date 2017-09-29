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

        # move_anim = self.create_move_anim(button)

        # move_anim.setEasingCurve(QtCore.QEasingCurve.InOutBack)

        # def start_move_anim():
        #     move_anim.start()

        # button.clicked.connect(start_move_anim)

        par_anim = self.create_parallel_animation(button)

        def start_par_anim():
            par_anim.start()

        button.clicked.connect(start_par_anim)

    def create_move_anim(self, button):
        animation = QtCore.QPropertyAnimation(button, "pos")
        animation.setDuration(1000)
        animation.setEndValue(QtCore.QPoint(button.x() + 400, button.y() + 100))
        return animation

    def create_size_change_animation(self, button):
        animation = QtCore.QPropertyAnimation(button, "size")
        animation.setDuration(1000)
        animation.setEndValue(QtCore.QSize(button.width() + 50, button.height() + 50))
        return animation

    def create_parallel_animation(self, button):
        animation_group = QtCore.QParallelAnimationGroup()
        move_anim = self.create_move_anim(button)
        size_change_anim = self.create_size_change_animation(button)
        animation_group.addAnimation(move_anim)
        animation_group.addAnimation(size_change_anim)
        return animation_group

def main():
    app = QtGui.QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
