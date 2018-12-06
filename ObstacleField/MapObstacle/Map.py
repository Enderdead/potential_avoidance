from math import exp, hypot

class Map:
    def __init__(self, length, width, alpha=0.001, beta=1):
        self.length = length
        self.width  = width
        self.alpha = alpha
        self.beta = beta

    def get_force(self, position):
        x , y = position
        wall_vects = ((0, y), (x, 0), (self.width,y), (x,self.length))
        norm_vects = ((1, 0), (0, 1), (-1, 0), (0, -1))
        result = [0,0]
        for (wall_vect, norm_vect) in zip(wall_vects, norm_vects):
            (x_wall, y_wall) = wall_vect
            result[0] +=  exp(-hypot(x_wall-x, y_wall-y)*self.alpha)*self.beta*norm_vect[0]
            result[1] +=  exp(-hypot(x_wall-x, y_wall-y)*self.alpha)*self.beta*norm_vect[1]
        
        return result




