from os import system, listdir, path
from function import close_running_file
from pathlib import Path
from function import telephone, email

folder_path = Path().absolute()  # 文件夹路径
file_names = listdir(folder_path)  # 获取文件夹下所有文件名
bbb = path.basename(__file__)
file_names.remove(bbb)
for file_name in file_names:
    close_running_file(file_name)
system("logonto.py")