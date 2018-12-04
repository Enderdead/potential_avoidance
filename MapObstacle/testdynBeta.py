import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.animation as animation
from Map import *
import pymp
betas = [5,2,1,0.5,0.1,0.05,0.01,0.005,0.001,0.0005,0.0001]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data.
X = np.arange(0, 2000, 10)
Y = np.arange(0, 3000, 10)
X, Y = np.meshgrid(X, Y)
Zs = [np.zeros_like(X,dtype=np.float) for i in range(len(betas))]
maps = [ Map(3000,2000,0.01,beta) for beta in betas]
with pymp.Parallel(4) as p:
    for beta in range(len(betas)):
        for i in range(X.shape[0]):
            for k in range(X.shape[1]):
                Zs[beta][i,k] = maps[beta].get_force((X[i,k],Y[i,k]))


def update_plot(frame_number, zarray, plot):
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, zarray[frame_number], cmap="magma")
    ax.set_title("beta : "+ str(betas[frame_number]))


plot = [ax.plot_surface(X, Y, Zs[0], color='0.75', rstride=1, cstride=1)]
ax.set_zlim(0,np.max(np.concatenate(Zs)))
animate = animation.FuncAnimation(fig, update_plot, len(betas), fargs=(Zs, plot),interval=1000)
plt.show()