from geogebra import * 
from field.Polygon import * 
from field.Limit import * 
from field.Point import * 
from field.funct import *
from field.Field import Field
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from path.compute import compute
from view.scalar import plot_scalar

from eval import *
# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")

print(poly)


# Create obj
objs = list()

objs.append(LimitObstacle( 2000,3000  , funct_list["exp"](alpha=0.01, beta=10)))
objs.append(Point(*target,funct_list["exp"](alpha=0.001,beta=-20)))
#objs.append(Polygon(poly,funct_list["log"](alpha=50, beta=.2, ceta=10)))
#objs.append(Polygon(poly, funct_list["lin"](a=20/600, b=10) ))
objs.append(Polygon(poly,funct_list["exp"](alpha=2, beta=10)))



path, it = compute(objs, list(start), list(target))

field = Field()
field.objects = objs
plot_scalar(field,   (0,2000), (0,3000), step=10)

