import matplotlib.pyplot as plt
# DDA algorithm implementation using python


def DDA(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    print("\ndx = ", dx, "dy =", dy)

    # numstep determination
    if(dx > dy):
        numstep = dx
    else:
        numstep = dy

    print("\nNumstep =", numstep)

    # x and y incrementation
    x_inc = dx/numstep
    y_inc = dy/numstep

    x = x1
    y = y1
    x_plt = [x1]
    y_plt = [y1]

    # print("\n\nWithout using round function")
    # print ('x = %s, y = %s' % ((x),(y)))
    # plt.plot(x,y)
    # for i in range(0,numstep):
    #     x+=x_inc
    #     y+=y_inc
    #     print ('x = %s, y = %s' % ((((x),(y)))))
    #     # print ('x = %s, y = %s' % (((x,y))))
    #     x_plt.append(x)
    #     y_plt.append(y)
    # plt.plot(x_plt,y_plt)

    print("\n\nAfter using round function")
    print ('x = %s, y = %s' % (((round(x),round(y)))))
    plt.plot(x,y)
    for i in range(0,numstep):
        x+=x_inc
        y+=y_inc
        print ('x = %s, y = %s' % (((round(x),round(y)))))
        # print ('x = %s, y = %s' % (((x,y))))
        x_plt.append(x)
        y_plt.append(y)
    plt.plot(x_plt,y_plt)



x1 = int(input("Enter x1 pixel value: "))
y1 = int(input("Enter y1 pixel value: "))
x2 = int(input("Enter x2 pixel value: "))
y2 = int(input("Enter y2 pixel value: "))

DDA(x1,y1,x2,y2)
plt.title("Straight line added using DDA algorithm")
plt.show()