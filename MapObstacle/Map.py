from math import exp, hypot

class Map:
    def __init__(self, length, width, alpha=0.001, beta=0):
        self.length = length
        self.width  = width
        self.alpha = alpha
        self.beta = beta

    def get_force(self, position):
        x , y = position
        wall_vect = ((0, y), (x, 0), (self.width,y), (x,self.length))
        result = 0
        for (x_wall, y_wall) in wall_vect:
            result += exp(-hypot(x_wall-x, y_wall-y)*self.alpha)*self.beta
        
        return result




