#pip install matplotlib

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate grid points
x, y, z = [], [], []
i = 0
for ix in range(10):
    for iy in range(10):
        for iz in range(10):
            x.append(ix)
            y.append(iy)
            z.append(iz)
            i += 1

# Plot the points
ax.scatter(x, y, z)

# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the plot
plt.show()
