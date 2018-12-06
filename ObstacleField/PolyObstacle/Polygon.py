from math import exp, hypot, isclose, atan2, cos, sin, pi

class Polygon:
    def __init__(self, poly, alpha=0.001, beta=1):
        self.poly = poly
        self.alpha = alpha
        self.beta = beta
        self.center = [0, 0]
        for x,y in poly:
            self.center[0] += x/len(poly)
            self.center[1] += y/len(poly)
        self.poly = [self.poly[-1]] + self.poly + [self.poly[0]]
        

    def get_force(self, position):
        x_ext , y_ext = position
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
            #print(distance_du_mur)
            if(0<projection<hypot(*cote) and distance_du_mur>=0):
                #print(distance_du_mur)
                vect = [sin(atan2(cote[1], cote[0])), -1*cos(atan2(cote[1], cote[0]))]
                if isclose(0,distance_du_mur, abs_tol=0.1):
                    return [self.beta*vect[0], self.beta*vect[1]]
                return [exp(-1*distance_du_mur*self.alpha)*self.beta*vect[0], exp(-1*distance_du_mur*self.alpha)*self.beta*vect[1]]
        
        if distances_mur[0]*distances_mur[1]>0 and distances_mur[0]<0:
            # if point is on polygon
            vect = [ (x_ext - self.center[0]),  (y_ext - self.center[1])]
            return [self.beta* vect[0]/hypot(*vect), self.beta* vect[1]/hypot(*vect)]
        vect = [ (x_ext - self.poly[min_i][0]),  (y_ext - self.poly[min_i][1])]
        vect = [vect[0]/hypot(*vect), vect[1]/hypot(*vect)]
        return [vect[0]*exp(-distance_min*self.alpha)*self.beta,vect[1]*exp(-distance_min*self.alpha)*self.beta]

if __name__ == '__main__':
    poly = Polygon( [( 1000,1000), (1600,1000),(1600,1100), (1000,1100)], alpha=0.01, beta=1)
    print(poly.get_force((1300,1000)))

