

import sys
from PyQt6 import QtCore, QtGui, QtWidgets


import openai



class GPT:
    def __init__(self):
        openai.api_key = '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'
        self.__messages = []


    def request(self, task):
        self.__messages.append({'role': 'user', 'content': task})
        answer = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.__messages
        )
        self.__messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return (answer.choices[0].message.content)

    def run(self, Text):
        return self.request(Text)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 603)
        self.assist = GPT()
        MainWindow.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.GIGACHAT = QtWidgets.QWidget()
        self.GIGACHAT.setObjectName("GIGACHAT")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GIGACHAT)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line1 = QtWidgets.QLineEdit(parent=self.GIGACHAT)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.line1.setFont(font)
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line1.setText("")
        self.line1.setObjectName("line1")
        self.gridLayout_2.addWidget(self.line1, 1, 0, 1, 1)
        self.Dowload = QtWidgets.QPushButton(parent=self.GIGACHAT)
        # self.Dowload.clicked.connect(self.save_text_foo)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Dowload.setFont(font)
        self.Dowload.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 229, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(0, 255, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.Dowload.setObjectName("Dowload")
        self.gridLayout_2.addWidget(self.Dowload, 1, 1, 1, 1)
        self.Otpravit = QtWidgets.QPushButton(parent=self.GIGACHAT)
        self.Otpravit.clicked.connect(self.BTNclic)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Otpravit.setFont(font)
        self.Otpravit.setStyleSheet("QPushButton{ \n"
"background-color: rgb(100, 100, 100);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(199, 199, 199);\n"
"      transition: 0.9s;\n"
"  }")
        self.Otpravit.setObjectName("Otpravit")
        self.gridLayout_2.addWidget(self.Otpravit, 2, 0, 1, 1)
        self.CLEAR = QtWidgets.QPushButton(parent=self.GIGACHAT)
        self.CLEAR.clicked.connect(self.BTN_CLear)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CLEAR.setFont(font)
        self.CLEAR.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 12, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.CLEAR.setObjectName("CLEAR")
        self.gridLayout_2.addWidget(self.CLEAR, 2, 1, 1, 1)
        self.TB = QtWidgets.QTextBrowser(parent=self.GIGACHAT)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.TB.setObjectName("TB")
        self.gridLayout_2.addWidget(self.TB, 0, 0, 1, 2)
        self.tabWidget.addTab(self.GIGACHAT, "")
        self.DUBLER = QtWidgets.QWidget()
        self.DUBLER.setObjectName("DUBLER")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.DUBLER)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line2 = QtWidgets.QLineEdit(parent=self.DUBLER)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.line2.setFont(font)
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setText("")
        self.line2.setObjectName("line2")
        self.gridLayout_4.addWidget(self.line2, 1, 0, 1, 1)
        self.Dowload_2 = QtWidgets.QPushButton(parent=self.DUBLER)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Dowload_2.setFont(font)
        self.Dowload_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 229, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(0, 255, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.Dowload_2.setObjectName("Dowload_2")
        self.gridLayout_4.addWidget(self.Dowload_2, 1, 1, 1, 1)
        self.Otpravit_2 = QtWidgets.QPushButton(parent=self.DUBLER)
        self.Otpravit_2.clicked.connect(self.BTNclic2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Otpravit_2.setFont(font)
        self.Otpravit_2.setStyleSheet("QPushButton{ \n"
"background-color: rgb(100, 100, 100);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(199, 199, 199);\n"
"      transition: 0.9s;\n"
"  }")
        self.Otpravit_2.setObjectName("Otpravit_2")
        self.gridLayout_4.addWidget(self.Otpravit_2, 2, 0, 1, 1)
        self.CLEAR_2 = QtWidgets.QPushButton(parent=self.DUBLER)
        self.CLEAR_2.clicked.connect(self.BTN_CLear_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CLEAR_2.setFont(font)
        self.CLEAR_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 12, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.CLEAR_2.setObjectName("CLEAR_2")
        self.gridLayout_4.addWidget(self.CLEAR_2, 2, 1, 1, 1)
        self.TB2 = QtWidgets.QTextBrowser(parent=self.DUBLER)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TB2.setFont(font)
        self.TB2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.TB2.setObjectName("TB2")
        self.gridLayout_4.addWidget(self.TB2, 0, 0, 1, 2)
        self.tabWidget.addTab(self.DUBLER, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 0, 1, 1)
        self.Dowload_3 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Dowload_3.setFont(font)
        self.Dowload_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 229, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(0, 255, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.Dowload_3.setObjectName("Dowload_3")
        self.gridLayout_3.addWidget(self.Dowload_3, 1, 1, 1, 1)
        self.Otpravit_3 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Otpravit_3.setFont(font)
        self.Otpravit_3.setStyleSheet("QPushButton{ \n"
"background-color: rgb(100, 100, 100);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    background-color: rgb(199, 199, 199);\n"
"      transition: 0.9s;\n"
"  }")
        self.Otpravit_3.setObjectName("Otpravit_3")
        self.gridLayout_3.addWidget(self.Otpravit_3, 2, 0, 1, 1)
        self.CLEAR_3 = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.CLEAR_3.setFont(font)
        self.CLEAR_3.setStyleSheet("QPushButton{\n"
"background-color: rgb(184, 12, 0);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"      \n"
"    \n"
"    background-color: rgb(255, 0, 0);\n"
"      transition: 0.9s;\n"
"  }\n"
"")
        self.CLEAR_3.setObjectName("CLEAR_3")
        self.gridLayout_3.addWidget(self.CLEAR_3, 2, 1, 1, 1)
        self.LABEL = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LABEL.setFont(font)
        self.LABEL.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.LABEL.setText("")
        self.LABEL.setObjectName("LABEL")
        self.gridLayout_3.addWidget(self.LABEL, 0, 0, 1, 2)
        self.tabWidget.addTab(self.widget, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Dowload.setText(_translate("MainWindow", "Скачать"))
        self.Otpravit.setText(_translate("MainWindow", "Отправить "))
        self.CLEAR.setText(_translate("MainWindow", "Очистить"))
        self.TB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body  style=\" font-family:\'MS Shell Dlg 2\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.GIGACHAT), _translate("MainWindow", "GIGACHAT"))
        self.Dowload_2.setText(_translate("MainWindow", "Скачать"))
        self.Otpravit_2.setText(_translate("MainWindow", "Отправить "))
        self.CLEAR_2.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DUBLER), _translate("MainWindow", "DUBLER"))
        self.Dowload_3.setText(_translate("MainWindow", "Скачать"))
        self.Otpravit_3.setText(_translate("MainWindow", "Отправить "))
        self.CLEAR_3.setText(_translate("MainWindow", "Очистить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "KANDINSKY"))

    def BTNclic(self):
        text = self.line1.text()
        self.TB.append(f"Пользователь:\n{text}\n\nGIGACHAT:")
        self.line1.setText("")
        self.TB.append(self.assist.run(text) + "\n")
    def BTNclic2(self):
        from main import Otvet
        text = self.line2.text()
        self.TB2.append(f"Пользователь:\n{text}\n\nDUBLER:")
        self.line2.setText("")
        self.TB2.append(Otvet(text))

    def BTN_CLear(self):
        self.TB.clear()

    def BTN_CLear_2(self):
        self.TB2.clear()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
