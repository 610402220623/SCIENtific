from codeleaved import codeleaved
from tempfile import mkstemp
from shutil import move, copymode
from os import system, listdir, path, fdopen, remove
from account import *
from function import close_running_file, remove_line, activefunction,returnaccount
from pathlib import Path
from about import version
from allaccount import *

folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)

addmorecode = youraccount[5]
actcode = codeleaved
yourcode = youraccount[5]
accountactive = youraccount[0]

filename1 = "codeleaved.py"
openmode1 = "r+"
openfile1 = open(filename1, openmode1)
openfile1.read()


def replacement(filepath, hardships, situations):
    fd, abspath = mkstemp()
    with fdopen(fd, "w") as file1:
        with open(filepath, "r") as file0:
            for line in file0:
                file1.write(line.replace(hardships, situations))
    copymode(filepath, abspath)
    remove(filepath)
    move(abspath, filepath)


if accountactive != "yes":
    exit()

choice1 = input("你确定要添加密钥吗？\n1.是     2.否\n")
while choice1 != "1" and choice1 != "2":
    print("你输入了什么？")
    choice1 = input("1.是     2.否\n")
if choice1 == "2":
    system("main.py")
elif choice1 == "1":
    input1 = input("请输入您想添加的密钥：")
    while input1 != "ok":
        if not activefunction(input1, version):
            print("您输入的密钥无效，请重新输入，如果您想退出，请输入ok退出")
        if activefunction(input1, version):
            opencode = open("code.py", "r+")
            codeused = opencode.read()
            if input1 not in codeleaved:
                print("您输入的密钥已被使用，请输入新密钥")
            elif input1 in yourcode:
                print("您输入的密钥已被您使用，请输入新密钥")
            else:
                addmorecode.append(input1)
                actcode.remove(input1)
                openmode2 = "w+"
                openfile2 = open(filename1, openmode2)
                openfile2.write(f"codeleaved={actcode}")
                openfile2.close()
                openfile3=open("account.py","w+")
                openfile3.read()
                allyourcode=youraccount[5]
                allyourcode.append(input1)
                del youraccount[5]
                youraccount.append(allyourcode)
                openfile3.write(f"youraccount={youraccount}")
                openfile3.close()
                openfile4=open("allaccount.py","r+")
                openfile4read=openfile4.read()
                openfile4.seek(0)
                openfile4.write(openfile4read.replace(str(eval(returnaccount(youraccount[1],youraccount[2]))),str(youraccount)))
                openfile4.close()

                print("添加成功，您可以继续添加密钥。")
        input1 = input("请输入您想添加的密钥：")
    if input1 == "ok":
        system("start.py")
