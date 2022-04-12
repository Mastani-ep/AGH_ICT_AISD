# pozbywanie sie pustych linii
f = open('zadanie2.csv', 'r')
txt = ''
for line in f:
    if line.split(',', 1)[1] != '\n':
        txt += line

# print(txt)
f.close()
f = open('zadanie2.csv', 'w')
f.write(txt)
f.close()

# sortowanie
f = open('zadanie2.csv', 'r')
sort = []
first_line = ''
sorttxt = ''
x = -1
for line in f:
    if x == -1:
        first_line += line
    else:
        sort.append(line)
    x += 1

for i in range(len(sort) - 1, 0, -1):
    for j in range(i):
        if int(sort[j].split(',', 1)[0]) > int(sort[j + 1].split(',', 1)[0]):
            sort[j], sort[j + 1] = sort[j + 1], sort[j]

for i in sort:
    sorttxt += i
f.close()
f = open('zadanie2.csv', 'w')
f.write(first_line)
f.write(sorttxt)
f.close()

# poprawianie indeksow
f = open('zadanie2.csv', 'r')
correct = []
correcttxt = ''
first_line = ''
x = -1
for line in f:
    if x == -1:
        first_line += line
    else:
        correct.append(int(line.split(',', 1)[0]))
    x += 1

n = len(correct)
for i in range(n-1):
    max = correct[i]
    if correct[i] >= correct[i+1]:
        max += 1
        correct[i+1] = max

print(correct)
f.close()
f = open('zadanie2.csv', 'r')
i = -1
for line in f:
    if i == -1:
        pass
    else:
        correcttxt += str(correct[i])+','+line.split(',', 1)[1]
    i += 1
print(correcttxt)
f.close()
f = open('zadanie2.csv', 'w')
f.write(correcttxt)
f.close()

# zamiana duzych liter na male
f = open('zadanie2.csv', 'r')
lower = ''
for line in f:
    lower += line.lower()
print(lower)
f.close()
f = open('zadanie2.csv', 'w')
f.write(lower)
f.close()

f = open('zadanie2.csv', 'r')
remove = 'id,val\n'
for line in f:
    split = line.split(' ')
    remove += split[0].split(',', 1)[0]
    split[0] = split[0].split(',', 1)[1]
    dod = [',']
    for i in split:
        if len(i) < 2:
            pass
        elif ord(i[0]) == ord(i[1])+1 or ord(i[0]) == ord(i[1])-1:
            if i[len(i)-1] == ',' or i[len(i)-1] == '.':
                id = line.split(',', 1)[0]
                print("Usunięto wyraz :", i.split(i[len(i)-1], 1)[0], "z wiersza o indeksie: ", id)
                i = i[len(i)-1]
            elif i[len(i)-1] == '\n':
                id = line.split(',', 1)[0]
                print("Usunięto wyraz :", i.split('.', 1)[0], "z wiersza o indeksie: ", id)
                i = '.\n'
            else:
                id = line.split(',', 1)[0]
                print("Usunięto wyraz :", i, "z wiersza o indeksie: ", id)
                i = ''
        dod.append(i)
    for j in range(len(dod)):
        if j == 0:
            remove += dod[j]
        elif j == 1:
            remove += dod[j]
        elif dod[j] == ',' or dod[j] == '.':
            remove += dod[j]
        elif dod[j] == '':
            pass
        else:
            if j-2 == 0 and dod[j-1] == '' or (j-3 == 0 and dod[j-2] == '' and dod[j-1] == ''):
                remove += dod[j]
            else:
                remove += ' '+dod[j]
print(remove)
f.close()
f = open('zadanie2.csv', 'w')
f.write(remove)
f.close()
