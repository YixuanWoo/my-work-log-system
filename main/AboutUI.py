# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutUI(object):
    def setupUi(self, aboutUI):
        aboutUI.setObjectName("aboutUI")
        aboutUI.resize(274, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(aboutUI.sizePolicy().hasHeightForWidth())
        aboutUI.setSizePolicy(sizePolicy)
        aboutUI.setMinimumSize(QtCore.QSize(274, 0))
        aboutUI.setMaximumSize(QtCore.QSize(274, 210))
        self.textBrowser = QtWidgets.QTextBrowser(aboutUI)
        
        self.textBrowser.setGeometry(QtCore.QRect(9, 9, 256, 192))
        self.textBrowser.setMaximumSize(QtCore.QSize(256, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(aboutUI)
        QtCore.QMetaObject.connectSlotsByName(aboutUI)

    def retranslateUi(self, aboutUI):
        _translate = QtCore.QCoreApplication.translate
        aboutUI.setWindowTitle(_translate("aboutUI", "关于"))
        self.textBrowser.setHtml(_translate("aboutUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">UI设计/程序开发：翊瑄</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">GUI开发库：PyQt5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">数据库：SQLite</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">本软件已开源，源码地址：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/YixuanWoo/my-work-log-system\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub地址</span></a></p></body></html>"))
