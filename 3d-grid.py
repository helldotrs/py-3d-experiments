2# Importing necessary libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setting the range for each axis
x_range = 3
y_range = 3
z_range = 2

# Deciding whether to show even and odd numbers
show_even_numbers = True
show_odd_numbers = True

# Creating a 3D plot
fig = plt.figure()  # Creates a new figure for plotting
ax = fig.add_subplot(111, projection='3d')  # Adds a 3D subplot

# Preparing lists to store coordinates and labels
x_coordinates = []
y_coordinates = []
z_coordinates = []
labels = []

# Counter for generating numbers at each point
counter = 0

# Generating points in the 3D space
for ix in range(x_range):
    for iy in range(y_range):
        for iz in range(z_range):
            # Adding the current point's coordinates to the lists
            x_coordinates.append(ix)
            y_coordinates.append(iy)
            z_coordinates.append(iz)

            # Deciding whether to add a label based on even/odd preference
            if (counter % 2 == 0 and show_even_numbers) or (counter % 2 != 0 and show_odd_numbers):
                labels.append(str(counter))
            else:
                labels.append("")  # Leave the label empty if not showing the number

            # Incrementing the counter for the next point
            counter += 1

# Plotting the points on the graph
scatter = ax.scatter(x_coordinates, y_coordinates, z_coordinates)

# Annotating each point with its label
for i in range(len(x_coordinates)):
    if labels[i]:  # Only annotate points that have a label
        ax.text(x_coordinates[i], y_coordinates[i], z_coordinates[i], labels[i], size=10, zorder=1, color='k')

# Setting labels for each axis
ax.set_
