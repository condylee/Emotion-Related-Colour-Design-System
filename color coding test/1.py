import matplotlib.pyplot as plt
from matplotlib import cm
plt.figure(dpi=150)
import numpy as np

##ListedColormap
#取多种颜色
plt.subplot(1,4,1)
#plt.bar(range(5),range(1,6),color=plt.cm.Accent(range(5)))
#plt.bar(range(5),range(1,6),color=plt.cm.get_cmap('Accent')(range(5)))
plt.bar(range(5),range(1,6),color=plt.get_cmap('Accent')(range(5)))

#取某一种颜色
plt.subplot(1,4,2)
plt.bar(range(5),range(1,6),color=plt.cm.Accent(4))

##LinearSegmentedColormap
#取多种颜色
plt.subplot(1,4,3)
plt.bar(range(5),range(1,6),color=plt.get_cmap('Blues')(np.linspace(0, 1, 5)))

#取一种颜色
plt.subplot(1,4,4)
plt.bar(range(5),range(1,6),color=plt.get_cmap('Blues')(3))