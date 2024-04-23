
from allaccount import *
from about import version
try:
    from function import activefunction
except ModuleNotFoundError:
    print("配置文件function.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
except ImportError:
    print("配置文件function.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
try:
    from codeleaved import codeleaved
except ModuleNotFoundError:
    print("配置文件codeleaved.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
except ImportError:
    print("配置文件codeleaved.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
try:
    from account import youraccount
except ModuleNotFoundError:
    print("配置文件account.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
except ImportError:
    print("配置文件account.py发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
try:
    from tempfile import mkstemp
    from shutil import move, copymode
    from os import fdopen, remove,system
    from time import sleep
except ModuleNotFoundError:
    print("python核心组件发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()
except ImportError:
    print("python核心组件发生错误，无法执行代码。")
    i = input("按任意键退出。")
    exit()

yourcode = youraccount[5]


def replacement(filepath, hardships, situations):
    fd, abspath = mkstemp()
    with fdopen(fd, "w") as file1:
        with open(filepath, "r") as file0:
            for line in file0:
                file1.write(line.replace(hardships, situations))
    copymode(filepath, abspath)
    remove(filepath)
    move(abspath, filepath)


actcode = codeleaved
filename1 = "codeleaved.py"
openmode1 = "r+"
openfile1 = open(filename1, openmode1)
openfile1.read()

a = "code.py"
b = "r+"
openflie = open(a, b)
c = openflie.read()
openflie.close()
if not activefunction(c,version):

    step1 = input("""确定激活？\n1.激活    2.退出\n""")
    if step1 == "1":
        step2 = input("""准备激活？\n1.购买此产品     2.我已有产品密钥\n""")
        if step2 == "1":
            system("buy.py")
        elif step2 == "2":
            codepass = input("输入产品密钥：")
            while codepass != "0" and activefunction(codepass,version) == False or codepass not in codeleaved:
                print("此密钥无效或已被输入，请重新输入，或输入0退出")
                codepass = input("输入产品密钥：")
            if codepass != "0" and activefunction(codepass,version) == True and codepass in codeleaved:
                w = "w+"
                openflie = open(a, w)
                openflie.write(codepass)
                openflie.truncate()
                openflie.close()
                actcode.remove(codepass)
                act1 = repr(actcode)
                openmode2 = "w+"
                openfile2 = open(filename1, openmode2)
                openfile2.write(f"codeleaved={act1}")
                openfile2.close()
                if codepass not in yourcode:
                    codepass1 = codepass
                    print("正在关联账户与许可证......")
                    aaa=youraccount.remove([])
                    list1=[]
                    list1.append(codepass1)
                    aaa.append(list1)
                    openflie3=open("account.py","w+")
                    openflie3.write(f"youraccount={aaa}")
                    openflie3.close()
                    print("成功！")
                else:
                    pass
                print("激活成功，现在你可以永久使用此产品")
                system("main.py")
            elif codepass == "0" or codepass == 0:
                exit()
    if step1 == "2":
        exit()
