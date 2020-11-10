import matplotlib.pyplot as plt

# Original input
x = [2, 7, 7, 2, 2]
y = [2, 2, 7, 7, 2]

# For scaling input
sx = 5
sy = 7

# Result for x and y
dx = [0, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 0]


for i in range(len(x)):
    dx[i] = x[i]*sx

for i in range(len(y)):
    dy[i] = y[i]*sy

print(dx)
print(dy)
plt.plot(x, y)
plt.plot(dx, dy)
plt.show()
