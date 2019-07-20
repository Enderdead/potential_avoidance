# Potential Avoidance
This little library implements the potential avoidance algorithm using numpy and matplotlib. You can create easily and quickly your field with many types of objects. Computing a path and display it are also available on this release. 

An example with complet field displaying on matplotlib.
<p align="center">
  <img src="https://user-images.githubusercontent.com/22777836/61185241-4ca8b080-a657-11e9-9579-201851272c95.gif">
</p>

## Quickstart
You need first to create your field and add some obstacles.
```python
# Create field obj
field = Field()

# Add field limit
field.add_object(LimitObstacle( 2000,3000 ))

# Add your destination with a PointObstacle
# Don't forget to setup your force negative to attract.
field.add_object(Point(*target,funct_list["exp"](alpha=0.001,beta=-20)))

# Add obstacle on the robot path
poly = [ (1700,2000), (950,1800),(1100,1500),(1300,1300),]
field.add_object(Polygon(poly))

# Then, compute the path 
path, _ = compute(field, (1100,90),(1000, 2680), max_it=1000)

# And finaly plot it
plot_scalar(field, (0,2000),(0,3000), path=path)
```
Result :

<p align="center">
  <img src="https://user-images.githubusercontent.com/22777836/61579193-9afbfa80-ab02-11e9-822a-9b8140362c49.png">
</p>


## Field model
You can find 3 basic object model introduced just bellow.
### Dot
The most basic object, it's only a punctual source. You can use it as a destination in your field.

<table>
        <tr>
            <td><img src="https://user-images.githubusercontent.com/22777836/61188365-39f5a200-a67e-11e9-9318-7c5a35bee499.png" width="600px"></td>
            <td><img src="https://user-images.githubusercontent.com/22777836/61188366-3bbf6580-a67e-11e9-94d9-8bc669637100.png" width="100%"></td>
        </tr>
</table>

### Polygon
Polygon object can be used as an obstacle on your field. 
<table>
        <tr>
            <td><img src="https://user-images.githubusercontent.com/22777836/61579004-79e5da80-aaff-11e9-9b94-58dd0099d2ad.png" width="600px"></td>
            <td><img src="https://user-images.githubusercontent.com/22777836/61578952-80c01d80-aafe-11e9-9eee-5a2abdc63fd2.png" width="600px"></td>
        </tr>
</table>

###  Limit field
This object can help you to limit your robot's playground.
<table>
        <tr>
            <td><img src="https://user-images.githubusercontent.com/22777836/61579005-82d6ac00-aaff-11e9-84fc-7899e1768130.png" width="600px"></td>
            <td><img src="https://user-images.githubusercontent.com/22777836/61578948-7e5dc380-aafe-11e9-961c-afd4541079c6.png" width="600px"></td>
        </tr>
</table>


## Potentials functions

Three functions are available on this lib. Logarithm, Linear, and Exponential can be found at package Field.funct .
You can see them on the following graph.
<p align="center">
<img src="https://user-images.githubusercontent.com/22777836/61188191-dc605600-a67b-11e9-8ece-9189ec2d44b3.png" alt="drawing" width="60%" />
</p>


## Installation 
Just use the setup script available on the root. You just have to run it like this : 
```bash 
python3 setup.py install --user
```
