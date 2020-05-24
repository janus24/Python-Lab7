print("Zapisywanie liczb podzielnych przez 4")

file = open("liczby.txt", "w")
for i in range(1, 40 + 1):
    if i % 4 == 0:
        file.write(str(i) + " ")

file.close()