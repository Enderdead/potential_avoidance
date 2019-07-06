
class Obstacle():
    def get_force(self, x, y):
        raise NotImplementedError()
    
    def get_potential(self, x, y):
        raise NotImplementedError()

class Field:
    """
    Store all Obstacle and compute all forces
    """
    def __init__(self):
        self.objects = list()
    
    def get_force(self, x, y):
        # Get vector 
        vec_force = [0, 0]
        for obj in self.objects:
            vec_force[0], vec_force[1] = (vec_force[0]+ obj.get_force(x, y)[0]),(vec_force[1]+ obj.get_force(x, y)[1])
        return vec_force

    def get_potential(self, x, y):
        potential = 0
        for obj in self.objects:
            potential +=  obj.get_potential(x, y)
        return potential
    
    def add_object(self, obj):
        if not isinstance(obj, Obstacle):
            raise TypeError()
        self.objects.append(obj)