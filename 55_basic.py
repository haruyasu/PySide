import sys
from PySide.QtCore import *
from PySide.QtGui import *

class GUI(QDialog):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)

        self.setWindowTitle("Test")
        self.setWindowFlags(Qt.Tool)

        self.refreshBtn = QPushButton("Refresh")
        self.treeWidget = QTreeWidget()
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)

        layout = QVBoxLayout()
        layout.setContentsMargins(6, 6, 6, 6)
        layout.addWidget(self.refreshBtn)
        layout.addWidget(self.treeWidget)
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    ui = GUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
