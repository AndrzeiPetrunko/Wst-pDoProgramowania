pada = input("Czy teraz pada?(Tak lub Nie): ")
autobus = input("Czy jest autobus?(Tak lub Nie): ")
if pada == "Tak" and autobus == "Tak":
    print("Weź parasol""\n""Dostaniesz się na uczelnie")
elif pada == "Tak" and autobus == "Nie":
    print("Nie dostaniesz się na uczelnię")
elif pada == "Nie" and autobus == "Tak":
    print("Dostaniesz się na uczelnie""\n""Miłego dnia i pięknej pogody")