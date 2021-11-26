import os
import os.path

dir = './'


# 列出目录下的所有UI文件
def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir+os.sep)
        # print(filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    return list


# 更改拓展名为.py
def trans_py_file(filename):
    return os.path.splitext(filename)[0] + '.py'


def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = trans_py_file(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile} '.format(pyfile=pyfile, uifile=uifile)
        os.system(cmd)


if __name__ == "__main__":
    runMain()