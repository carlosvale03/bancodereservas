# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_sacar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Page_sacar(object):
    """
    Essa é uma classe para a pagina de saque
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 386)
        Form.setMinimumSize(QtCore.QSize(521, 386))
        Form.setMaximumSize(QtCore.QSize(521, 386))
        Form.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.btn_voltar = QtWidgets.QPushButton(Form)
        self.btn_voltar.setGeometry(QtCore.QRect(220, 310, 81, 23))
        self.btn_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet("QPushButton{\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(202, 202, 202);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(122, 122, 122);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.btn_voltar.setObjectName("btn_voltar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 80, 401, 281))
        self.frame.setStyleSheet("background-color: rgb(235, 255, 234);\n"
"background-color: rgb(221, 223, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 210, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_sacar = QtWidgets.QPushButton(self.frame)
        self.btn_sacar.setGeometry(QtCore.QRect(150, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sacar.setFont(font)
        self.btn_sacar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sacar.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(4, 4, 4);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_sacar.setObjectName("btn_sacar")
        self.txt_senha = QtWidgets.QLineEdit(self.frame)
        self.txt_senha.setGeometry(QtCore.QRect(130, 100, 141, 20))
        self.txt_senha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_valor = QtWidgets.QLineEdit(self.frame)
        self.txt_valor.setGeometry(QtCore.QRect(130, 60, 141, 20))
        self.txt_valor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_valor.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_valor.setObjectName("txt_valor")
        self.frame.raise_()
        self.btn_voltar.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_voltar.setText(_translate("Form", "Voltar"))
        self.label.setText(_translate("Form", "SACAR"))
        self.btn_sacar.setText(_translate("Form", "Sacar"))
        self.txt_senha.setPlaceholderText(_translate("Form", "Digite sua senha"))
        self.txt_valor.setPlaceholderText(_translate("Form", "Digite o valor aqui"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Page_sacar()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
