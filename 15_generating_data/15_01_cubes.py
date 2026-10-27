'''

Raymond Nault
Chapter 15: Generating Cubes

'''

# code will generate and display a chart of cubes of numbers

import matplotlib.pyplot as plt
cubes = [1, 8, 27, 64, 125]
fig, ax = plt.subplots()
ax.plot(cubes, linewidth=3)

# chart title and axis labels
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# tick label size
ax.tick_params(labelsize=14)

plt.show()