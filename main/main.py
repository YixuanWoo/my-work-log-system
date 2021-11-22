from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from main_ui import Ui_MainWindow
from AboutUI import Ui_aboutUI
from createProjectUI import Ui_create_Proj_ui
from createRoomUI import Ui_CreateRoom
from editroomUI import Ui_EditRoomForm
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
        self.loadProjData()   
        #以下开始是各个按钮关联的槽函数
        self.ui.staticButton.clicked.connect(self.staticFunction)
        self.ui.newRoomButton.clicked.connect(lambda:self.open_createRoomWindow(self))
        self.ui.editRoomButton.setEnabled(False)
        self.ui.editRoomButton.clicked.connect(self.open_editRoomWindow)
        self.ui.actiondf.triggered.connect(lambda:self.open_aboutWindow())
        self.ui.actionNewProject.triggered.connect(lambda:self.open_createProjWindow(self))

    #点击统计按钮所实现的功能
    def staticFunction(self):
       Reply = QMessageBox.about(self,'抱歉','此功能暂未开发\n敬请期待')
    #调用关于信息的窗口
    def open_aboutWindow(self):
        self.windowAbout=Aboutwindow()
        self.windowAbout.show()
    #新建项目按钮的的槽函数
    def open_createProjWindow(self,window):
        self.createProjWindow=CreateProjectWindow(window)
        self.createProjWindow.show()
    #调用创建新房源的函数：
    def open_createRoomWindow(self,cbox):
        self.windowCreateRoom=CreateRoomWindow(cbox)
        self.windowCreateRoom.show()
    #打开编辑房屋的函数：
    def open_editRoomWindow(self):
        self.editRoomWindow=EditRoomWindow()
        self.editRoomWindow.show()
    #该函数负责让combox载入数据库信息并添加选项
    def loadProjData(self):
        self.projectList=fuction.listSQLiteData()
        if self.projectList!=[]:
            names=fuction.getFileNames(self.projectList)
            self.ui.comboBox.addItems(names)        



#创建关于信息的类
class Aboutwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_aboutUI()
        self.ui.setupUi(self)


#定义创建项目的窗口类
class CreateProjectWindow(QWidget):
    def __init__(self,window):
        super().__init__()
        self.ui1=Ui_create_Proj_ui()
        self.ui1.setupUi(self)
        self.ui1.creatProjConfirmButton.clicked.connect(lambda:self.creat_project_data(window))

    #点击创建项目按钮之后的槽函数，包括读取文本框信息写入数据库
    def creat_project_data(self,window):
        #读取用户输入的各类数据
        name=self.ui1.projNameInput.text()
        address=self.ui1.ProjAddressInput.text()
        buildingNum=int(self.ui1.buildingNumInput.value())
        noStart=self.ui1.buildingNoStart.value()
        nostop=self.ui1.spinBox_2.value()                       #这里的spinBox2是楼栋号截止数
        #print(name) 本行代码用于命令行测试，不测试时注释掉，保留代码内容

        #下面代码负责创建项目数据库，并建立第一个数据库表格，存储用户输入的项目基础信息
        fuction.createProjectSQLite(name,address,buildingNum,noStart,nostop)
        window.loadProjData()
        self.close()                    #功能实现后把自己关掉


#定义创建房间c窗口类
class CreateRoomWindow(QWidget):
    def __init__(self,cbox):
        super().__init__()
        self.ui=Ui_CreateRoom()
        self.ui.setupUi(self)
        ProjectText=cbox.ui.comboBox.currentText()
        self.ui.ShowProjLable.setText(ProjectText)  #实现了创建房源是提醒用户此时所处理的项目


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