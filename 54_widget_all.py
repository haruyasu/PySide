import os, sys
from functools import partial
import time
from PySide import QtCore, QtGui

LOGO_IMAGE = os.path.dirname(__file__) + "/img/ben.png"

class GUI(QtGui.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Widget ALL")
        self.resize(600, 600)
        wrapper = QtGui.QWidget()
        self.setCentralWidget(wrapper)
        mainLayout = QtGui.QVBoxLayout()
        wrapper.setLayout(mainLayout)

        # --- first row ---
        firstHolizontalArea = QtGui.QHBoxLayout()
        firstHolizontalArea.setSpacing(20)
        mainLayout.addLayout(firstHolizontalArea)

        labelArea = QtGui.QVBoxLayout()
        firstHolizontalArea.addLayout(labelArea)

        labelWidget = QtGui.QLabel("Text is shown like this.")
        labelArea.addWidget(labelWidget)

        imageWidget = QtGui.QLabel()
        imageWidget.setPixmap(QtGui.QPixmap(LOGO_IMAGE))
        labelArea.addWidget(imageWidget)
        labelArea.addStretch()

        textArea = QtGui.QTextEdit()
        textArea.setPlainText("Text are \ncan be set\nmultiple lines and HTML")
        firstHolizontalArea.addWidget(textArea)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- second row ---
        secondHorizontalArea = QtGui.QHBoxLayout()
        secondHorizontalArea.setSpacing(20)
        mainLayout.addLayout(secondHorizontalArea)

        lineEdit = QtGui.QLineEdit()
        lineEdit.setMaximumWidth(200)
        lineEdit.setText("This widget is useful for inputting text")
        secondHorizontalArea.addWidget(lineEdit)

        comboBox = QtGui.QComboBox()
        comboBox.addItems(["AA", "BB", "CC"])
        comboBox.setEditable(True)
        comboBox.setInsertPolicy(QtGui.QComboBox.NoInsert)
        comboBox.completer().setCompletionMode(QtGui.QCompleter.PopupCompletion)
        secondHorizontalArea.addWidget(comboBox)

        spinBox = QtGui.QSpinBox()
        spinBox.setMinimum(0)
        spinBox.setMaximum(10)
        spinBox.setSuffix("min")
        secondHorizontalArea.addWidget(spinBox)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- third row ---
        thirdHorizontalArea = QtGui.QHBoxLayout()
        thirdHorizontalArea.setSpacing(20)
        mainLayout.addLayout(thirdHorizontalArea)

        checkBox = QtGui.QCheckBox("Check Box")
        thirdHorizontalArea.addWidget(checkBox)
        checkBox.setCheckable(True)

        radioArea = QtGui.QVBoxLayout()
        thirdHorizontalArea.addLayout(radioArea)

        radioGroup = QtGui.QButtonGroup(self)

        radioBtn1 = QtGui.QRadioButton("Option 1")
        radioArea.addWidget(radioBtn1)
        radioGroup.addButton(radioBtn1)

        radioBtn2 = QtGui.QRadioButton("Option 2")
        radioArea.addWidget(radioBtn2)
        radioGroup.addButton(radioBtn2)

        radioBtn3 = QtGui.QRadioButton("Option 3")
        radioArea.addWidget(radioBtn3)
        radioGroup.addButton(radioBtn3)

        radioBtn1.setChecked(True)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- fourth row ---
        fourthHorizontalArea = QtGui.QHBoxLayout()
        fourthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(fourthHorizontalArea)

        calender = QtGui.QCalendarWidget()
        fourthHorizontalArea.addWidget(calender)
        calender.setMaximumWidth(300)

        lcdNumber = QtGui.QLCDNumber()
        fourthHorizontalArea.addWidget(lcdNumber)
        lcdNumber.display(1234)

        sliderArea = QtGui.QVBoxLayout()
        fourthHorizontalArea.addLayout(sliderArea)

        sliderDisplay = QtGui.QLabel("0")
        sliderArea.addWidget(sliderDisplay)

        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        sliderArea.addWidget(slider)
        slider.setRange(0, 100)
        slider.setTickPosition(QtGui.QSlider.TicksBothSides)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickInterval(10)
        slider.valueChanged.connect(lambda val: sliderDisplay.setText(str(val)))
        slider.setValue(0)

        dialDisplay = QtGui.QLabel("0")
        sliderArea.addWidget(dialDisplay)
        dial = QtGui.QDial()
        sliderArea.addWidget(dial)
        dial.setRange(0, 100)
        dial.setSingleStep(5)
        dial.setPageStep(10)
        dial.setNotchesVisible(True)
        dial.setWrapping(True)
        dial.setNotchTarget(5)
        dial.valueChanged.connect(lambda val: dialDisplay.setText(str(val)))
        dial.setValue(0)

        mainLayout.addWidget(self.makeHorizontalLine())


    def makeHorizontalLine(self):
        hline = QtGui.QFrame()
        hline.setFrameShape(QtGui.QFrame.HLine)
        hline.setFrameShadow(QtGui.QFrame.Sunken)
        return hline

def main():
    app = QtGui.QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()