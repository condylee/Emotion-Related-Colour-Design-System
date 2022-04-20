from matplotlib import pyplot as plt
import matplotlib
import numpy as np
import PIL.Image as Image

plt.subplot(221)
plt.title("all normal LB")
plt.imshow(Image.open(r'D:\大三上\科研/all nor LB.png'))

plt.subplot(222)
plt.title("all normal Levy")
plt.imshow(Image.open(r'D:\大三上\科研/all nor Levy.png'))

plt.subplot(223)
plt.title("self normal LB")
plt.imshow(Image.open(r'D:\大三上\科研/self nor LB.png'))

plt.subplot(224)
plt.title("self normal Levy")
plt.imshow(Image.open(r'D:\大三上\科研/self nor Levy.png'))

plt.show()