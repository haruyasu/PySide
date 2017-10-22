import os, sys
from functools import partial
import time
from PySide.QtCore import *
from PySide.QtGui import *

LOGO_IMAGE = os.path.dirname(__file__) + "/img/ben.png"

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

        # --- first row ---
        firstHolizontalArea = QHBoxLayout()
        firstHolizontalArea.setSpacing(20)
        mainLayout.addLayout(firstHolizontalArea)

        labelArea = QVBoxLayout()
        firstHolizontalArea.addLayout(labelArea)

        labelWidget = QLabel("Text is shown like this.")
        labelArea.addWidget(labelWidget)

        imageWidget = QLabel()
        imageWidget.setPixmap(QPixmap(LOGO_IMAGE))
        labelArea.addWidget(imageWidget)
        labelArea.addStretch()

        textArea = QTextEdit()
        textArea.setPlainText("Text are \ncan be set\nmultiple lines and HTML")
        firstHolizontalArea.addWidget(textArea)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- second row ---
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

        # --- third row ---
        thirdHorizontalArea = QHBoxLayout()
        thirdHorizontalArea.setSpacing(20)
        mainLayout.addLayout(thirdHorizontalArea)

        checkBox = QCheckBox("Check Box")
        thirdHorizontalArea.addWidget(checkBox)
        checkBox.setCheckable(True)

        radioArea = QVBoxLayout()
        thirdHorizontalArea.addLayout(radioArea)

        radioGroup = QButtonGroup(self)

        radioBtn1 = QRadioButton("Option 1")
        radioArea.addWidget(radioBtn1)
        radioGroup.addButton(radioBtn1)

        radioBtn2 = QRadioButton("Option 2")
        radioArea.addWidget(radioBtn2)
        radioGroup.addButton(radioBtn2)

        radioBtn3 = QRadioButton("Option 3")
        radioArea.addWidget(radioBtn3)
        radioGroup.addButton(radioBtn3)

        radioBtn1.setChecked(True)

        mainLayout.addWidget(self.makeHorizontalLine())

        # --- fourth row ---
        fourthHorizontalArea = QHBoxLayout()
        fourthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(fourthHorizontalArea)

        calender = QCalendarWidget()
        fourthHorizontalArea.addWidget(calender)
        calender.setMaximumWidth(300)

        lcdNumber = QLCDNumber()
        fourthHorizontalArea.addWidget(lcdNumber)
        lcdNumber.display(1234)

        sliderArea = QVBoxLayout()
        fourthHorizontalArea.addLayout(sliderArea)

        sliderDisplay = QLabel("0")
        sliderArea.addWidget(sliderDisplay)

        slider = QSlider(Qt.Horizontal)
        sliderArea.addWidget(slider)
        slider.setRange(0, 100)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setSingleStep(5)
        slider.setPageStep(10)
        slider.setTickInterval(10)
        slider.valueChanged.connect(lambda val: sliderDisplay.setText(str(val)))
        slider.setValue(0)

        dialDisplay = QLabel("0")
        sliderArea.addWidget(dialDisplay)
        dial = QDial()
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

        # --- fifth row ---
        fifthHorizontalArea = QHBoxLayout()
        fifthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(fifthHorizontalArea)

        fifthHorizontalArea.addWidget(self.makeListWidget())
        fifthHorizontalArea.addWidget(self.makeTabWidget())
        fifthHorizontalArea.addWidget(self.makeTreeWidget())

        mainLayout.addWidget(self.makeHorizontalLine())

    # --- sixth row ---
        sixthHorizontalArea = QHBoxLayout()
        sixthHorizontalArea.setSpacing(20)
        mainLayout.addLayout(sixthHorizontalArea)

        msgBoxBtn = QPushButton("Message Dialog")
        sixthHorizontalArea.addWidget(msgBoxBtn)
        msgBoxBtn.clicked.connect(partial(QMessageBox().information, self, "Message", "This is normal information message."))

        progressDialogBtn = QPushButton("Progress Dialog")
        sixthHorizontalArea.addWidget(progressDialogBtn)
        progressDialogBtn.clicked.connect(self.showProgressDialog)

        fileDialogBtn = QPushButton("File Dialog")
        sixthHorizontalArea.addWidget(fileDialogBtn)
        fileDialogBtn.clicked.connect(partial(QFileDialog.getOpenFileName, self, "File Select", options = QFileDialog.DontUseNativeDialog))



    def makeHorizontalLine(self):
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        return hline

    def makeListWidget(self):
        listWidget = QListWidget()
        listWidget.setMaximumWidth(100)
        listWidget.addItems(["this", "is", "list", "widget"])
        return listWidget

    def makeTabWidget(self):
        tableWidget = QTableWidget()
        headerLabels = ["Name", "Age", "Sex"]
        tableWidget.setColumnCount(len(headerLabels))
        tableWidget.setHorizontalHeaderLabels(headerLabels)
        tableWidget.verticalHeader().setVisible(False)

        try:
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        except:
            tableWidget.horizontalHeader().setResizeMode(QHeaderView.Interactive)

        tableWidget.setAlternatingRowColors(True)
        tableWidget.horizontalHeader().setStretchLastSection(True)
        dataList = [
            ["Sum", "25", "Male"],
            ["Bob", "26", "Male"],
            ["Erena", "22", "Female"]
        ]
        tableWidget.setRowCount(len(dataList))

        for row, colData in enumerate(dataList):
            for col, value in enumerate(colData):
                item = QTableWidgetItem(value)
                tableWidget.setItem(row, col, item)

        return tableWidget

    def makeTreeWidget(self):
        treeWidget = QTreeWidget()
        headerLabels = ["Name", "Age"]
        treeWidget.setColumnCount(len(headerLabels))
        treeWidget.setHeaderLabels(headerLabels)
        treeWidget.setAlternatingRowColors(True)
        treeData = {
            "Male":[
                {"name":"Jon", "age":"20"},
                {"name":"Ken", "age":"24"},
                {"name":"Alex", "age":"26"}
            ],
            "Female":[
                {"name":"Rucy", "age":"19"},
                {"name":"Queen", "age":"22"}
            ]
        }

        for sex, profiles in treeData.iteritems():
            topItem = QTreeWidgetItem([sex])
            treeWidget.addTopLevelItem(topItem)

            for profile in profiles:
                childItem = QTreeWidgetItem(topItem, [profile.get("name"), profile.get("age")])

        treeWidget.expandAll()
        return treeWidget

    def showProgressDialog(self):
        max = 100
        progressDialog = QProgressDialog("Progress...", "Cancel", 0, max, self)
        progressDialog.setWindowTitle("Progress Dialog")

        for count in range(max + 1):
            qApp.processEvents()

            if progressDialog.wasCanceled():
                break

            progressDialog.setValue(count)
            progressDialog.setLabelText("Progress... %d %%" % count)
            time.sleep(0.1)


def main():
    app = QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()