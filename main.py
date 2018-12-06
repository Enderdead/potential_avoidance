from geogebra import * 
from ObstacleField.PolyObstacle.Polygon import * 
from ObstacleField.MapObstacle.Map import * 
from ObstacleField.PointObstacle.Point import * 

max_it = 500
delta = 1 #TOUT LE TEMPS

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
objs.append(Point(*target,alpha=0.0001,beta=-15))
objs.append(Polygon(poly,alpha=0.01, beta=100))

path = list()
it = 0 
while(hypot(robot_pos[0]-target[0], robot_pos[1]- target[1])>10 and it<max_it):
    robot_pos[0], robot_pos[1] =  robot_pos[0]+robot_vel[0]*delta, robot_pos[1]  + robot_vel[1]*delta
    robot_vel = [0, 0]
    for obj in objs:
        robot_vel[0], robot_vel[1] = (robot_vel[0]+ obj.get_force(robot_pos)[0]),(robot_vel[1]+ obj.get_force(robot_pos)[1])
    it += 1
    path.append((robot_pos[0],robot_pos[1]))


result = "LigneBrisée("
for element in path:
    result +=str(tuple(element))+","

result = result[:-1]+ ")"
print(result)
print("nb it : ",it)
