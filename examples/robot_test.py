from geogebra import * 
from ObstacleField.PolyObstacle.Polygon import * 
from ObstacleField.MapObstacle.Map import * 
from ObstacleField.PointObstacle.Point import * 
from ObstacleField.funct import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from math import atan2, hypot, pi
import numpy as np
from robot_setup import *
from time import sleep
# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")

K_p_lin = 15
K_p_ang = 2

wheeledbase.set_position( 1000, 400, pi/2)

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
objs.append(Polygon(poly,funct_list["exp"](alpha=0.005, beta=20)))
i = 0
path = list()
try:
    while True:
        i+=1
        x, y, theta = wheeledbase.get_position()
        force = [0, 0]
        for obj in objs:
            force[0] += obj.get_force([x, y])[0]
            force[1] += obj.get_force([x, y])[1]

        omega = atan2(force[1], force[0])
        lin_vel = hypot(*force)
        path.append((x,y))
        wheeledbase.set_velocities(K_p_lin*lin_vel, K_p_ang*(omega-theta))
        sleep(0.1)

except KeyboardInterrupt:
    pass


wheeledbase.stop()
result = "LigneBrisée("
for element in path:
    result +=str(tuple(element))+","

result = result[:-1]+ ")"
print(result)
print("nb it : ",it)
