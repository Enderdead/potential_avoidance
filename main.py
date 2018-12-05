from geogebra import * 
from PolyObstacle.Polygon import * 
from MapObstacle.Map import * 
from PointObstacle.Point import * 

nb_it = 200
delta = 10

# Extract geogebra data
geo = Geogebra("./main.ggb")
start = geo.get("START")
target = geo.get("END")[0], geo.get("END")[1]
poly_temp = geo.getall("^tot_.*$")
poly = poly_temp[:-2]
maps = geo.get("MAP")
robot_pos = [start[0], start[1]]
robot_vel = [0,0]

# Create obj
objs = list()
objs.append(Map(*maps))
objs.append(Point(*target,alpha=0.0001,beta=-1.5))
objs.append(Polygon(poly,alpha=0.01, beta=10))

path = list()

for _ in range(nb_it):
    robot_pos[0], robot_pos[1] =  robot_pos[0]+robot_vel[0]*delta, robot_pos[1]  + robot_vel[1]*delta
    robot_vel = [0, 0]
    for obj in objs:
        robot_vel[0], robot_vel[1] = (robot_vel[0]+ obj.get_force(robot_pos)[0]*delta),(robot_vel[1]+ obj.get_force(robot_pos)[1]*delta)

    path.append((robot_pos[0],robot_pos[1]))


result = "LigneBrisée("
for element in path:
    result +=str(tuple(element))+","

result = result[:-1]+ ")"

print(result)