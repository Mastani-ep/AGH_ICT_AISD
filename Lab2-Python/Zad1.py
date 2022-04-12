divide = []
ciag = ''
# szukanie liczb podzielnych przez 7 i niepodzielnych przez 5
for i in range(500, 3001):
    if i % 7 == 0 and i % 5 != 0:
        divide.append(i)
print(divide)

# tworzenie stringa z znalezionych liczb
for i in range(len(divide)):
    ciag += str(divide[i])
print(ciag)

# podmienianie '21' na 'XX'
liczba = ciag.count('21')
print("Liczba wystapien '21': ", liczba)
ciag = ciag.replace('21', 'XX', liczba)
print("Po podmienieniu: ", ciag)

