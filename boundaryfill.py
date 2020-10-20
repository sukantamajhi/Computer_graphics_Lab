#Boundary fill algorithm
m = 10
n = 10


def b_fill(screen, x, y, newC, bcolor):
    if(x < 0 or x >= m or y < 0 or y >= n or screen[x][y] == newC or screen[x][y] == bcolor):
        return
    screen[x][y] = newC
    b_fill(screen, x+1, y,  newC, bcolor)
    b_fill(screen, x, y+1,  newC, bcolor)
    b_fill(screen, x-1, y, newC, bcolor)
    b_fill(screen, x, y-1, newC, bcolor)


def fill(screen, x, y, newC):
    prevC = screen[x][y]
    b_fill(screen, x, y, newC, bcolor)


screen = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [0, 1, 2, 2, 2, 2, 2, 1, 1, 0],
          [0, 1, 2, 2, 2, 2, 2, 2, 1, 0],
          [1, 2, 2, 2, 2, 2, 2, 2, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
x = 4
y = 5
newC = 8
bcolor = 1
fill(screen, x, y, newC)
print('After fill')
for i in range(m):
    for j in range(n):
        print(screen[i][j], end='')
    print()
