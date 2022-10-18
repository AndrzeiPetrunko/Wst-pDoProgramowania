x = int(input("Wprowadź wiek klienta:"))
if x < 4:
    print("Cena biletu: Bezpłatny")
elif x > 4 and x < 18:
    print("Cena biletu: 10zł")
elif x > 18:
    print("Cena biletu: 20zł")