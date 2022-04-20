import numpy as np
#本文件进行了两个数据集的 统一数据归一化
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
alist=loaddata(r'D:\大三上\科研/LB.txt')
alist2=loaddata(r'D:\大三上\科研/Levy.txt')
alist = list(map(float, alist))
alist2 = list(map(float, alist2))

min1=min(alist)
min2=min(alist2)
max1=max(alist)
max2=max(alist2)
print(min1,min2,max1,max2)
if min1<min2:
    minn=min1
else :
    minn=min2
if max1>max2:
    maxx=max1
else :
    maxx=max2
print(maxx,minn)
print(type(alist[1]))

#========进行minMax方式的归一化=========
for i in range(0,len(alist)):
    alist[i]=(alist[i]-minn)/(maxx-minn)
for i in range(0,len(alist2)):
    alist2[i]=(alist2[i]-minn)/(maxx-minn)

#print(alist)
print(max(alist),min(alist))
#print(alist2)
print(max(alist2),min(alist2))

#==============================================
alist.sort()
alist2.sort()
#print(alist)
#我将数据分到10个bucket里面，进行数据数量的统计。
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
l10=[]

alist3=alist2+alist

delta=0.1
for i in range(len(alist3)):
    if alist3[i]>=minn and alist3[i]<minn+delta:
        l1.append(alist3[i])
    elif alist3[i]>=minn+delta and alist3[i]<minn+2*delta:
        l2.append(alist3[i])
    elif alist3[i]>=minn+2*delta and alist3[i]<minn+3*delta:
        l3.append(alist3[i])
    elif alist3[i]>=minn+3*delta and alist3[i]<minn+4*delta:
        l4.append(alist3[i])
    elif alist3[i]>=minn+4*delta and alist3[i]<minn+5*delta:
        l5.append(alist3[i])
    elif alist3[i] >= minn+5*delta and alist3[i] < minn + 6*delta:
        l6.append(alist3[i])
    elif alist3[i] >= minn + 6*delta and alist3[i] < minn + 7 * delta:
        l7.append(alist3[i])
    elif alist3[i] >= minn + 7 * delta and alist3[i] < minn + 8 * delta:
        l8.append(alist3[i])
    elif alist3[i] >= minn + 8 * delta and alist3[i] < minn + 9 * delta:
        l9.append(alist3[i])
    elif alist3[i] >= minn + 9 * delta and alist3[i] <= maxx:
        l10.append(alist3[i])
alpha1=len(l1)/len(alist3)
alpha2=(len(l1)+len(l2))/len(alist3)
alpha3=(len(l1)+len(l2)+len(l3))/len(alist3)
alpha4=(len(l1)+len(l2)+len(l3)+len(l4))/len(alist3)
alpha5=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5))/len(alist3)
alpha6=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6))/len(alist3)
alpha7=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7))/len(alist3)
alpha8=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7)+len(l8))/len(alist3)
alpha9=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7)+len(l8)+len(l9))/len(alist3)


print("alpha: ")
print(alpha1)
print(alpha2)
print(alpha3)
print(alpha4)
print(alpha5)
print(alpha6)
print(alpha7)
print(alpha8)
print(alpha9)
alpha=[]
alpha.append(alpha1)
alpha.append(alpha2)
alpha.append(alpha3)
alpha.append(alpha4)
alpha.append(alpha5)
alpha.append(alpha6)
alpha.append(alpha7)
alpha.append(alpha8)
alpha.append(alpha9)

#================================================LB 数据
l1.clear()
l2.clear()
l3.clear()
l4.clear()
l5.clear()
l6.clear()
l7.clear()
l8.clear()
l9.clear()
l10.clear()
print("LB num: ")
for i in range(len(alist)):
    if alist[i]>=minn and alist[i]<minn+delta:
        l1.append(alist[i])
    elif alist[i]>=minn+delta and alist[i]<minn+2*delta:
        l2.append(alist[i])
    elif alist[i]>=minn+2*delta and alist[i]<minn+3*delta:
        l3.append(alist[i])
    elif alist[i]>=minn+3*delta and alist[i]<minn+4*delta:
        l4.append(alist[i])
    elif alist[i]>=minn+4*delta and alist[i]<minn+5*delta:
        l5.append(alist[i])
    elif alist[i] >= minn+5*delta and alist[i] < minn + 6*delta:
        l6.append(alist[i])
    elif alist[i] >= minn + 6*delta and alist[i] < minn + 7 * delta:
        l7.append(alist[i])
    elif alist[i] >= minn + 7 * delta and alist[i] < minn + 8 * delta:
        l8.append(alist[i])
    elif alist[i] >= minn + 8 * delta and alist[i] < minn + 9 * delta:
        l9.append(alist[i])
    elif alist[i] >= minn + 9 * delta and alist[i] <= maxx:
        l10.append(alist[i])

