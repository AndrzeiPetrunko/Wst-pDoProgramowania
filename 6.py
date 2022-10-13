#
# To jest prosty kalkulator. Podajcie dwie liczby i numer operację
#
print("1)Dodawanie ""\n""2)Odejmowanie""\n""3)Mnożenie""\n""4)Dzielenie""\n""5)Reszta z dzielenia")
x = int(input("Pierwsza liczba: "))
y = int(input("Dryga liczba: "))
oper = int(input("Wybierz numer operację: "))
if oper ==  1:
    print("Rezultat:",x + y)
if oper ==  2:
    print("Rezultat:",x - y)
if oper ==  3:
    print("Rezultat:",x * y)
if oper ==  4:
    print("Rezultat:",x / y)
if oper ==  5:
    print("Rezultat:",x % y)
if oper != 1 and 2 and 3 and 4 and 5:
    print("Nie możliwo wykonać operację")
