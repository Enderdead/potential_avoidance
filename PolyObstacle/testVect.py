import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
from Polygon import *
from math import hypot
import pymp

# Make data.
X = np.arange(100, 1900, 100)
Y = np.arange(100, 2900, 100)
A, B = np.meshgrid(X, Y)
U = np.zeros_like(A,dtype=np.float32)
V = np.zeros_like(A,dtype=np.float32)
poly = Polygon( [( 476,386),\
                 (1125,590),\
                 (1012,970),\
                 (808,1262),\
                 (653,1167),\
                  (508,672)], alpha=0.005, beta=1)

for i in range(A.shape[0]):
    for k in range(A.shape[1]):
        U[i,k] = poly.get_force((A[i,k], B[i,k]))[0]
        V[i,k] = poly.get_force((A[i,k], B[i,k]))[1]
        if hypot(U[i,k],V[i,k])<0.001:
            U[i,k] = np.nan
            V[i,k] = np.nan


fig, ax = plt.subplots()

q = ax.quiver(X, Y, U, V)


plt.show()