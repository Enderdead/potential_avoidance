from PotAvoidance.field.Polygon import * 
from PotAvoidance.field.Point import * 
from PotAvoidance.field.funct import *
from PotAvoidance.field.Field import * 
from PotAvoidance.path.compute import compute
from PotAvoidance.utils.eval import *
from PotAvoidance.view.scalar import plot_scalar
from PotAvoidance.view.vector import plot_vector

# Create field obj
field = Field()

field.add_object(LimitObstacle( 2000,3000 ))# , funct_list["exp"](alpha=0.01, beta=10)))
field.add_object(Point(1000, 2680,funct_list["exp"](alpha=0.001,beta=-20)))
poly = ((1700,2000), (950,1800),(1100,1500),(1300,1300))
field.add_object(Polygon(poly))#,funct_list["exp"](alpha=0.005, beta=10)))

path, _ = compute(field, (1100,90),(1000, 2680), max_it=1000)
plot_scalar(field, (0,2000),(0,3000), path=path)