import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter
from collections import OrderedDict
import matplotlib.image as mpimg

cmaps = OrderedDict()

cmaps['Perceptually Uniform Sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']

cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

cmaps['Sequential (2)'] = [   ##  这个的winter我选了！
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']

cmaps['Diverging'] = [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']

cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']

cmaps['Miscellaneous'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'Oranges', 'nipy_spectral',
            'gist_ncar']

nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)   #这里的1貌似对产生color map没有什么影响？
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()


#for cmap_category, cmap_list in cmaps.items():
#    print("cate:",cmap_category)  #cate是该list的key名字
#    print("list:",cmap_list)      #这是整个的list

   # plot_color_gradients(cmap_category, cmap_list, nrows)
#fig, axes = plt.subplots(nrows=nrows)
#fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
"""
for ax, name in zip(axes, cmaps['Sequential (2)']):
    if name=='winter':
      #  ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
      #  pos = list(ax.get_position().bounds)
      #  x_text = pos[0] - 0.01
     #   y_text = pos[1] + pos[3] / 2.
      #  fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)
for ax in axes:
        ax.set_axis_off()
"""
#img = mpimg.imread('D:\大三上\科研/画.jpg')
#print(img)

plt.imshow(X=gradient, aspect='auto', cmap='viridis')
plt.savefig('D:\大三上\科研/test.png')
#plt.imshow(image, cmap=plt.get_cmap('winter'))
#plt.show()

img = mpimg.imread('D:\大三上\科研/test.png')
plt.imshow(img)
plt.show()
print(img)

