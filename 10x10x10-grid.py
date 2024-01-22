import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for each axis
x_range = 10
y_range = 10
z_range = 10

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate grid points and annotations
x, y, z, s = [], [], [], []
i = 0
for ix in range(x_range):
    for iy in range(y_range):
        for iz in range(z_range):
            x.append(ix)
            y.append(iy)
            z.append(iz)
            if i % 2 == 0:  # Check if 'i' is even
                s.append(str(i))
            else:
                s.append("")  # Empty string for odd numbers
            i += 1

# Plot the points
scatter = ax.scatter(x, y,
