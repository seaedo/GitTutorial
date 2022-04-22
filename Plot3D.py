# import plot libraries libraries
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# import numpy linear algebra library
import numpy as np
 
# create figure and set it to 3d projection
fig = plt.figure()
ax = fig.gca(projection='3d')
 
# 1D arrays for x and y coordinates
n_points = 500
x_min,x_max = -5,5
y_min,y_max = -5,5
X = np.linspace(x_min,x_max, n_points)
Y = np.linspace(y_min,y_max, n_points)
 
# 2D X,Y grids from 1D arrays
X, Y = np.meshgrid(X, Y)
 
# Z 2D grid for the plot
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
 
# plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap='viridis',linewidth=0, antialiased=True)
 
# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
 
# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)
 
# plot
plt.show()
