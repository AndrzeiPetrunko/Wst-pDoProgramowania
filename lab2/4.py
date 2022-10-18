x = input("Litera: ")
if len(x) > 1 or len(x) == 0:
    print("Wprowadzono za dużo lub za mało liter")
    exit()
n = ord("a") - ord("A")
if 'a' <= x <= 'z':
    print(chr(ord(x) - n))
elif 'A' <= x <= 'Z':
    print(chr(ord(x) + n))
else:
    print("To nie jest litera")




