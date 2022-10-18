x = input("Litera: ")

if len(x) > 1 or len(x) == 0:
    print("Wprowadzono za dużo lub za mało liter")
    exit()
if 'a' <= x <= 'z':
    print("Litera jest mała")
elif 'A' <= x <= 'Z':
    print("Litera jest duża")
else:
    print("To nie jest litera")




