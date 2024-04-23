def remove_line(fileName, lineToSkip):
    with open(fileName, 'r', encoding='utf-8') as read_file:
        lines = read_file.readlines()
    currentLine = 1
    with open(fileName, 'w', encoding='utf-8') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
            currentLine += 1


from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen


def replacement(filepath, hardships, situations):
    fd, abspath = mkstemp()
    with fdopen(fd, "w") as file1:
        with open(filepath, "r") as file0:
            for line in file0:
                file1.write(line.replace(hardships, situations))
    copymode(filepath, abspath)
    remove(filepath)
    move(abspath, filepath)


from os import remove, rename


def removespace(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    new_lines = []
    for line in lines:
        if line.strip() != "":
            new_lines.append(line)
    new_file = open("usingusingusing.py", "w")
    new_file.writelines(new_lines)
    new_file.close()
    remove(filename)
    rename("usingusingusing.py", filename)


import subprocess


def close_running_file(filename):
    process = subprocess.Popen(["python", filename])
    process.terminate()


def checkpassword(a):
    if len(a) < 10:
        b = False
    else:
        try:
            c = float(a)
            b = False
        except ValueError:
            b = True
    return b


def telephone(a):
    if len(a) == 11:
        if a[0] == "1":
            try:
                aa = int(a)
                if aa == int(a):
                    b = True
                else:
                    b = False
            except:
                b = False
        else:
            b = False
    else:
        b = False
    return b


def email(a):
    if len(a) >= 12:
        if "@qq.com" in a or "@outlook.com" in a or "@hotmail.com" in a or "@163.com" in a or "@158.com" in a or "@sina.com" in a or "@oldzhang.com" in a or "@gmail.com" in a or "@foxmail.com" in a or "@54181452.com" in a:
            return True
        else:
            return False
    else:
        return False


from json import loads


def inputaccount(email, telephone, password):
    result = False
    list1 = [email, telephone, password]
    for line in open("allaccount.py", "r+"):
        line2 = line[line.find("{"):]
        line3 = loads(line2)
        line4 = list(line3.values())
        if list1 == line4:
            result = True
    return result


# -*- coding:UTF-8 -*-
__author__ = 'rxz'

from datetime import datetime
from hashlib import sha1


def activefunction(a, version):
    from codeall import codeall
    from codeleaved import codeleaved
    result = False
    if a in codeall and a in codeleaved:
        result = True
    else:
        pass
    return result


def check_variable(variable_name):
    try:
        dir(variable_name)
        result = True
    except NameError:
        result = False
    return result


def checkrows(filename):
    # 打开文件
    with open(filename) as f:
        # 初始化计数器
        count = 0
        # 循环遍历每一行
        for line in f:
            # 计数器加一
            count += 1
        # 输出行数
    return count


def lineread(filename):
    file = open(filename, "r")
    a = file.read()
    file.close()
    return a


import ast
import glob


def extract_variable_names(file_pattern):
    variable_names = []
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            content = file.read()
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            variable_names.append(target.id)
                        elif isinstance(target, ast.Tuple):
                            variable_names.extend([name.id for name in target.elts if isinstance(name, ast.Name)])
    return variable_names


def runmodule(filename, start, finish):  # 指定文件名和行号
    # 读取文件内容
    with open(filename, 'r') as file:
        lines = file.readlines()
    # 提取指定行的代码
    exec_lines = []
    for number in range(start, finish + 1):
        exec_lines.append(lines[number - 1].strip())  # 行号是从1开始的，所以减1
    # 执行代码
    for line in exec_lines:
        exec(line)


from allaccount import *


def searchaccount(email, telephone):
    def extract_variable_names1(file_pattern):
        variable_names = []
        for file_path in glob.glob(file_pattern):
            with open(file_path, 'r') as file:
                content = file.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                variable_names.append(target.id)
                            elif isinstance(target, ast.Tuple):
                                variable_names.extend([name.id for name in target.elts if isinstance(name, ast.Name)])
        return variable_names

    extract = extract_variable_names1("allaccount.py")
    result = False
    for i in extract:
        j = eval(i)
        if email not in j or telephone not in j:
            pass
        elif email in j and telephone in j:
            result = True
            break
    return result


def strtonumber(a):
    try:
        b = int(a)
        result = True
    except:
        result = False


def changetext(filename, a, b):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        for line in f.readlines():
            if line != '\n':
                lines.append(line)
        f.close()
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            if a in line:
                line = b
                f.write('%s\n' % line)
            else:
                f.write('%s' % line)


def activefunction2(a, version):
    from codeall import codeall
    from codeleaved import codeleaved
    result = False
    for i in range(1, 1001):
        codelist1 = []
        k = "SCIENtific" + str(i) + str(datetime.now())
        j = sha1(k.encode("utf-8")).hexdigest()
        Versioninformation = sha1(version.encode("utf-8")).hexdigest()
        for p in range(0, 40):
            codelist1.append(j[p])
            codelist1.append(Versioninformation[p])
        code = "".join(codelist1).strip()
        if code == a and a in codeall and a not in codeleaved:
            result = True
            break
        else:
            pass
    return result


def returnaccount(email, telephone):
    def extract_variable_names1(file_pattern):
        variable_names = []
        for file_path in glob.glob(file_pattern):
            with open(file_path, 'r') as file:
                content = file.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Assign):
                        for target in node.targets:
                            if isinstance(target, ast.Name):
                                variable_names.append(target.id)
                            elif isinstance(target, ast.Tuple):
                                variable_names.extend([name.id for name in target.elts if isinstance(name, ast.Name)])
        return variable_names

    extract = extract_variable_names1("allaccount.py")
    result = False
    for i in extract:
        j = eval(i)
        if email not in j or telephone not in j:
            pass
        elif email in j and telephone in j:
            result = i
            break
    return result
def replaceletter(mode,original_string,new_char, index_to_replace=False,old_char=False,time=1):
    if mode=="1":
        replaced_string = original_string[:index_to_replace] + new_char + original_string[index_to_replace + 1:]
    elif mode=="2":
        replaced_string = original_string.replace(old_char, new_char, time)
    return replaced_string