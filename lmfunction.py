from os import system, listdir, path
from function import close_running_file
from pathlib import Path


folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
if not activefunction(c):
    print("此产品未激活，请先激活后使用。")
    system("activated.py")
elif activefunction(c):
print("""黎曼函数计算程序已启动，如果您想使用它，请按照要求操作：
1.自变量power大于1;
2.结束值end大于500；
如果您想退出，请在power或end处输入0，然后按回车键。""")


def lmfunction(power, end):
    list1 = []
    if power <= 1:
        return False
    elif end <= 500:
        return False
    else:
        for i in range(1, int(end)):
            a = i ** (-power)
            list1.append(a)
        result = sum(list1)
        return result


power = input("Power：").strip()
end = input("End：").strip()
while power != "0" and end != "0":
    try:
        power = float(power)
        end = int(end)
        result = lmfunction(power, end)
        if result == False:
            print(
                """计算发生了错误，可能有以下原因：\n1.黎曼函数只在x>1的情况下有值；\n2.当结束值太小时，无法精确估计黎曼函数值；\n此程序将结束值的要求设置到了500以上，请按照最小要求输入自变量。""")
        else:
            print(result)
        power = float(input("Power："))
        end = int(input("End："))
    except ValueError:
        print("您输入的字符串无法转换成数字,请检查以下几点：\n1.检查是否在数字中间输入空格；\n2.检查是否输入字母，汉字及其他符号\n检查完毕后，请重新输入。")
        power = input("Power：").strip()
        end = input("End：").strip()
if power != 0 or end != 0:
    print("正在关闭......")
    system("main2.py")

