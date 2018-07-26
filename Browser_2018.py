#this is a crazy idea
#shawn April 2018

import sys
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineWidgets  import QWebEngineView

import Browser_UI_2018
reload(Browser_UI_2018)
from Browser_UI_2018 import BrowserDialog
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


class MyBrowser(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = BrowserDialog()
        self.ui.setupUi(self)

        self.startPage = "http://www.google.com"
        self.ui.lineEdit.setText(self.startPage)

        self.loadURL()
        self.ui.lineEdit.returnPressed.connect(self.loadURL)
        self.ui.qwebview.loadFinished.connect(self.updateLink)

    def loadURL(self):
        url = self.ui.lineEdit.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url

        self.ui.qwebview.load(QUrl(url))

    def updateLink(self):
        currURL = self.ui.qwebview.url().toString()
        self.ui.lineEdit.setText(currURL)

def main():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)
    myapp = MyBrowser(mayaMainWindow)
    myapp.show()
