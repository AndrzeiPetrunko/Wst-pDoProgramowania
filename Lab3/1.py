#zadanie_1
a = int(input("Podaj pierwszę liczbę: "))
b = int(input("Podaj drugę liczbę: "))
if a > b:
    a,b = b,a
while (a <= b):
    print(a, end=', ')
    a +=1