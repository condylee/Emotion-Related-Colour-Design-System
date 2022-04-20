# 把 x 中的变量类型由字符串变为 int
import re
def loaddata(filename):
    data=[]
    with open (filename) as txtData:
        lines=txtData.readlines()
        for line in lines:
            lineData=re.split('\s+',line.strip())
            for i in range(0,len(lineData)):
                data.append(lineData[i])

    return data
alist=loaddata(r'D:\大三上\科研/LB2.txt')
alist = list(map(float, alist))
print(alist)
print(type(alist[1]))


#print(alist)