# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editroomUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditRoomForm(object):
    def setupUi(self, EditRoomForm):
        EditRoomForm.setObjectName("EditRoomForm")
        EditRoomForm.resize(350, 400)
        EditRoomForm.setMinimumSize(QtCore.QSize(350, 400))
        EditRoomForm.setMaximumSize(QtCore.QSize(350, 400))
        self.groupBox = QtWidgets.QGroupBox(EditRoomForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 310, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.showBuildingLable = QtWidgets.QLabel(self.groupBox)
        self.showBuildingLable.setGeometry(QtCore.QRect(90, 40, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showBuildingLable.setFont(font)
        self.showBuildingLable.setObjectName("showBuildingLable")
        self.showUnitLable = QtWidgets.QLabel(self.groupBox)
        self.showUnitLable.setGeometry(QtCore.QRect(190, 40, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showUnitLable.setFont(font)
        self.showUnitLable.setObjectName("showUnitLable")
        self.showFloorlable = QtWidgets.QLabel(self.groupBox)
        self.showFloorlable.setGeometry(QtCore.QRect(230, 40, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showFloorlable.setFont(font)
        self.showFloorlable.setObjectName("showFloorlable")
        self.showRoomNumLable = QtWidgets.QLabel(self.groupBox)
        self.showRoomNumLable.setGeometry(QtCore.QRect(270, 40, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showRoomNumLable.setFont(font)
        self.showRoomNumLable.setObjectName("showRoomNumLable")
        self.groupBox_2 = QtWidgets.QGroupBox(EditRoomForm)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 310, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(20, 50, 271, 160))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 6, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 8, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 7, 0, 1, 1)
        self.editConfirmButton = QtWidgets.QPushButton(EditRoomForm)
        self.editConfirmButton.setGeometry(QtCore.QRect(260, 360, 70, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.editConfirmButton.setFont(font)
        self.editConfirmButton.setObjectName("editConfirmButton")

        self.retranslateUi(EditRoomForm)
        QtCore.QMetaObject.connectSlotsByName(EditRoomForm)

    def retranslateUi(self, EditRoomForm):
        _translate = QtCore.QCoreApplication.translate
        EditRoomForm.setWindowTitle(_translate("EditRoomForm", "??????????????????"))
        self.groupBox.setTitle(_translate("EditRoomForm", "????????????"))
        self.label.setText(_translate("EditRoomForm", "?????????"))
        self.showBuildingLable.setText(_translate("EditRoomForm", "?????????"))
        self.showUnitLable.setText(_translate("EditRoomForm", "??????"))
        self.showFloorlable.setText(_translate("EditRoomForm", "??????"))
        self.showRoomNumLable.setText(_translate("EditRoomForm", "??????"))
        self.groupBox_2.setTitle(_translate("EditRoomForm", "?????????"))
        self.label_6.setText(_translate("EditRoomForm", "???????????????"))
        self.label_3.setText(_translate("EditRoomForm", "????????????"))
        self.label_2.setText(_translate("EditRoomForm", "????????????"))
        self.label_5.setText(_translate("EditRoomForm", "????????????????????????"))
        self.comboBox.setItemText(0, _translate("EditRoomForm", "?????????"))
        self.comboBox.setItemText(1, _translate("EditRoomForm", "??????"))
        self.label_4.setText(_translate("EditRoomForm", "????????????????????????"))
        self.editConfirmButton.setText(_translate("EditRoomForm", "??????"))
