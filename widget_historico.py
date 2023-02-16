# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_historico.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Page_historico(object):
    """
    Essa é uma classe para a pagina de historico
    """
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 419)
        Form.setMinimumSize(QtCore.QSize(521, 419))
        Form.setMaximumSize(QtCore.QSize(521, 419))
        Form.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 60, 421, 341))
        self.frame.setStyleSheet("background-color: rgb(235, 255, 234);\n"
"background-color: rgb(221, 223, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 280, 401, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_voltar = QtWidgets.QPushButton(self.frame)
        self.btn_voltar.setGeometry(QtCore.QRect(170, 300, 81, 23))
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
        self.txt_historico = QtWidgets.QTextBrowser(self.frame)
        self.txt_historico.setGeometry(QtCore.QRect(20, 10, 381, 261))
        self.txt_historico.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_historico.setObjectName("txt_historico")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_voltar.setText(_translate("Form", "Voltar"))
        self.txt_historico.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "HISTÓRICO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Page_historico()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
