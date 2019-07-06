from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def plot_vector(field, x_lim, y_lim, step=20, path=None):


    x_step = abs(x_lim[0]-x_lim[1])//step
    y_step = abs(y_lim[0]-y_lim[1])//step
    # Make data.
    X = np.arange(*x_lim, x_step, dtype =np.float32)
    Y = np.arange(*y_lim, y_step, dtype =np.float32)
    X, Y = np.meshgrid(X, Y)
    U = np.zeros_like(X,dtype=np.float32)
    V = np.zeros_like(X,dtype=np.float32)

    for i in range(X.shape[0]):
        for k in range(X.shape[1]):
            for obj in field.objects:
                U[i,k] += obj.get_force(*[float(X[i,k]), float(Y[i,k])])[0]
                V[i,k] += obj.get_force(*[float(X[i,k]), float(Y[i,k])])[1]

    fig, ax = plt.subplots()

    q = ax.quiver(X, Y, U, V)


    plt.show()