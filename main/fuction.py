
import os

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


listSQLiteData()