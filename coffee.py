import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('bd.ui', self)
        self.con = sqlite3.connect("coffe.db")
        self.pushButton.clicked.connect(self.update_result)
        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()

        result = cur.execute("Select * from coffee WHERE id=?",
                             (self.spinBox.text(),)).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())