import numpy as np
import matplotlib.pyplot as plt
import matplotlib


colors = ["orange", "blue"]
x = [1, 0 , -1, 3, 2, 2]
y = [-1, 0, 1, 2, 2, 3]

color_indices = [0, 0, 0, 1, 1, 1]
colormap = matplotlib.colors.ListedColormap(colors)

plt.scatter(x, y, c=color_indices, cmap=colormap)
plt.grid()
plt.show()



