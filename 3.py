from math import sqrt
a = float(input())
b = float(input())
c = float(input())
dis = b ** 2 - 4 * a * c
if dis > 0:
    x_1 = (-b - sqrt(dis))/2*a
    x_2 = (-b + sqrt(dis))/2*a
    print("solution:", x_1, "and", x_2)
elif dis == 0:
    x = -b / 2 * a
    print("solution:", x)
else:
    print ("there's no solution")

