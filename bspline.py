import matplotlib.pyplot as plt
import numpy as np


def knot_values(n, k):
    t = np.zeros((1, n+k+1))
    for i in range(0, n+k+1):
        if i < k:
            t[0][i] = 0
        if i >= k and i <= n:
            t[0][i] = i-k+1
        if i > n:
            t[0][i] = n-k+2

    return t


def basis_spline(u, t, i, k):
    if k == 1:
        if u >= t[0][i] and u <= t[0][i+1]:
            sol = 1
        else:
            sol = 0
    else:
        a = (u - t[0][i])*basis_spline(u, t, i, k-1)
        b = t[0][i+k-1] - t[0][i]
        c = (t[0][i+k] - u)*basis_spline(u, t, i+1, k-1)
        d = t[0][i+k] - t[0][i+1]
        if b == 0:
            temp1 = 0
        else:
            temp1 = a/b

        if d == 0:
            temp2 = 0
        else:
            temp2 = c/d

        sol = (temp1) + (temp2)

    return sol


def curve_generator(n, k, ctrl_x, ctrl_y):

    t = knot_values(n, k)
    print(t)
    u = np.arange(t[0][k-1], t[0][n+1], 0.001)
    length = u.shape

    x = np.zeros((1, length[0]))
    y = np.zeros((1, length[0]))

    for i in range(0, n+1):
        for j in range(0, length[0]):
            x[0][j] = x[0][j] + basis_spline(u[j], t, i, k)*ctrl_x[i]
            y[0][j] = y[0][j] + basis_spline(u[j], t, i, k)*ctrl_y[i]

    return x, y


n = 6
k = 3
ctrl_x = np.array([0, 3, 6, 9, 10, 12, 15])
ctrl_y = np.array([0, 4, 2, 3, 7, 8, 5])

[x, y] = curve_generator(n, k, ctrl_x, ctrl_y)

n = x.shape
a = [0]*n[1]
b = [0]*n[1]
for i in range(0, n[1]):
    a[i] = x[0][i]
    b[i] = y[0][i]

plt.plot(ctrl_x, ctrl_y)
plt.show()
