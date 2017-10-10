__appname__ = "PyDataMan"
__modlule__ = "main"

from PySide.QtCore import *
from PySide.QtGui import *
import sys, sqlite3, re, os, logging
from ui import mainWindw_PyDataMan

appDataPath = os.environ["APPDATA"] + "\\PyDataMan\\"

if not os.path.exists(appDataPath):
    try:
        os.makedirs(appDataPath)
    except Exception, e:
        appDataPath = os.getcwd()

logging.basicConfig(filename=appDataPath + "pydataman.log",
                    format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s")

logger = logging.getLogger(name="main-gui")

class Main(QMainWindow, mainWindw_PyDataMan.Ui_mainWindow):
    dbPath = appDataPath + "pydata.db"
    dbConn = sqlite3.connect(dbPath)

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.dbCursor = self.dbConn.cursor()
        self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Main(id INTEGER PRIMARY KEY,
                                 username TEXT, name TEXT, phone TEXT, addresss TEXT, status TEXT)""")
        self.dbConn.commit()

        self.settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "PyDataMan", "PyDataMan")

        self.addData.clicked.connect(self.add_button_clicked)
        self.removeRow.clicked.connect(self.remove_row_clicked)
        self.load_initial_settings()

    def load_initial_settings(self):
        """Loads the initial settings for the application. Sets the mainTable colum widths."""
        self.dbCursor.execute("""SELECT * FROM Main""")
        allRows = self.dbCursor.fetchall()

        for row in allRows:
            inx = allRows.index(row)
            self.mainTable.insertRow(inx)
            self.mainTable.setItem(inx, 0, QTableWidgetItem(row[1]))
            self.mainTable.setItem(inx, 1, QTableWidgetItem(row[2]))
            self.mainTable.setItem(inx, 2, QTableWidgetItem(row[3]))
            self.mainTable.setItem(inx, 3, QTableWidgetItem(row[4]))
            self.mainTable.setItem(inx, 4, QTableWidgetItem(row[5]))

    def add_button_clicked(self):
        """Calls the validate_fields() method, and adds the items to the table if true"""
        username = self.userName.text()
        firstname = self.firstName.text()
        phone = self.phoneNumber.text()
        address = self.address.text()
        approved = self.approved.isChecked()

        if not self.validate_fields():
            return False

        currentRowCount = self.mainTable.rowCount()

        self.mainTable.insertRow(currentRowCount)
        self.mainTable.setItem(currentRowCount, 0, QTableWidgetItem(username))
        self.mainTable.setItem(currentRowCount, 1, QTableWidgetItem(firstname))
        self.mainTable.setItem(currentRowCount, 2, QTableWidgetItem(phone))
        self.mainTable.setItem(currentRowCount, 3, QTableWidgetItem(address))
        self.mainTable.setItem(currentRowCount, 4, QTableWidgetItem("Approved" if approved else "Not approved"))

        parameters = (None, username, firstname, phone, address, str(approved))
        self.dbCursor.execute("""INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?)""", parameters)
        self.dbConn.commit()

    def remove_row_clicked(self):
        """Removes the selected row from the mainTable"""
        currentRow = self.mainTable.currentRow()

        if currentRow > -1:
            currentUsername = (self.mainTable.item(currentRow, 0).text(), )
            self.dbCursor.execute("""DELETE FROM Main WHERE username=?""", currentUsername)
            self.dbConn.commit()
            self.mainTable.removeRow(currentRow)

    def validate_fields(self):
        """Validated the QLineEdits based on RegEx"""
        self.dbCursor.execute("""SELECT username FROM Main""")
        usernames = self.dbCursor.fetchall()
        for username in usernames:
            if self.userName.text() in username[0]:
                QMessageBox.warning(self, "Warning", "Such username already exists!!!")
                return False

        if not re.match('^[2-9]\d{2}-\d{3}-\d{4}', self.phoneNumber.text()):
            QMessageBox.warning(self, "Warning", "Phone number seems incorrect!!!")
            return False

        return True

    def import_action_triggered(self):
        """Database import handler"""
        pass

    def export_action_triggered(self):
        """Database export handler"""
        pass

    def preferences_action_trigggered(self):
        """Fires up the Preferences dialog"""
        pass

    def about_action_triggered(self):
        """Opens the About dialog"""
        pass

    def exit_action_triggered(self):
        """Closes the application"""
        pass

def main():
    QCoreApplication.setApplicationName("PyDataMan")
    QCoreApplication.setApplicationVersion("0.1")
    QCoreApplication.setOrganizationName("PyDataMan")
    QCoreApplication.setOrganizationDomain("pydataman.com")

    app = QApplication(sys.argv)
    form =Main()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
