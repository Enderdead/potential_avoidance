from math import hypot

def compute(fields, start, target, max_it=500, tol=10):
    path = list()
    it = 0 
    robot_pos = list(start)
    robot_vel = [0, 0]
    while(hypot(robot_pos[0]-target[0], robot_pos[1]- target[1])>tol and it<max_it):
        robot_pos[0], robot_pos[1] =  robot_pos[0]+robot_vel[0], robot_pos[1]  + robot_vel[1]
        robot_vel = [0, 0]
        for obj in fields.objects:
            robot_vel[0], robot_vel[1] = (robot_vel[0]+ obj.get_force(*robot_pos)[0]),(robot_vel[1]+ obj.get_force(*robot_pos)[1])
        it += 1
        path.append((robot_pos[0],robot_pos[1]))

    return path, it

