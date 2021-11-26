#本文档定义各类功能函数
import os
import webbrowser
import sqlite3
#查询所有.sqlite格式的文件！ 
def listSQLiteData():
    s = os.listdir('./Data/')   
    #print(s)
    f_file = []
    for i in s:
        if i.endswith('.sqlite'):
            #print(i)
            f_file.append(i)
    return f_file

#访问个人GitHub网页的功能函数
def acessGitHub():
    url = 'https://github.com/YixuanWoo/my-work-log-system'
    webbrowser.open_new_tab(url) 
    browser= webbrowser.get()
    browser.open_new(url)
    
#获取文件名称中剔除后缀的文件名函数
def getFileName(file_name):
    # 输出为 test.py
    file_name = file_name.split('.')[0]
    return file_name
#c从列表中返回一个剔除后缀的文件名列表
def getFileNames(files):
    namelst=[]
    for name in files:
        namelst.append(getFileName(name))
    return namelst

def createProjectSQLite(name,address,buildingNum,noStart,nostop):
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
        c.execute('''create table room
        (No int not null,
        building int not null,
        floor int not null,
        unit int not null,
        area real,
        sell blob,
        buyer text)''')
        for no in range(noStart,nostop+1):
            c.execute(f'''insert into building(No,unitNum,floormax) VALUES({no},3,22)''')
        conn.commit()                   #数据库在操作结束后必须通过commit方法上传才能生效
        conn.close()                    #关闭数据库


def exchangeToIntLst(data):
    strlst=[]
    IntLst=[]
    for item in data :
        number=item[0]                                  #读取元组中的数据
        strlst.append(str(number))  
    for item in strlst:
        IntLst.append(int(item))
    return IntLst

def exchangeTostrLst(data):
    strlst=[]
    for item in data :
        number=item[0]                                  #读取元组中的数据
        strlst.append(str(number))  
    return strlst