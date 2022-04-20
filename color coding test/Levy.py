from matplotlib import pyplot as plt
import matplotlib
import numpy as np

plt.figure()
a=np.outer(np.arange(0,1,0.01),np.ones(10))
cdict1 = {'red':   [
                    (0.0,0.03125,0.03125),
                    (0.099176,  0.110280875, 0.110280875),
                    (0.203348,  0.1932929375, 0.1932929375),
                    (0.309024,  0.2775035, 0.2775035),
                    (0.413252,  0.3605601875, 0.3605601875),
                    (0.517468,  0.4436073125, 0.4436073125),
                    (0.623152,  0.52782425, 0.52782425),
                    (0.727344,  0.61085225, 0.61085225),
                    (0.832996,  0.6950436875, 0.6950436875),
                    (0.937236,  0.7781099375, 0.7781099375),
                    (1.0,  0.828125, 212)
                    ],
         'green': [ (0.0,  133, 0.51953125),
                    (0.099176,  0.54781190625, 0.54781190625),
                    (0.203348,  0.577517203125, 0.577517203125),
                    (0.309024,  0.607651375, 0.607651375),
                    (0.413252,  0.637372640625, 0.637372640625),
                    (0.517468,  0.667090484375, 0.667090484375),
                    (0.623152,  0.6972269375, 0.6972269375),
                    (0.727344,  0.7269379375, 0.7269379375),
                    (0.832996,  0.757065265625, 0.757065265625),
                    (0.937236,  0.786789953125, 0.786789953125),
                    (1.0,  0.8046875, 206)
                    ],
         'blue':  [ (0.0,  171, 0.66796875),
                    (0.099176,  0.61218225, 0.61218225),
                    (0.203348,  0.5535855, 0.5535855),
                    (0.309024,  0.494142749, 0.494142749),
                    (0.413252,  0.4355145, 0.4355145),
                    (0.517468,  0.376893, 0.376893),
                    (0.623152,  0.3174457499, 0.3174457499),
                    (0.727344,  0.25883775, 0.25883775),
                    (0.832996,  0.1994085, 0.1994085),
                    (0.937236,  0.1407735, 0.1407735),
                    (1.0,  0.10546875, 27)
                    ]}
cdict2 = {'red':   [
                    (0.0,0.03125,0.03125),
                    (0.099176,  0.39021987, 0.39021987),
                    (0.203348,  0.554809625, 0.554809625),
                    (0.309024,  0.6809166875, 0.6809166875),
                    (0.413252,  0.7265234375, 0.7265234375),
                    (0.517468,  0.7422665, 0.7422665),
                    (0.623152,  0.75638075, 0.75638075),
                    (0.727344,  0.77145125, 0.77145125),
                    (0.832996,  0.7902893750000001, 0.7902893750000001),
                    (0.937236,  0.8216703125, 0.8216703125),
                    (1.0,  0.828125, 212)
                    ],
         'green': [ (0.0,  133, 0.51953125),
                    (0.099176,  0.64798615625, 0.64798615625),
                    (0.203348,  0.7068834687500001, 0.7068834687500001),
                    (0.309024,  0.752010015625, 0.752010015625),
                    (0.413252,  0.768330078125, 0.768330078125),
                    (0.517468,  0.7739636249999999, 0.7739636249999999),
                    (0.623152,  0.7790143125, 0.7790143125),
                    (0.727344,  0.7844071875, 0.7844071875),
                    (0.832996,  0.79114828125, 0.79114828125),
                    (0.937236,  0.802377734375, 0.802377734375),
                    (1.0,  0.8046875, 206)
                    ],
         'blue':  [ (0.0,  171, 0.66796875),
                    (0.099176,  0.41457825, 0.41457825),
                    (0.203348,  0.29839724999609374, 0.29839724999609374),
                    (0.309024,  0.2093805, 0.2093805),
                    (0.413252,  0.1771874609375, 0.1771874609375),
                    (0.517468,  0.16607474999609376, 0.16607474999609376),
                    (0.623152,  0.15611175, 0.15611175),
                    (0.727344,  0.145473749609375, 0.145473749609375),
                    (0.832996,  0.13217625, 0.13217625),
                    (0.937236,  0.110025, 0.110025),
                    (1.0,  0.10546875, 27)
                    ]}
my_cmap1 = matplotlib.colors.LinearSegmentedColormap('my_colormap1',cdict1,256)
my_cmap2 = matplotlib.colors.LinearSegmentedColormap('my_colormap2',cdict2,256)
plt.title(u'self normal LB ')
plt.imshow(a,aspect='auto', cmap =my_cmap2)
plt.figure()
plt.title(u'self normal LB ')
plt.imshow(a,aspect='auto', cmap =my_cmap1)
plt.show()