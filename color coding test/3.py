#list=[35,20,45,12,21,28,46,64,73,78,54,20,21,22,23,24,4,3,5,2,3,10,11,14]
from sklearn import preprocessing
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
alist=loaddata(r'D:\大三上\科研/Levy.txt')
alist = list(map(float, alist))
alist.sort()
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
maxx=max(alist)
minn=min(alist)
print("max: ",maxx)
print("min: ",minn)
#============先进行正则化：
for i in range(0,len(alist)):
    alist[i]=(alist[i]-minn)/(maxx-minn)
minn=0
maxx=1


#delta=float((maxx-minn)/10)  #分成五份
delta=0.1
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
alpha1=len(l1)/len(alist)
alpha2=(len(l1)+len(l2))/len(alist)
alpha3=(len(l1)+len(l2)+len(l3))/len(alist)
alpha4=(len(l1)+len(l2)+len(l3)+len(l4))/len(alist)
alpha5=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5))/len(alist)
alpha6=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6))/len(alist)
alpha7=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7))/len(alist)
alpha8=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7)+len(l8))/len(alist)
alpha9=(len(l1)+len(l2)+len(l3)+len(l4)+len(l5)+len(l6)+len(l7)+len(l8)+len(l9))/len(alist)


"""print("1:",l1)
print("2:",l2)
print("3:",l3)
print("4:",l4)
print("5:",l5)
print("6:",l6)
print("7:",l7)
print("8:",l8)
print("9:",l9)
print("10:",l10)
"""

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

print("num: ")
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
num=[]
num.append(l1[len(l1)-1])
num.append(l2[len(l2)-1])
num.append(l3[len(l3)-1])
num.append(l4[len(l4)-1])
num.append(l5[len(l5)-1])
num.append(l6[len(l6)-1])
num.append(l7[len(l7)-1])
num.append(l8[len(l8)-1])
num.append(l9[len(l9)-1])
num.append(l10[len(l10)-1])
"""
78   2

0.375
0.7083333333333334
0.8333333333333334
0.875
"""
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

rr=[8,99.896288, 142.03126400000002, 174.314672, 185.99, 190.020224, 193.633472, 197.49152, 202.31408000000002, 210.3476, 212]
gg=[133,165.884456, 180.96216800000002, 192.514564, 196.6925, 198.13468799999998, 199.427664, 200.80824, 202.53396, 205.4087, 206]
bb=[171,106.132032, 76.389695999, 53.601408, 45.35999, 42.515135999, 39.964608, 37.2412799, 33.83712, 28.1664, 27]


#========================
print('\n')
print('\n')



def RGBguiyi(aa):
    for i in range (0,len(aa)):
        aa[i]=aa[i]/256
    print(aa)

RGBguiyi(rr)
RGBguiyi(gg)
RGBguiyi(bb)
"""
min_max_scaler = preprocessing.MinMaxScaler()

rr_minMax = min_max_scaler.fit_transform(rr)
print(rr_minMax)
gg_minMax=min_max_scaler.fit_transform(gg)
print(gg_minMax)
bb_minMax=min_max_scaler.fit_transform(bb)
print(bb_minMax)
"""