import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# making new walks, as long as program is active

while True:
    # making random walk
    rw = RandomWalk()
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = list(range(rw.num_points))
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another random walk? (y/n): ")
    if keep_running.lower() != 'y':
        break
    