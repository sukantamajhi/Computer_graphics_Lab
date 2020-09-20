import matplotlib.pyplot as plt
def bressenham(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1

    x_plt = []
    y_plt = []

    p_not = 2*dy - dx

    x = x1
    y = y1

    print(x,y)
    
    plt.plot(x,y)

    if dx>dy:
        k = dx
    else:
        k = dy

    for i in range(k):
        if p_not<0:
            x1 += 1
            p_not = p_not+2*dy
        else:
            x1 += 1
            y1 += 1
            p_not = p_not+2*dx-2*dy

        print(x1,y1)
        x_plt.append(x1)
        y_plt.append(y1)
        plt.plot(x_plt,y_plt)

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

bressenham(x1,y1,x2,y2)
plt.show()