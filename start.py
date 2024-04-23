
aa = "firstrun.py"
bb = "r+"
openfirst = open(aa, bb)
read = openfirst.read()
if read != "No":
    openfirst = open(aa, "w+")
    openfirst.write("No")
    openfirst.truncate()
    openfirst.close()

else:
    pass

from os import system,listdir,path
from about import version
from account import *
from function import close_running_file,activefunction
from pathlib import Path
folder_path =Path().absolute() # 文件夹路径
accountactive=youraccount[0]
youremail=youraccount[1]
yourtelephone=youraccount[2]
yourname=youraccount[4]
yourcode=youraccount[5]


file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
a = "code.py"
b = "r+"
openflie = open(a, b)
c=openflie.read()
openflie.close()
if not activefunction(c,version):
    print("此产品未激活，请先激活后使用。")
    system("activated.py")
elif activefunction(c,version):
    choice1=input("请选择您想做的事情\n1.查看我的账户    2.进入主程序     3.退出\n4.管理我的账户      5.添加许可证密钥\n")
    while choice1=="1":
        print("账户激活状态：",accountactive)
        print("您关联的邮箱：",youremail)
        print("您关联的电话号码：",yourtelephone)
        print("您的姓名：",yourname)
        print("与您的帐户关联的许可证密钥：")
        for i in yourcode:
            print(i)
        choice1 = input("请选择您想做的事情\n1.查看我的账户    2.进入主程序     3.退出\n4.管理我的账户      5.添加许可证密钥\n")
    if choice1 == "2":
        system("main.py")
    if choice1 == "3":
        print("正在关闭......")
        exit()
    if choice1 == "4":
        pass
    if choice1 == "5":
        system("addmorecode.py")
        


