from PySide import QtCore, QtGui
import sys
import os.path


class MainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.mainLayout = QtGui.QVBoxLayout()
        self.open_file_button = QtGui.QPushButton('open file')
        self.connect(self.open_file_button, QtCore.SIGNAL("clicked()"), self.open_file)
        self.mainLayout.addWidget(self.open_file_button)
        self.open_folder_button = QtGui.QPushButton('open folder')
        self.connect(self.open_folder_button, QtCore.SIGNAL("clicked()"), self.open_folder)
        self.mainLayout.addWidget(self.open_folder_button)
        self.setLayout(self.mainLayout)
        self.setWindowTitle('open')
        self.setMinimumSize(200, 200)

    def open_file(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file', os.path.expanduser('~') + '/Desktop')
        print filename

    def open_folder(self):
        foldername = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', os.path.expanduser('~') + '/Desktop')
        print foldername


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    md = MainDialog()
    md.show()
    app.exec_()
