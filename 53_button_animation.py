import sys
from PySide import QtCore
from PySide import QtGui

class GUI(QtGui.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Animation")
        self.resize(600, 400)
        button = QtGui.QPushButton("Animation Button", self)
        button.setGeometry(QtCore.QRect(0, 100, 100, 50))

        # ----- just move
        # move_anim = self.create_move_anim(button)
        # move_anim.setEasingCurve(QtCore.QEasingCurve.InOutBack)
        # def start_move_anim():
        #     move_anim.start()
        # button.clicked.connect(start_move_anim)
        # -----

        # ----- move and size prallel
        # par_anim = self.create_parallel_animation(button)
        # def start_par_anim():
        #     par_anim.start()
        # button.clicked.connect(start_par_anim)
        # -----

        # ----- move and size sequential
        seq_anim = self.create_sequential_animation(button)
        def start_seq_anim():
            seq_anim.start()
        button.clicked.connect(start_seq_anim)
        # -----

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

    def create_sequential_animation(self, button):
        animation_group = QtCore.QSequentialAnimationGroup()
        move_anim = self.create_move_anim(button)
        size_change_anim = self.create_size_change_animation(button)
        animation_group.addAnimation(move_anim)
        animation_group.addPause(500)
        animation_group.addAnimation(size_change_anim)
        return animation_group

def main():
    app = QtGui.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
