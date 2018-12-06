import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import matplotlib.animation as animation
from matplotlib import cm
from math import hypot
from Polygon import *
import pymp


fig = plt.figure()
ax = fig.gca(projection='3d')


# Make data.
X = np.arange(0, 2000, 10)
Y = np.arange(0, 3000, 10)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X,dtype=np.float)
poly = Polygon( [( 476,386),\
                 (1125,590),\
                 (1012,970),\
                 (808,1262),\
                 (653,1167),\
                  (508,672)], alpha=0.005, beta=1)
for i in range(X.shape[0]):
    for k in range(X.shape[1]):
        Z[i,k] = hypot(*poly.get_force((X[i,k],Y[i,k])))



# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colo

plt.show()
