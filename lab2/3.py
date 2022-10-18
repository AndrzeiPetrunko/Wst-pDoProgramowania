print("1)Dodawanie ""\n""2)Odejmowanie""\n""3)Mnożenie""\n""4)Dzielenie""\n""5)Potęgowanie")
try:
    x = float(input("Pierwsza liczba: "))
except:
    print("Podana wartość nie jest liczbą")
    exit()
try:
    y = float(input("Dryga liczba: "))
except:
    print("Podana wartość nie jest liczbą")
    exit()
oper = int(input("Wybierz numer operację: "))
if oper ==  1:
    print("Rezultat:",x + y)
if oper ==  2:
    print("Rezultat:",x - y)
if oper ==  3:
    print("Rezultat:",x * y)
if oper == 4 and y == 0:
    print("BŁĄD")
    exit()
if oper ==  4:
    print("Rezultat:",x / y)
if oper ==  5:
    print("Rezultat:",x ** y)
else:
    print("Taka operacja nie istnie")