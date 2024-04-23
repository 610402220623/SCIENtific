

from os import system, listdir, path

from function import close_running_file,activefunction
from pathlib import Path

folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
a = "code.py"
b = "r+"
openflie = open(a, b)
c = next(openflie)
openflie.close()
if not activefunction(c):
    print("此产品没有激活，请先激活。")
    choice = input("""1.激活     2.关闭""")
    if choice == "1":
        system("activated.py")
    if choice == "2":
        exit()
else:
    def prime(a):
        b = True
        if a <= 1:
            b = "error"
        elif a == 2:
            b = True
        for i in range(2, a):
            if a % i == 0:
                b = False
                break
        return b


    a = input("请输入您想判断的整数，如果您输入的是小数，程序将向下取整：")
    while a != "0":
        try:
            a = int(a)
            if not prime(a):
                print("合数")
            elif prime(a) == True:
                print("质数")
            elif prime(a) == "error":
                print("您输入的值小于或等于1，因此无法判断，请重新输入。")
            a = input("请输入您想判断的整数，如果您输入的是小数，程序将向下取整：")
        except ValueError:
            print("您输入的字符串无法转换成数字,请检查以下几点：\n1.检查是否在数字中间输入空格；\n2.检查是否输入字母，汉字及其他符号\n检查完毕后，请重新输入。")
            a = input("请输入您想判断的整数，如果您输入的是小数，程序将向下取整：")
    if a == "0":
        print("正在关闭......")

        system("main2.py")
