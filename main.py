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

from account import *


from os import system, listdir, path
from function import close_running_file,activefunction
from pathlib import Path
accountactive=youraccount[0]

folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)

if accountactive == "no":
    print("请先登录后再使用，SCIENtific会将您的许可证和您的帐户绑定在一起")
    system("logonto.py")
if accountactive == "yes":
    pass
a = "code.py"
b = "r+"
openflie = open(a, b)
c = openflie.read()
openflie.close()
if not activefunction(c):
    print("此产品没有激活，请先激活。")
    system("activated.py")
else:

    a = input(
        """欢迎回来，请选择您想做的事情：\n1.计算黎曼函数值    2.判断素数     3.判断两数是否互质\n4.计算正态分布值    5.敬请期待\n如果您想退出，请按0键然后按回车键。\n请输入您选择的数字：""")
    while a != "0":
        if a == "1":
            system("lmfunction.py")
        if a == "2":
            system("prime.py")

        else:
            print("请输入选择内的数字。")
            a = int(input("请输入您选择的数字，如果您输入的是小数，程序将向下取整："))
    if a == "0":
        print("正在关闭......")
        exit()
