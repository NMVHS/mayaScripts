#this is a crazy idea
#shawn April 2018

import sys
from PySide import QtCore, QtGui
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebView

import Browser_UI_2016
reload(Browser_UI_2016)
from Browser_UI_2016 import BrowserDialog
from maya import OpenMayaUI as omui
from shiboken import wrapInstance


class MyBrowser(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
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
    mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)
    myapp = MyBrowser(mayaMainWindow)
    myapp.show()
