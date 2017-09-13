from PySide import QtCore, QtGui
import os.path, sys

CURRENT_PATH = os.path.dirname(__file__)

class SpinBoxDelegate(QtGui.QItemDelegate):
    def createEditor(self, parent, option, index):
        if index.column == 1:
            editor = QtGui.QDoubleSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(100)
            editor.setValue(index.data())
            return editor

    def editorEvent(self, event, model, option, index):
        rect = QtCore.QRect(option.rect.x() + (option.rect.width() / 2) - (option.rect.height() / 2),
                            option.rect.top(),
                            option.rect.height(),
                            option.rect.height())

        if rect.contains(event.pos().x(), event.pos().y()) == True:
            if index.column() == 0:
                if event.type() == QtCore.QEvent.MouseButtonPress:
                    num = index.data()
                    if num == 1:
                        model.setData(index, 0)
                    else:
                        model.setData(index, 1)
        return True

    def setEditorData(self, editor, index):
        value = index.model().data(index, QtCore.Qt.EditRole)
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        editor.interpretText()
        value = editor.value()
        model.setData(index, value, QtCore.Qt.EditRole)

    def paint(self, painter, option, index):
        if index.column() == 0:
            rect = QtCore.QRect(option.rect.x() + (option.rect.width() / 2) - (option.rect.height() / 2),
                                option.rect.top(),
                                option.rect.height(),
                                option.rect.height())
            statusIcon = "ok.png"
            if index.data() == 1:
                statusIcon = "notok.png"
            img = QtGui.QPixmap(os.path.join(CURRENT_PATH, "img", statusIcon))
            painter.drawPixmap(rect, img)

        if index.column() == 1:
            bar = QtGui.QStyleOptionProgressBar()
            bar.rect = option.rect
            bar.rect.setHeight(option.rect.height() - 1)
            bar.rect.setTop(option.rect.top() + 1)
            bar.minimum = 0
            bar.maximum = 100
            bar.progress = int(index.data())
            bar.textVisible = True
            bar.text = str(index.data()) + '%'
            bar.textAlignment = QtCore.Qt.AlignCenter
            QtGui.QApplication.style().drawControl(QtGui.QStyle.CE_ProgressBar, bar, painter)

def main():
    app = QtGui.QApplication(sys.argv)
    model = QtGui.QStandardItemModel(6, 2)
    tableView = QtGui.QTableView()
    tableView.setModel(model)
    delegate = SpinBoxDelegate()
    tableView.setItemDelegate(delegate)

    for row in range(6):
        for column in range(2):
            index = model.index(row, column, QtCore.QModelIndex())
            model.setData(index, (row + 1) * (column + 1))

    tableView.setWindowTitle("Delegate")
    tableView.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()