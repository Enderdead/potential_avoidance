from geogebra import * 
from field.Polygon import * 
from field.Map import * 
from field.Point import * 
from field.funct import *
from field.Field import Field
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from view.vector import plot_vector
# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")


# Create obj
objs = list()

objs.append(Map(2000,3000, funct_list["exp"](alpha=0.01, beta=10)))
#objs.append(Point(*target,funct_list["lin"](a=7/3000,b=-7)))
#objs.append(Polygon(poly,funct_list["exp"](alpha=0.01, beta=20)))


f = Field()
f.objects = objs

plot_vector(f, (0,2500), (0,3500))