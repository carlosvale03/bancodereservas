# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_excluir.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Page_excluir(object):
    """
    Essa é uma classe para a pagina de excluir conta
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(516, 307)
        Form.setMinimumSize(QtCore.QSize(516, 307))
        Form.setMaximumSize(QtCore.QSize(516, 307))
        Form.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 40, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 80, 401, 201))
        self.frame.setStyleSheet("background-color: rgb(235, 255, 234);\n"
"background-color: rgb(221, 223, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 130, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_excluir = QtWidgets.QPushButton(self.frame)
        self.btn_excluir.setGeometry(QtCore.QRect(150, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_excluir.setFont(font)
        self.btn_excluir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(4, 4, 4);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.btn_excluir.setObjectName("btn_excluir")
        self.txt_senha = QtWidgets.QLineEdit(self.frame)
        self.txt_senha.setGeometry(QtCore.QRect(130, 40, 141, 20))
        self.txt_senha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.btn_voltar = QtWidgets.QPushButton(self.frame)
        self.btn_voltar.setGeometry(QtCore.QRect(160, 160, 81, 23))
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
        self.frame.raise_()
        self.label.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "EXCLUIR CONTA"))
        self.btn_excluir.setText(_translate("Form", "Excluir"))
        self.txt_senha.setPlaceholderText(_translate("Form", "Digite sua senha"))
        self.btn_voltar.setText(_translate("Form", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Page_excluir()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
