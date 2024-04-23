from function import activefunction
from os import system
from time import sleep


a = "code.py"
b = "r+"
openflie = open(a, b)
c=openflie.read()
openflie.close()
if activefunction(c):
    print("你已激活此产品，确认更换许可证吗？")
    choice = input("1.Yes    2.No\n")
    if choice == "1":
        sleep(0.5)
        print("请邮件至micro201014@outlook.com获取安装多个许可证的方法。")
        system("main.py")
    if choice == "2":
        system("main.py")

if not activefunction(c):
    from account import accountactive
    if accountactive=="yes":
        from random import choice
        from codeleaved import codeleaved
        given=choice(codeleaved)
        print("新用户免费赠送密钥：",given)
system("main.py")



