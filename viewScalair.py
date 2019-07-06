from geogebra import * 
from field.Polygon import * 
from field.Map import * 
from field.Point import * 
from field.funct import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from compute import compute
from eval import *
# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")

print(poly)
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, 2000, 10, dtype =np.float32)
Y = np.arange(0, 3000, 10, dtype =np.float32)
X, Y = np.meshgrid(X, Y)
Z = np.zeros_like(X, dtype=np.float32)
# Create obj
objs = list()

objs.append(LimitObstacle( 2000,3000  , funct_list["exp"](alpha=0.01, beta=10)))
objs.append(Point(*target,funct_list["exp"](alpha=0.001,beta=-20)))
#objs.append(Polygon(poly,funct_list["log"](alpha=50, beta=.2, ceta=10)))
#objs.append(Polygon(poly, funct_list["lin"](a=20/600, b=10) ))
objs.append(Polygon(poly,funct_list["exp"](alpha=0.01, beta=10)))

for i in range(X.shape[0]):
    for k in range(X.shape[1]):
        for obj in objs:
            Z[i,k] += obj.get_potential(*[float(X[i,k]), float(Y[i,k])] )


path, it = compute(objs, list(start), list(target))


path_x = np.array([element[0] for element in path], dtype=np.float32)
path_y = np.array([element[1] for element in path], dtype=np.float32)

path_z = np.zeros_like(path_x, dtype=np.float32)
for i in range(path_x.shape[0]):
    for obj in objs:
        path_z[i] += obj.get_potential(*[float(path_x[i]), float(path_y[i])])



ax.plot(path_x, path_y, path_z, color="black")
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
# Add a color bar which maps values to colors.
print(eval(path, target,  it))
plt.show()