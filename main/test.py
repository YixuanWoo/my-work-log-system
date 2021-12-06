import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class CellTextAlignment(QWidget):
    def __init__(self):
        super(CellTextAlignment, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格对齐方式")
        self.resize(400, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '年龄'])
        Item1 = QTableWidgetItem('老王')
        
        # 设置单元格对齐方式：常量在Qt中
        Item1.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        tableWidget.setItem(0, 0, Item1)

        tableWidget.setSpan(1, 1, 1, 2)

        self.setLayout(layout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellTextAlignment()
    main.show()
    sys.exit(app.exec_())

