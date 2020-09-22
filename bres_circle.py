# Bressenham's circle drawing algorithm

import matplotlib.pyplot as plt

def bres_circle(x0,y0,r):
    x = 0
    y = r
    
    x_plt = []
    y_plt = []

    print(x,y)


    d = 3-2*r

    while(x<=y):
        if (d<0):
            x+=1
            d = d+4*x+6
        else:
            x+=1
            y-=1
            d = d+5*(x-y)+6
        

        print(x,y)
        x_plt.append(x+x0)
        y_plt.append(y+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(y+x0)
        y_plt.append(x+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(-y+x0)
        y_plt.append(x+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(-x+x0)
        y_plt.append(y+y0)
        plt.scatter(x_plt,y_plt)
        
        x_plt.append(-x+x0)
        y_plt.append(-y+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(-y+x0)
        y_plt.append(-x+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(y+x0)
        y_plt.append(-x+y0)
        plt.scatter(x_plt,y_plt)

        x_plt.append(x+x0)
        y_plt.append(-y+y0)
        plt.scatter(x_plt,y_plt)

bres_circle(50,50,10)
plt.title("Straight line added using Bressenham's Circle Drawing algorithm")
plt.show()