import sys
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication,QVBoxLayout
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets import QWebEngineView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class BrowserDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(804, 604)
        self.layout = QVBoxLayout(Dialog)
        self.qwebview = QWebEngineView(Dialog)
        self.qwebview.setGeometry(QtCore.QRect(0, 50, 800, 600))
        self.qwebview.setObjectName(_fromUtf8("kwebview"))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 790, 25))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.qwebview)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Browser", "Browser", None))
