literka = input("Literka lub zdanie: ")
x = 0
nowy = ""
for i in range(len(literka)):
    if literka[x] == literka[x].lower():
        nowy += literka[x].upper()
        x += 1
    elif literka[x] == literka[x].upper():
        nowy += literka[x].lower()
        x += 1
print(nowy)