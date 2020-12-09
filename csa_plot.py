# import matplotlib.pyplot as plt

# Cohen Sutherland Algorithm for Line Clipping
Inside = 0  # 0000
Left = 1  # 0001
Right = 2  # 0010
Top = 8  # 1000
Bottom = 4  # 0100

# Clip window
x_max = 10
y_max = 8
x_min = 4
y_min = 4


def computeCode(x, y):
    code = Inside
    if x < x_min:
        code |= Left
    elif x > x_max:
        code |= Bottom
    elif y > y_max:
        code |= Top
    return code


def sutherland(x1, y1, x2, y2):
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break

        elif (code1 & code2) != 0:
            break

        else:

            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & Top:

                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & Bottom:

                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & Right:

                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & Left:

                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))

    else:
        print("Line rejected")


sutherland(5, 4, 7, 6)
sutherland(2, 2, 12, 6)
sutherland(5, 6, 12, 7)
sutherland(12, 10, 10, 9)
