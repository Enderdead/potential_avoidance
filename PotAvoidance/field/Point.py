from math import exp, hypot
from .Field import Obstacle


class Point(Obstacle):
    def __init__(self, x, y, funct):
        self.x = x
        self.y = y
        self.funct = funct

    def get_force(self, x, y):
        x_ext , y_ext = x, y
        vect = (x_ext-self.x, y_ext-self.y)  
        if hypot(*vect) == 0 :
            return [0, 0]
        vect = vect[0]/hypot(*vect),  vect[1]/hypot(*vect)
        return self.funct(vect, hypot(x_ext-self.x, y_ext-self.y))

    def get_potential(self, x, y):
        x_ext , y_ext = x, y
        return self.funct.apply(hypot(x_ext-self.x, y_ext-self.y))
