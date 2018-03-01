from PySide.QtCore import *
from PySide.QtGui import *


class Test(QDialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)

        for i in range(10):
            item = QListWidgetItem("Item %i" % i)
            self.listWidget.addItem(item)

        # self.listWidget.itemClicked.connect(self.printItemText)
        self.connect(self.listWidget, SIGNAL("itemSelectionChanged()"), self.printItemText)

    def printItemText(self):
        items = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.listWidget.selectedItems()[i].text()))
            print x


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = Test()
    form.show()
    app.exec_()
