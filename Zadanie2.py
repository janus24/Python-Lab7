print("Odczyt liczb z pliku \n")

file = open("liczby.txt", "r")
print(file.read())
file.close()