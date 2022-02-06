import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# unit step function
def step_func(x):
    if(x > 0):
        return 1
    return 0


def fit(X, y, iters, eta):
    # training the data
    m,n = X.shape
    w = np.zeros((n+1,1))
    err_rate = []
    for i in range(iters):
        err = 0
        for a, b in enumerate(X):
            b = np.insert(b, 0, 1).reshape(-1,1)

            # Calculating prediction/hypothesis.
            y_h = step_func(np.dot(b.T,w))
            # Updating if the example is misclassified.
            if (y_h - y[a]) != 0:
                w += ( eta * ((y[a] - y_h) * b))
    
    return w


colors = ["orange", "blue"]
X = np.array([[1, -1], [0, 0], [-1, 1], [3, 2], [2, 2], [2, 3]])
color_indices = [0, 0, 0, 1, 1, 1]
colormap = matplotlib.colors.ListedColormap(colors)
x1 = [min(X[:,0]), max(X[:,0])]
print(x1)
w = fit(X,color_indices,10, 0.5)
x2 = -w[1]/w[2]
c = -w[0]/w[2]
x2 = x2*x1 + c

plt.scatter(X[:,0], X[:,1], c=color_indices, cmap=colormap)
plt.grid()
print(x1)
print(x2)
plt.plot(x1, x2, 'y-')
plt.show()