import sys
from PySide import QtGui

def print_state(state):
    if state:
        print("enable")
    else:
        print("disable")

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle("Check")
    main_window.resize(300, 100)
    panel = QtGui.QWidget()
    checkbox = QtGui.QCheckBox("Checkbox", parent=panel)
    button = QtGui.QPushButton("Push checkbox state", parent=panel)
    layout = QtGui.QVBoxLayout()
    layout.addWidget(checkbox)
    layout.addWidget(button)
    panel.setLayout(layout)
    button.clicked.connect(checkbox.toggle)
    checkbox.stateChanged.connect(print_state)
    main_window.setCentralWidget(panel)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()