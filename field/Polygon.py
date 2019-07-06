from math import exp, hypot, isclose, atan2, cos, sin, pi
from field.Field import Obstacle
from field.funct import Exp
class Polygon(Obstacle):
    def __init__(self, poly, funct):
        self.poly = poly
        self.funct = funct
        self.center = [0, 0]
        for x,y in poly:
            self.center[0] += x/len(poly)
            self.center[1] += y/len(poly)
        self.poly = [self.poly[-1]] + self.poly + [self.poly[0]]
        
    def get_potential(self, x_ext, y_ext):
        min_i = -1
        distance_min = 60000
        for i in range(1,len(self.poly)-1):
            x, y = self.poly[i]
            distance = hypot(x-x_ext, y-y_ext)
            if distance<distance_min:
                distance_min = distance
                min_i = i

        distances_mur = [0,0]
        for k in range(2):
            x1, y1 = self.poly[min_i-1+k]
            x2, y2 = self.poly[min_i+k]
            cote = (x2-x1 , y2-y1)
            robot = (x_ext-x1, y_ext-y1)
            scalaire = robot[0]*cote[0] + robot[1]*cote[1]
            projection = scalaire/hypot(*cote)
            distance_du_mur = (robot[0]*cote[1] - cote[0]*robot[1])/hypot(*cote)
            distances_mur[k] = distance_du_mur
            if(0<=projection<=hypot(*cote) and distance_du_mur>=0):
                vect = [sin(atan2(cote[1], cote[0])), -1*cos(atan2(cote[1], cote[0]))]
                if isclose(0,distance_du_mur, abs_tol=0.1):
                    return self.funct.get_max()
                return self.funct.apply(distance_du_mur)
        
        if distances_mur[0]*distances_mur[1]>0 and distances_mur[0]<0:
            # if point is on polygon
            vect = [ (x_ext - self.center[0]),  (y_ext - self.center[1])]
            #TODO 
            #vect = [vect[0]/hypot(*vect), vect[1]/hypot(*vect)] 
            return self.funct.get_max()
        vect = [ (x_ext - self.poly[min_i][0]),  (y_ext - self.poly[min_i][1])]
        vect = [vect[0]/hypot(*vect), vect[1]/hypot(*vect)]
        return self.funct.apply(distance_min)


    def get_force(self, x_ext , y_ext):
        min_i = -1
        distance_min = 60000
        for i in range(1,len(self.poly)-1):
            x, y = self.poly[i]
            distance = hypot(x-x_ext, y-y_ext)
            if distance<distance_min:
                distance_min = distance
                min_i = i

        distances_mur = [0,0]
        for k in range(2):
            x1, y1 = self.poly[min_i-1+k]
            x2, y2 = self.poly[min_i+k]
            cote = (x2-x1 , y2-y1)
            robot = (x_ext-x1, y_ext-y1)
            scalaire = robot[0]*cote[0] + robot[1]*cote[1]
            projection = scalaire/hypot(*cote)
            distance_du_mur = (robot[0]*cote[1] - cote[0]*robot[1])/hypot(*cote)
            distances_mur[k] = distance_du_mur
            if(0<=projection<=hypot(*cote) and distance_du_mur>=0):
                vect = [sin(atan2(cote[1], cote[0])), -1*cos(atan2(cote[1], cote[0]))]
                if isclose(0,distance_du_mur, abs_tol=0.1):
                    return self.funct.saturate(vect)
                return self.funct(vect, distance_du_mur)
        
        if distances_mur[0]*distances_mur[1]>0 and distances_mur[0]<0:
            # if point is on polygon
            vect = [ (x_ext - self.center[0]),  (y_ext - self.center[1])]
            vect = [vect[0]/hypot(*vect), vect[1]/hypot(*vect)] 
            return self.funct.saturate(vect)
        vect = [ (x_ext - self.poly[min_i][0]),  (y_ext - self.poly[min_i][1])]
        vect = [vect[0]/hypot(*vect), vect[1]/hypot(*vect)]
        return self.funct(vect, distance_min)




class LimitObstacle(Obstacle):
    def __init__(self, width, length, funct=Exp(alpha=0.01, beta=10)):
        self.length = length
        self.width  = width
        self.funct = funct

    def get_force(self, x, y):
        wall_vects = ((0, y), (x, 0), (self.width,y), (x,self.length))
        norm_vects = ((1, 0), (0, 1), (-1, 0), (0, -1))
        result = [0,0]
        for (wall_vect, norm_vect) in zip(wall_vects, norm_vects):
            (x_wall, y_wall) = wall_vect
            result[0] +=  self.funct(norm_vect, hypot(x_wall-x, y_wall-y))[0]
            result[1] +=  self.funct(norm_vect, hypot(x_wall-x, y_wall-y))[1]
        return result

    def get_potential(self, x, y):
        wall_vects = ((0, y), (x, 0), (self.width,y), (x,self.length))
        norm_vects = ((1, 0), (0, 1), (-1, 0), (0, -1))
        result = 0
        for (wall_vect, norm_vect) in zip(wall_vects, norm_vects):
            (x_wall, y_wall) = wall_vect
            result  += self.funct.apply(hypot(x_wall-x, y_wall-y))
        return result
