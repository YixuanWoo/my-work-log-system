from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from main_ui import Ui_MainWindow
from AboutUI import Ui_aboutUI
from createProjectUI import Ui_create_Proj_ui
from createRoomUI import Ui_CreateRoom
from editroomUI import Ui_EditRoomForm
import sqlite3
import fuction

#主窗口类
class Mainwindow(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()

        #创建self.ui实例
        self.ui=Ui_MainWindow()
        #UI初始化
        self.ui.setupUi(self)
        #初始化时读取数据库文件，如果有项目就将项目读入多选下拉框
        self.projectList=fuction.listSQLiteData()
        if self.projectList!=[]:
            self.ui.comboBox.addItems(self.projectList)   #ComboBox是项目读取控件，UI文档中未改名，在此标注
        #以下开始是各个按钮关联的槽函数
        self.ui.staticButton.clicked.connect(self.staticFunction)
        self.ui.newRoomButton.clicked.connect(self.open_createRoomWindow)
        self.ui.editRoomButton.setEnabled(False)
        self.ui.editRoomButton.clicked.connect(self.open_editRoomWindow)
        self.ui.actiondf.triggered.connect(lambda:self.open_aboutWindow())
        self.ui.actionNewProject.triggered.connect(lambda:self.open_createProjWindow())
    

    #点击统计按钮所实现的功能
    def staticFunction(self):
       Reply = QMessageBox.about(self,'抱歉','此功能暂未开发\n敬请期待')
    #调用关于信息的窗口
    def open_aboutWindow(self):
        self.windowAbout=Aboutwindow()
        self.windowAbout.show()
    #新建项目按钮的的槽函数
    def open_createProjWindow(self):
        self.createProjWindow=CreateProjectWindow()
        self.createProjWindow.show()
    
    #调用创建新房源的函数：
    def open_createRoomWindow(self):
        self.windowCreateRoom=CreateRoomWindow()
        self.windowCreateRoom.show()
    #打开编辑房屋的函数：
    def open_editRoomWindow(self):
        self.editRoomWindow=EditRoomWindow()
        self.editRoomWindow.show()
    
    #该函数负责让combox载入数据库信息并添加选项
    def loadProjData():
        if self.projectList==[]:
            pass

#创建关于信息的类
class Aboutwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_aboutUI()
        self.ui.setupUi(self)
#定义创建项目的窗口类
class CreateProjectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui1=Ui_create_Proj_ui()
        self.ui1.setupUi(self)
        self.ui1.creatProjConfirmButton.clicked.connect(self.creat_project_data)

    #点击创建项目按钮之后的槽函数，包括读取文本框信息写入数据库
    def creat_project_data(self):
        name=self.ui1.projNameInput.text()
        address=self.ui1.ProjAddressInput.text()
        buildingNum=int(self.ui1.buildingNumInput.value())
        noStart=self.ui1.buildingNoStart.value()
        nostop=self.ui1.spinBox_2.value()   #这里的spinBox2是楼栋号截止数
        #print(name) 本行代码用于命令行测试，不测试时注释掉，保留代码内容
#************************************************************************************************************
        #下面代码负责创建项目数据库，并建立第一个数据库表格，存储用户输入的项目基础信息
        conn=sqlite3.connect(f'./Data/{name}.sqlite')
        c=conn.cursor() 
        c.execute('''create table project
        (
        name text not null,
        address char(50), buildingNum int not null);''')
        c.execute(f"insert into project(name,address,buildingNum) VALUES('{name}','{address}',{buildingNum})")
        c.execute('''create table building
        (No int not null,
        unitNum int not null,
        floormax int not null)''')
        for no in range(noStart,nostop+1):
            c.execute(f'''insert into building(No,unitNum,floormax) VALUES({no},3,22)''')
        conn.commit()                   #数据库在操作结束后必须通过commit方法上传才能生效
        conn.close()                    #关闭数据库
        self.close()                    #关闭自己的窗口
#定义创建房间c窗口类
class CreateRoomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_CreateRoom()
        self.ui.setupUi(self)

#定义编辑房间窗口类
class EditRoomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_EditRoomForm()
        self.ui.setupUi(self)

#以下是主程序运行区 
app=QApplication([])
a=Mainwindow()
a.show()
app.exec_()