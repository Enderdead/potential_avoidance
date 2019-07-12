from math import exp, hypot, isclose, atan2, cos, sin, pi
from ..utils.math_tools import *
from .Field import Obstacle
from .funct import Exp



class Polygon(Obstacle):
    def __init__(self, poly, funct):

        self.poly = poly
        self.funct = funct
        self.center = [0, 0]
        for x,y in poly:
            self.center[0] += x/len(poly)
            self.center[1] += y/len(poly)
        if not is_convex_polygon(poly):
            pass # TODO fix
            #raise TypeError("Polygon given isn't convex !")
        if not is_anti_clock_wise(poly):
            raise TypeError("Polygon isn't defined on anti_clock_wise way !")

    def get_potential(self, x_ext, y_ext):
        dist, _ = dist_from_polygon((x_ext, y_ext), self.poly, self.center)
        if dist<0:
            return self.funct.get_max()
        return self.funct.apply(dist)

    def get_force(self, x_ext , y_ext):
        dist, vec = dist_from_polygon((x_ext, y_ext), self.poly, self.center)
        if dist<0:
            return self.funct(vec, dist)
        return self.funct(vec, dist)


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
        for (wall_vect, _) in zip(wall_vects, norm_vects):
            (x_wall, y_wall) = wall_vect
            result  += self.funct.apply(hypot(x_wall-x, y_wall-y))
        return result
