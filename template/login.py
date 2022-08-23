# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'primeira_tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
#
# ########################## Descrição do Projeto ####################################  Nada de Plagiar seu cuzaão
#
# Nome do Projeto : Ferramenta Controle de Coletores                         Data inicio : 01/09/2021 V.1.0 - JSolutions # Recusa Imitações
# 
# Autores : Sérgio F. 
#



from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Login(object):
        
        # Criador : Sérgio F.
        # Descrição das Funções :
        # Validações de Usuário e Senha MsgBox
        
    styleEditOk = ("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148, 0, 211);        \n"
"    color: rgb(148, 0, 211);\n"
"}")
    
    styleEditError = ("QLineEdit {\n"
"    border: 2px solid rgb(255, 85, 127);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(148, 0, 211);        \n"
"    color: rgb(148, 0, 211);\n"
"}")
    stylePopupError = ("background-color: rgb(255, 85, 127);border-radius: 5px;")
    
    stylePopupOk = ("background-color: rgb(0, 255, 123);border-radius: 5px;")  
      

    def checkFields(self):
            
         textUser = ""
         textPassword = ""
         
         # Checkando Usuário 
         
         def showMessage(message):
                self.frame_error.show()
                self.label_error.setText(message) 
         
         if not self.lineEdit_user.text():
                textUser = " Usuário Vazio "
                self.lineEdit_user.setStyleSheet(self.styleEditError)
         else:
                textUser = ""
                self.lineEdit_user.setStyleSheet(self.styleEditOk)
                
                
          # Checkando Senha      
                
         if not self.lineEdit_password.text():
                textPassword = " Senha Vazia "
                self.lineEdit_password.setStyleSheet(self.styleEditError)
         else:
                textPassword = ""
                self.lineEdit_password.setStyleSheet(self.styleEditOk)
                
          # Check Fildes
                
         if textUser + textPassword != "":
                text = textUser + textPassword
                showMessage(text)
                self.frame_error.setStyleSheet(self.stylePopupError)
         else:   
                 text = "Login OK ."
                 
                 showMessage(text)
                 self.frame_error.setStyleSheet(self.stylePopupOk)
                 
                 # Salvar Usuário
                 
         #if self.checkBox_save_user.isChecked():
                 #text = text + "| Usuário Salvo : OK"        
                 #showMessage(text)
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet(self.stylePopupError)
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("color: rgb(35, 35, 35);")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_close_popup = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;    \n"
"    background-image: url(:/Close_Image/Images/cil-x.png);\n"
"    background-position: center;    \n"
"    background-color: rgb(60, 60, 60);\n"
"    color: rgb(255, 250, 250);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);    \n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.pushButton_close_popup.setText("")
        self.pushButton_close_popup.setObjectName("pushButton_close_popup")
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.avatar = QtWidgets.QFrame(self.login_area)
        self.avatar.setGeometry(QtCore.QRect(165, 90, 120, 120))
        self.avatar.setStyleSheet("QFrame {\n"
"    background-image: url(:/Close_Image/Images/avatar.png);\n"
"    border-radius: 60px;\n"
"    border: 10px solid rgb(148, 0,211);\n"
"    background-position: center;\n"
"}\n"
"QFrame:hover {\n"
"    border: 10px solid rgb(153, 51, 153);\n"
"}\n"
"\n"
"")
        self.avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setObjectName("avatar")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_user.setGeometry(QtCore.QRect(85, 288, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setStyleSheet(self.styleEditOk)
        self.lineEdit_user.setMaxLength(10)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_password = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_password.setGeometry(QtCore.QRect(85, 350, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setStyleSheet(self.styleEditOk)
        self.lineEdit_password.setMaxLength(10)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_login = QtWidgets.QPushButton(self.login_area)
        self.pushButton_login.setGeometry(QtCore.QRect(85, 425, 300, 60))
        self.pushButton_login.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(148, 0, 211);\n"
"    border: 2px solid rgb(128, 0, 128);    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.pushButton_login.setObjectName("pushButton_login")
        
        
   
   
        
        self.label = QtWidgets.QLabel(self.login_area)
        self.label.setGeometry(QtCore.QRect(60, 10, 331, 51))
        self.label.setStyleSheet("color: rgb(95, 95, 95);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login_area)
        self.label_2.setGeometry(QtCore.QRect(60, 230, 331, 51))
        self.label_2.setStyleSheet("color:  rgb(55, 55, 55);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_credits = QtWidgets.QLabel(self.bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout_2.addWidget(self.label_credits)
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        

        # Creator : Sérgio F.
        # Descrição :
        # Função para fechar o Popup - Bt Close red "X"
        
        self.pushButton_close_popup.clicked.connect(lambda:self.frame_error.hide())
        
        
        # Creator : Sérgio F.
        # Descrição : 
        # Ocultar Pop-up quando iniciada o Login
        
        self.frame_error.hide()
        
        
        #Chamada pro Login 
        
        self.pushButton_login.clicked.connect(self.checkFields)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tela de Login : Collector Control"))
        self.label_error.setText(_translate("MainWindow", "ERROR"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow", "USUÁRIO"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow", "SENHA"))
        self.pushButton_login.setText(_translate("MainWindow", "CONECTAR - CONTROLE DE COLETORES"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; color:#959595;\">BEM VINDO!</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#414141;\">ACESSAR</span><span style=\" font-size:11pt; color:#414141;\"> | COLLECTOR CONTROL</span></p></body></html>"))
        self.label_credits.setText(_translate("MainWindow", "Created by: JSolutions - CD RJ - 2021"))
        
import template.files_rc
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
