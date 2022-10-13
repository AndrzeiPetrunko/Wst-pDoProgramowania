x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
if x < y and y < z:
    print(x, " -> ", y, " -> ", z)
elif x < z and z < y:
    print(x, " -> ", z, " -> ", y)
elif y < z and z < x:
    print(y, " -> ", z, " -> ", x)
elif z < x and x < y:
    print(z, " -> ", x, " -> ", y)
elif y < x and x < z:
    print(y, " -> ", x, " -> ", z)
elif z < y and y < x:
    print(z, " -> ", y, " -> ", x)
elif x == y or x == z or z == y:
    print("Dwie lub trzy liczby są takie same :(")

