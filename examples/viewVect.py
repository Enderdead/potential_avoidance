from geogebra import * 
from field.Polygon import * 
from field.Map import * 
from field.Point import * 
from field.funct import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")




# Make data.
X = np.arange(0, 2000, 100, dtype =np.float32)
Y = np.arange(0, 3000, 125, dtype =np.float32)
X, Y = np.meshgrid(X, Y)
U = np.zeros_like(X,dtype=np.float32)
V = np.zeros_like(X,dtype=np.float32)
# Create obj
objs = list()

objs.append(Map(2000,3000, funct_list["exp"](alpha=0.01, beta=10)))
objs.append(Point(*target,funct_list["lin"](a=7/3000,b=-7)))
objs.append(Polygon(poly,funct_list["exp"](alpha=0.01, beta=20)))

for i in range(X.shape[0]):
    for k in range(X.shape[1]):
        for obj in objs:
            U[i,k] += obj.get_force(*[float(X[i,k]), float(Y[i,k])])[0]
            V[i,k] += obj.get_force(*[float(X[i,k]), float(Y[i,k])])[1]

fig, ax = plt.subplots()

q = ax.quiver(X, Y, U, V)


plt.show()