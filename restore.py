from time import sleep
from os import system,listdir,path
from function import close_running_file
from pathlib import Path
folder_path =Path().absolute() # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
choice1 = input("""确定要退出登录吗？\n1.是     2.否\n""")
if choice1 == "2":
    system("start.py") and exit()
while choice1 != "1" and choice1 != "2":
    sleep(0.2)
    print("此选择无效。")
    choice1 = input("""1.是     2.否\n""")
if choice1 == "1":
    filename1 = "firstrun.py"
    filename2 = "code.py"
    filename3 = "account.py"
    openmode1 = "w+"
    openmode2 = "w"
    openmode3 = "w+"
    fileopen1 = open(filename1, openmode1)
    fileopen1.write("Yes")
    fileopen1.close()
    fileopen2 = open(filename2, openmode2)
    fileopen2.truncate()
    fileopen2.close()
    fileopen3 = open(filename3, openmode3)
    fileopen3.write('youraccount = ["no", "NOemail", "NOtelephone", "NOHAVEPASSWORD", "NOname", []]')
    fileopen3.close()
    choice3 = input("请按回车键退出。")

