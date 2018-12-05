from math import exp, hypot

class Point:
    def __init__(self, x, y, alpha=0.001, beta=1):
        self.x = x
        self.y = y
        self.alpha = alpha
        self.beta = beta

    def get_force(self, position):
        x_ext , y_ext = position
        result =  exp(-hypot(self.x-x_ext, self.y-y_ext)*self.alpha)*self.beta   
        vect = (x_ext-self.x, y_ext-self.y)  
        vect = vect[0]/hypot(*vect),  vect[1]/hypot(*vect)  
        return (result*vect[0], result*vect[1])
