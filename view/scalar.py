import numpy as np 
from field.Field import Field
from collections.abc import Iterable
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pymp

def plot_scalar(field, x_lim, y_lim, step=10, path=None):
    if not isinstance(field, Field):
        raise TypeError("fied must be a Field object !")

    if not isinstance(x_lim, Iterable):
        raise TypeError("x_lim must be a iterable")
    if len(x_lim)!=2:
        raise TypeError("x_lim must get 2 elements")

    if not isinstance(y_lim, Iterable):
        raise TypeError("y_lim must be a iterable")
    if len(y_lim)!=2:
        raise TypeError("y_lim must get 2 elements")


    # Make data.
    X = np.arange(*x_lim, step, dtype =np.float32)
    Y = np.arange(*y_lim, step, dtype =np.float32)
    X, Y = np.meshgrid(X, Y)
    Z = np.zeros_like(X, dtype=np.float32)

    #with pymp.Parallel(4) as p:
    for i in range(X.shape[0]):
        for k in range(X.shape[1]):
            for obj in field.objects:
                Z[i,k] += obj.get_potential(*[float(X[i,k]), float(Y[i,k])] )



    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    if not path is None:
        path_x = np.array([element[0] for element in path], dtype=np.float32)
        path_y = np.array([element[1] for element in path], dtype=np.float32)

        path_z = np.zeros_like(path_x, dtype=np.float32)
        for i in range(path_x.shape[0]):
            for obj in objs:
                path_z[i] += obj.get_potential(*[float(path_x[i]), float(path_y[i])])


        ax.plot(path_x, path_y, path_z, color="black")

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    plt.show()