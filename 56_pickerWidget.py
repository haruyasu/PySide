import os, sys
from PySide.QtCore import *
from PySide.QtGui import *

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget ALL")
        self.resize(600, 600)
        wrapper = QWidget()
        self.setCentralWidget(wrapper)
        mainLayout = QVBoxLayout()
        wrapper.setLayout(mainLayout)

        secondHorizontalArea = QHBoxLayout()
        secondHorizontalArea.setSpacing(20)
        mainLayout.addLayout(secondHorizontalArea)

        lineEdit = QLineEdit()
        lineEdit.setMaximumWidth(200)
        lineEdit.setText("This widget is useful for inputting text")
        secondHorizontalArea.addWidget(lineEdit)

        comboBox = QComboBox()
        comboBox.addItems(["AA", "BB", "CC"])
        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QComboBox.NoInsert)
        comboBox.completer().setCompletionMode(QCompleter.PopupCompletion)
        secondHorizontalArea.addWidget(comboBox)

        spinBox = QSpinBox()
        spinBox.setMinimum(0)
        spinBox.setMaximum(10)
        spinBox.setSuffix("min")
        secondHorizontalArea.addWidget(spinBox)

        mainLayout.addWidget(self.makeHorizontalLine())

    def makeHorizontalLine(self):
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        return hline
        
def main():
    app = QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
