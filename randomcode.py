from datetime import datetime
from hashlib import sha512

def madecode(version):
    codelist = []
    for i in range(1, 500):
        codelist1 = []
        k = "SCIENtific" + str(i) + str(datetime.now())
        j = sha512(k.encode("utf-8")).hexdigest()
        Versioninformation = sha512(version.encode("utf-8")).hexdigest()
        for p in range(0, 128):
            codelist1.append(j[p])
            codelist1.append(Versioninformation[p])
        del codelist1[255]
        code = "".join(codelist1).strip()
        codelist.append(code)
    return codelist
madecode1=input("此软件的最新发行版本总号：")
list1=["1","2","3","4","5","6","7","8","9","0"]
while madecode1 not in list1:
    print("ERROR")
    madecode1 = input("此软件的最新发行版本总号：")
if madecode1 in list1:
    madecode2=input("请输入发行分号：")
madecode3=madecode2+"."+madecode1
codelist=madecode(madecode3)
strcodelist = str(codelist)
openfile = open("codeall.py", "w+")
openfile.write(f"codeall={strcodelist}")
openfile.close()
openfile2=open("codeleaved.py","w+")
openfile2.write(f"codeleaved={strcodelist}")
openfile2.close()
a=input("重置成功,请按回车键退出。")
exit()
