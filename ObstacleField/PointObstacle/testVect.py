import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
from Point import *
from math import hypot
import pymp
import sys
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from funct import *
# Make data.
X = np.arange(100, 1900, 100)
Y = np.arange(100, 2900, 100)
A, B = np.meshgrid(X, Y)
U = np.zeros_like(A,dtype=np.float32)
V = np.zeros_like(A,dtype=np.float32)

f = funct_list["log"]( alpha=900, beta=400)
point = Point( 1000,1500, f)

for i in range(A.shape[0]):
    for k in range(A.shape[1]):
        U[i,k] = point.get_force((A[i,k], B[i,k]))[0]
        
        V[i,k] = point.get_force((A[i,k], B[i,k]))[1]
        if hypot(U[i,k],V[i,k])<0.001:
            U[i,k] = np.nan
            V[i,k] = np.nan

fig, ax = plt.subplots()

q = ax.quiver(X, Y, U, V)


plt.show()