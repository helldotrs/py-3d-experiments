import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate grid points and annotations
x, y, z, s = [], [], [], []
i = 0
for ix in range(10):
    for iy in range(10):
        for iz in range(10):
            x.append(ix)
            y.append(iy)
            z.append(iz)
            if i % 2 == 0:  # Check if 'i' is even
                s.append(str(i))
            else:
                s.append("")  # Empty string for odd numbers
            i += 1

# Plot the points
scatter = ax.scatter(x, y, z)

# Annotate each point
for i in range(len(x)):
    if s[i]:  # Only annotate if the string is not empty
        ax.text(x[i], y[i], z[i], s[i], size=10, zorder=1, color='k')

# Set labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Show the plot
plt.show()
