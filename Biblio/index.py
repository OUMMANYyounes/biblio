from PyQt5 import QtCore, QtGui, QtWidgets
############################################################################################
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import subprocess
############################################################################################



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 546)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 40, 391, 391))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(38, 60, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login_Button = QtWidgets.QPushButton(self.groupBox)
        self.login_Button.setGeometry(QtCore.QRect(120, 197, 161, 31))
        self.login_Button.setObjectName("login_Button")
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_username.setGeometry(QtCore.QRect(130, 59, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_username.setFont(font)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_login_error = QtWidgets.QLabel(self.groupBox)
        self.label_login_error.setGeometry(QtCore.QRect(50, 240, 291, 31))
        self.label_login_error.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_login_error.setText("")
        self.label_login_error.setObjectName("label_login_error")
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_password.setGeometry(QtCore.QRect(130, 120, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_error_password = QtWidgets.QLabel(self.groupBox)
        self.label_error_password.setGeometry(QtCore.QRect(100, 140, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_error_password.setFont(font)
        self.label_error_password.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error_password.setText("")
        self.label_error_password.setObjectName("label_error_password")
        self.label_error_username = QtWidgets.QLabel(self.groupBox)
        self.label_error_username.setGeometry(QtCore.QRect(100, 80, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_error_username.setFont(font)
        self.label_error_username.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error_username.setText("")
        self.label_error_username.setObjectName("label_error_username")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 91, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 340, 251, 20))
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(60, 296, 271, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_pic = QtWidgets.QLabel(self.centralWidget)
        self.label_pic.setGeometry(QtCore.QRect(40, 70, 271, 321))
        self.label_pic.setObjectName("label_pic")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
####################################################################################################
        self.lineEdit_username.textChanged.connect(self.clear_u)
        self.lineEdit_password.textChanged.connect(self.clear_p)
        self.login_Button.clicked.connect(self.check_login)
        self.pushButton.clicked.connect(self.signup)


####################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "login"))
        self.groupBox.setTitle(_translate("MainWindow", "Hello, friend!"))
        self.label.setText(_translate("MainWindow", "Username :"))
        self.login_Button.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "Password :"))
        self.pushButton.setText(_translate("MainWindow", "SIGN UP"))
        self.label_3.setText(_translate("MainWindow", "Don\'t have an acounte yet ?"))
        self.label_pic.setText(_translate("MainWindow", ""))
    
    
#####################################################################################################
    def clear_u(self):
        self.label_error_username.setText("")
        self.label_login_error.setText("")
    
    def clear_p(self):
        self.label_error_password.setText("")
        self.label_login_error.setText("")   
    
    def check_login(self):        
        #grab the input
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        #check input
        if len(username) == 0 or  len(password) == 0 :
            if len(username) == 0 :
                self.label_error_username.setText("Don't leave the username blank")
            if len(password) == 0 :
                self.label_error_password.setText("Don't leave the password blank")
        else:        
        
            self.db = QSqlDatabase.addDatabase('QSQLITE')
            self.db.setDatabaseName('users_info.db')
            if not self.db.open():
                QMessageBox.critical(None, 'Error', 'Could not open database')
            query = QSqlQuery()
            query.prepare('SELECT * FROM user WHERE username = :username AND password = :password')
            query.bindValue(':username', username)
            query.bindValue(':password', password)
            if not query.exec():
                QMessageBox.critical(None, 'Error', 'Could not execute query')
            elif query.next():
                QMessageBox.information(None, 'Success', 'Login successful')
                conn = sqlite3.connect('users_info.db')
                cursor = conn.cursor()
                query = "SELECT admin FROM user WHERE username = ?"
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                my_variable = result[0]

                # Close the cursor and database connection
                cursor.close()
                conn.close()
                if my_variable == "yes":
                    print("Welcome Admin")
                    MainWindow.close()
                    subprocess.run(["python", "display_admin.py"])
                else:
                    print("Welcome Guest")
                    MainWindow.close()
                    subprocess.run(["python", "display_guest.py"])
            else:
                self.label_login_error.setText("Invalid username or password")

    def signup(self):
        MainWindow.close()
        subprocess.run(["python", "signup.py"])
        
##################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
