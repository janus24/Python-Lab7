file = open("liczby.txt", "a+")
a = input("Wpisz tekst który chcesz dopisać do pliku: ")
file.writelines(str(a) + " ")
file.close()

with open("liczby.txt", "r") as file:
    for line in file:
        print(line, end="")