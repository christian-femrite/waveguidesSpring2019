from mpl_toolkits.mplot3d import Axes3D

#matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors 
import time

# Set constants
H0 = 10
a = 2
b = 5
w = 10*(10**6)
beta = 200
max_t = 0.01
delta_t = 0.1*10**(-3)
delta_x = 0.1
delta_y = 0.1
delta_z = 0.1
waveguide_length = 5


# Define plot features
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Linear spaced (x,y,z) data
x = np.arange(0,a,delta_x)
y = np.arange(0,b,delta_y)
z = np.arange(0,waveguide_length,delta_z)
t = np.arange(0,max_t,delta_t)

# Data for three-dimensional scattered points
Hz = np.zeros([x.shape[0],z.shape[0],t.shape[0]])
Hz_colors = np.zeros([x.shape[0],z.shape[0],t.shape[0]])

for ix,x_val in np.ndenumerate(x):
    for iz,z_val in np.ndenumerate(z):
        for it,t_val in np.ndenumerate(t):
            Hz[ix,iz,it] = H0*np.cos(np.pi/a*x_val)*np.cos(w*t_val-beta*z_val)
            Hz_colors[ix,iz,it] = Hz[ix,iz,it]/H0



for ix,x_val in np.ndenumerate(x):
    for iz,z_val in np.ndenumerate(z):
        ax.scatter3D(x_val, 3, z_val, c=Hz[ix,iz,1], cmap = 'Greens')

# Display the 3D plot
plt.show()