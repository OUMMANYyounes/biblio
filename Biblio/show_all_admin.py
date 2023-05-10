from PyQt5.QtCore import Qt

from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.QtWidgets import QApplication, QTableView
import subprocess

app = QApplication([])
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("Books_Manga.sqlite")
db.open()

model = QSqlTableModel()
model.setTable("books")
model.select()

view = QTableView()
view.setModel(model)
view.resizeColumnsToContents()
view.setGeometry(500,400,930,300)
view.show()

app.exec_()
subprocess.run(["python", "display_admin.py"])