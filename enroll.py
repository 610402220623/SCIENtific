from os import listdir, path
from function import checkpassword, close_running_file, email, telephone,activefunction,checkrows
from pathlib import Path
from about import version
folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
a = "code.py"
b = "r+"
openflie = open(a, b)
c = openflie.read()
openflie.close()
if not activefunction(c,version):
    answer1 = input("您是第一次使用这个软件吗？\n1.是    others.否\n")
    if answer1 == "1":
        answer2 = input("要查看关于此产品的使用教程吗？\n1.是     others.否\n")
        if answer2 == "1":
            pass
        else:
            pass
    else:
        pass
else:
    pass

youremail = input("Email:")
while not email(youremail):
    print("您输入的电子邮件有误，请重新输入")
    youremail = input("Email:")
if email(youremail):
    yourtelephone = input("Telephone:")
    while not telephone(yourtelephone):
        print("您输入的电话号码非中国大陆发行，如果您是外国用户，请使用中国代理。")
        yourtelephone = input("Telephone:")
    if telephone(yourtelephone):
        yourname=input("请设置您的用户名：")
        while len(yourname) == 0:
            print("姓名不能为空，请重新输入。")
            yourname = input("请设置您的用户名：")
        password = input("请设置密码以确保账户的安全性。\n")
        while not checkpassword(password):
            password = input("你设置的密码强度过低，请重新设置。\n")

        if len(yourname) != 0 and checkpassword(password):
            print("注册成功，正在保存信息...")
            paccount=["yes",youremail,yourtelephone,password,yourname,[]]
            openfile2 = open("account.py", "w+")
            openfile2.write(f"youraccount={paccount}")
            openfile2.close()
            aa=checkrows("allaccount.py")
            openflie3=open("allaccount.py","r")
            c=openflie3.read()
            openflie3.close()
            for i in range(1,aa+5):
                b="account"+str(i)
                if b in c:
                    pass
                else:
                    openflie3=open("allaccount.py","a+")
                    openflie3.write(f"{b}={paccount}\n")
                    openflie3.close()
                    break

            print("保存成功。")
            choice = input("请按回车键退出。")