print(l1[len(l1)-1])
print(l2[len(l2)-1])
print(l3[len(l3)-1])
print(l4[len(l4)-1])
print(l5[len(l5)-1])
print(l6[len(l6)-1])
print(l7[len(l7)-1])
print(l8[len(l8)-1])
print(l9[len(l9)-1])
print(l10[len(l10)-1])
num_LB=[]
num_LB.append(l1[len(l1)-1])
num_LB.append(l2[len(l2)-1])
num_LB.append(l3[len(l3)-1])
num_LB.append(l4[len(l4)-1])
num_LB.append(l5[len(l5)-1])
num_LB.append(l6[len(l6)-1])
num_LB.append(l7[len(l7)-1])
num_LB.append(l8[len(l8)-1])
num_LB.append(l9[len(l9)-1])
num_LB.append(l10[len(l10)-1])

#=====================================
print("Levy num: ")
l1.clear()
l2.clear()
l3.clear()
l4.clear()
l5.clear()
l6.clear()
l7.clear()
l8.clear()
l9.clear()
l10.clear()

for i in range(len(alist2)):
    if alist2[i]>=minn and alist2[i]<minn+delta:
        l1.append(alist2[i])
    elif alist2[i]>=minn+delta and alist2[i]<minn+2*delta:
        l2.append(alist2[i])
    elif alist2[i]>=minn+2*delta and alist2[i]<minn+3*delta:
        l3.append(alist2[i])
    elif alist2[i]>=minn+3*delta and alist2[i]<minn+4*delta:
        l4.append(alist2[i])
    elif alist2[i]>=minn+4*delta and alist2[i]<minn+5*delta:
        l5.append(alist2[i])
    elif alist2[i] >= minn+5*delta and alist2[i] < minn + 6*delta:
        l6.append(alist2[i])
    elif alist2[i] >= minn + 6*delta and alist2[i] < minn + 7 * delta:
        l7.append(alist2[i])
    elif alist2[i] >= minn + 7 * delta and alist2[i] < minn + 8 * delta:
        l8.append(alist2[i])
    elif alist2[i] >= minn + 8 * delta and alist2[i] < minn + 9 * delta:
        l9.append(alist2[i])
    elif alist2[i] >= minn + 9 * delta and alist2[i] <= maxx:
        l10.append(alist2[i])

print(l1[len(l1)-1])
print(l2[len(l2)-1])
print(l3[len(l3)-1])
print(l4[len(l4)-1])
print(l5[len(l5)-1])
print(l6[len(l6)-1])
print(l7[len(l7)-1])
print(l8[len(l8)-1])
print(l9[len(l9)-1])
print(l10[len(l10)-1])
num_Levy=[]
num_Levy.append(l1[len(l1)-1])
num_Levy.append(l2[len(l2)-1])
num_Levy.append(l3[len(l3)-1])
num_Levy.append(l4[len(l4)-1])
num_Levy.append(l5[len(l5)-1])
num_Levy.append(l6[len(l6)-1])
num_Levy.append(l7[len(l7)-1])
num_Levy.append(l8[len(l8)-1])
num_Levy.append(l9[len(l9)-1])
num_Levy.append(l10[len(l10)-1])





def makeGradient(r0,g0,b0,r1,g1,b1,alpha):
    rr=[]
    gg=[]
    bb=[]
    delta_r=abs(r1-r0)
    delta_g=abs(g1-g0)
    delta_b=abs(b1-b0)
    for i in range(0,len(alpha)):
       if r0<r1:
           rr.append(r0 + delta_r * alpha[i])
       else:
           rr.append(r0-delta_r*alpha[i])
       if g0<g1:
           gg.append(g0 + delta_g * alpha[i])
       else:
           gg.append(g0 - delta_g * alpha[i])
       if b0<b1:
          bb.append(b0 + delta_b * alpha[i])
       else:
          bb.append(b0 - delta_b * alpha[i])
    rr.append(r1)
    bb.append(b1)
    gg.append(g1)
    print(rr)
    print(gg)
    print(bb)
makeGradient(8,133,171,212,206,27,alpha)

rr=[8,65.730776, 97.230416, 124.30856, 139.693424, 152.21779999999998, 164.934344, 177.698216, 191.71913600000002, 205.425896, 212]
gg=[133,153.65856200000002, 164.93049200000002, 174.62022, 180.125588, 184.60735, 189.157878, 193.725342, 198.74263200000001, 203.647502, 206]
bb=[171,130.248864, 108.013824, 88.89984, 78.039936, 69.1992, 60.222815999999995, 51.213024000000004, 41.31590399999999, 31.640544000000006, 27]


def RGBguiyi(aa):
    for i in range (0,len(aa)):
        aa[i]=aa[i]/256
    print(aa)
print('\n')
RGBguiyi(rr)
RGBguiyi(gg)
RGBguiyi(bb)