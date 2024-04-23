from time import sleep

try:
    from allaccount import *
    # 导入用户信息
except:
    a = input("服务器维护中，请稍后再试，请按回车键退出。")
    exit()
from os import system, listdir, path
from function import close_running_file
from pathlib import Path

try:
    from function import telephone, email, activefunction, extract_variable_names, runmodule, searchaccount, strtonumber
except:
    a = input("文件function.py错误或丢失，请运行save.py程序。")
    exit()
from codeall import codeall

folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
choice1 = input("请选择激活方式：\n1.登录    2.注册\n")
while choice1 != "1" and choice1 != "2":
    print("请输入选择内的数字。")
    choice1 = input("请选择激活方式：\n1.登录    2.注册\n")
if choice1 == '2':
    system("enroll.py")
elif choice1 == '1':
    openfile1 = open("allaccount.py", "r")
    openfile1read = openfile1.read().strip()
    openfile1.close()
    logintotelephone = input("输入您账户所关联的电话号码：").strip()
    while not telephone(logintotelephone):
        print("您输入的电话号码有误，请重新输入。")
        logintotelephone = input("输入您账户所关联的电话号码：").strip()
    if telephone(logintotelephone):
        pass

    logintoemail = input("输入您账户所关联的邮箱地址：").strip()
    while not email(logintoemail):
        print("您输入的邮箱地址有误，请重新输入。")
        logintoemail = input("输入您账户所关联的邮箱地址：").strip()
    if email(logintoemail):
        k = [logintoemail, logintotelephone]
        print("正在搜索......")
while not searchaccount(logintoemail,logintotelephone):
    choice = input(
        f"没有与{logintotelephone}和{logintoemail}相关联的账户。\n请检查邮箱账号与电话号码是否匹配，或重新注册一个账号将{logintoemail}和{logintotelephone}关联起来\n是否注册？\n1.是       others.否")
    if choice == '1':
        system("enroll.py")
    else:
        logintotelephone = input("输入您账户所关联的电话号码：").strip()
        while not telephone(logintotelephone):
            print("您输入的电话号码有误，请重新输入。")
            logintotelephone = input("输入您账户所关联的电话号码：").strip()
        if telephone(logintotelephone):
            pass
        logintoemail = input("输入您账户所关联的邮箱地址：").strip()
        while not email(logintoemail):
            print("您输入的邮箱地址有误，请重新输入。")
            logintoemail = input("输入您账户所关联的邮箱地址：").strip()
        if email(logintoemail):
            k = [logintoemail, logintotelephone]
            print("正在搜索......")
if searchaccount(logintoemail, logintotelephone):
    pass
extract = extract_variable_names("allaccount.py")
for i in extract:
    j = eval(i)
    if logintoemail not in j or logintotelephone not in j:
        pass

    elif logintoemail in j and logintotelephone in j:
        password = input("已搜索到账户,请输入密码以确保是你本人。\n")
        choice = 3
        while password != eval(i)[3]:
            if choice >= 1:
                password = input("密码错误，请重新输入。\n")
                choice = choice - 1
            else:
                choice2 = input("您忘记密码了吗？您可以通过验证身份修改密码。\n是否修改？\n1.是    others.否\n")
                if choice2 == "1":
                    pass  # 此处还没有构建。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
                else:
                    password = input("请输入密码:")
                    choice = 3

        if password == eval(i)[3]:

            if len(eval(i)[5]) != 0:
                error = 0
                correctcodelist = []
                for ii in eval(i)[5]:
                    if ii not in codeall:
                        error += 1


                    if ii in codeall:
                        correctcodelist.append(ii)
                if len(correctcodelist) == 0:
                    print(
                        "您的帐户密钥无效，如果您已购买此产品，")  # 此处还没有构建。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
                else:
                    if error == 0:
                        if len(correctcodelist) > 1:
                            print("您的帐户有两个或两个以上密钥：")
                            for i in range(0, len(correctcodelist)):
                                print(f"{i + 1}.{correctcodelist[i]}")
                            choice = input("您想安装哪一个？")

                            while not strtonumber(choice):
                                print("我没有明白您输入了什么。")
                                print("您的帐户有两个或两个以上密钥：")
                                for i in range(0, len(correctcodelist)):
                                    print(f"{i + 1}.{correctcodelist[i]}")
                                choice = input("您想安装哪一个？")
                            if strtonumber(choice):
                                while not 1 <= int(choice) < len(correctcodelist):
                                    print("我没有明白您输入了什么。")
                                    print("您的帐户有两个或两个以上密钥：")
                                    for i in range(0, len(correctcodelist)):
                                        print(f"{i + 1}.{correctcodelist[i]}")
                                    choice = input("您想安装哪一个？")
                                if 1 <= int(choice) < len(correctcodelist):
                                    bbbb = correctcodelist[int(choice) - 1]
                                    openfile1 = open("code.py", "w+")
                                    openfile1.write(bbbb)
                                    openfile1.close()
                        else:
                            bbbb = correctcodelist[0]
                            openfile1 = open("code.py", "w+")
                            openfile1.write(bbbb)
                            openfile1.close()

                    else:
                        print("检测到您的")  # 此处还没有构建。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。
                        q=eval(i)[5]
                        for ii in eval(i)[5]:
                            if ii not in codeall:
                                q.remove(ii)
                            else:
                                pass
                        r=eval(i)
                        r.remove(r[5])
                        r.append(q)
                        openfile1=open("allaccount.py","r+")
                        openfile1read=openfile1.read()
                        aaa=openfile1read.replace(str(eval(i)),str(r))
                        openfile1.seek(0)
                        openfile1.write(aaa)
                        openfile1.truncate()
                        openfile1.close()
                        if len(correctcodelist) > 1:
                            choice = input("您的帐户有两个或两个以上密钥，您想安装哪一个？")
                            for i in range(0, len(correctcodelist)):
                                print(f"{i + 1},{correctcodelist[i]}")
                            while not strtonumber(choice):
                                print("我没有明白您输入了什么。")
                                choice = input("您的帐户有两个或两个以上密钥，您想安装哪一个？")
                                for i in range(0, len(correctcodelist)):
                                    print(f"{i + 1},{correctcodelist[i]}")
                            if strtonumber(choice):
                                while not 1 <= int(choice) < len(correctcodelist):
                                    print("我没有明白您输入了什么。")
                                    choice = input("您的帐户有两个或两个以上密钥，您想安装哪一个？")
                                    for i in range(0, len(correctcodelist)):
                                        print(f"{i + 1},{correctcodelist[i]}")
                                if 1 <= int(choice) < len(correctcodelist):
                                    bbbb = correctcodelist[int(choice) - 1]
                                    openfile1 = open("code.py", "w+")
                                    openfile1.write(bbbb)
                                    openfile1.close()
                        else:
                            bbbb = correctcodelist[0]
                            openfile1 = open("code.py", "w+")
                            openfile1.write(bbbb)
                            openfile1.close()
            print("登录成功，正在返回主界面。")
            openfile3 = open("account.py", "w+")
            openfile3.write(f"youraccount={eval(i)}")
            openfile3.close()
            system("start.py")
    break
