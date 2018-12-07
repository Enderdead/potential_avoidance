from geogebra import * 
from ObstacleField.PolyObstacle.Polygon import * 
from ObstacleField.MapObstacle.Map import * 
from ObstacleField.PointObstacle.Point import * 
from ObstacleField.funct import *
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


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, 3000, 10, dtype =np.float32)
Y = np.arange(0, 3000, 10, dtype =np.float32)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X, dtype=np.float32)
# Create obj
objs = list()

objs.append(Map(*maps, funct_list["exp"](alpha=0.01, beta=10)))
objs.append(Point(1000,1000,funct_list["exp"](alpha=0.001,beta=-2)))
objs.append(Polygon(poly,funct_list["exp"](alpha=0.01, beta=10)))

for i in range(X.shape[0]):
    for k in range(X.shape[1]):
        for obj in objs:
            Z[i,k] += hypot(*obj.get_force([float(X[i,k]), float(Y[i,k])]  ))


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)



# Add a color bar which maps values to colors.
plt.show()