#zadanie_4
a = int(input("Podaj pierwszę liczbę: "))
b = int(input("Podaj drugę liczbę: "))
if a > b:
    a,b = b,a
while (a <= b):
    if a % 2:
        a += 1
        continue
    else:
        print(a, end=', ')
        a += 1