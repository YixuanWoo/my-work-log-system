from sqlite3.dbapi2 import connect
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QWidget
from main_ui import Ui_MainWindow
from AboutUI import Ui_aboutUI
from createProjectUI import Ui_create_Proj_ui
from createRoomUI import Ui_CreateRoom
from editroomUI import Ui_EditRoomForm
import fuction
import sqlite3

#主窗口类
class Mainwindow(QMainWindow,QWidget):
    #主窗口初始化
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
        self.ui.actiondf.triggered.connect(lambda:self.open_aboutWindow)
        self.ui.actionNewProject.triggered.connect(lambda:self.open_createProjWindow(self))
        self.ui.pushButton.clicked.connect(self.loadRoomData)

        self.ui.tableWidget.removeRow(0)
        self.ui.tableWidget.removeColumn(1)

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
        proj=str(self.ui.comboBox.currentText())
        print(proj)
        if (proj == False) or (proj==''):
            self.ui.newRoomButton.setEnabled(False)
        else:
            self.ui.newRoomButton.setEnabled(True)
    def loadRoomData(self):
        proj=str(self.ui.comboBox.currentText())

        if self.ui.viewCbox.currentText()=='全部':
            conn=sqlite3.connect(f'./Data/{proj}.sqlite')
            c=conn.cursor()
            c.execute("SELECT unitNum FROM building;")
            unitNum=c.fetchall()
            unitLst= fuction.exchangeToIntLst(unitNum)
            maxUnit=max(unitLst)
            print(maxUnit)
            


        elif self.ui.comboBox_3.currentText()=='按楼栋':
            pass


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
        self.ProjectText=cbox.ui.comboBox.currentText()
        self.ui.ShowProjLable.setText(self.ProjectText)                         #实现了创建房源是提醒用户此时所处理的项目
        self.ui.pushButton.clicked.connect(lambda:self.creatRoomFunction())     #链接按钮功能
        self.ui.chooseBuildingComBox.addItems(self.readbuildingNo())
        
    
    
    #这个函数实现读取楼栋名称
    def readbuildingNo(self):
        conn=sqlite3.connect(f'./Data/{self.ProjectText}.sqlite') #先打开数据库
        c=conn.cursor()                                           #建立可操作性对象
        c.execute("SELECT No FROM building;")
        buildingNo=c.fetchall()
        print(buildingNo)
        buildinglst=fuction.exchangeToLst(buildingNo)               #数据转化为字符串类型并输出到buildinglst
        #print(buildinglst) 这是一行测试代码，用于测试buildinglst变量的输出内容
        c.close()
        return buildinglst
        
    def creatRoomFunction(self):
        #读取用户输入的各种值
        romNo=self.ui.chooseRomNoBox.value()
        floor=self.ui.spinBox.value()
        buildingNo=self.ui.chooseBuildingComBox.currentText()
        unit=self.ui.chooseUnitBox.value()

        #把数据组合成房号，按照‘楼栋-单元，楼层，房号’的顺序
        roomNo=buildingNo+'-'+str(unit)+str(floor)+str(romNo)
        conn=sqlite3.connect(f'./Data/{self.ProjectText}.sqlite')
        c=conn 
         
        c.execute(f"insert into room(No,floor,unit,building,sell) VALUES({roomNo},{floor},{unit},{buildingNo},False)")
        conn.commit()                   #数据库在操作结束后必须通过commit方法上传才能生效
        conn.close()   
        Reply = QMessageBox.about(self,'翊瑄的消息：','创建成功') 


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