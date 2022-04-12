import time


# funkcja sortujaca
def sort(tab):
    for i in range(len(tab) - 1, 0, -1):
        for j in range(i):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]


# funkcja sprawdzajaca powtarzanie sie elementow
def repeat(tab):
    repeat = []
    a = False
    for x in range(len(tab)):
        k = tab[x]
        tab.remove(tab[x])
        if k in tab:
            if k in repeat:
                pass
            else:
                print("Powtarza się: ")
                print(k)
            repeat.append(k)
            a = True
        tab.append(k)
        sort(tab)
    if a == 0:
        print("Żadna liczba nie powtarza się więcej niż jeden raz.")


# funkcja powiekszajaca liste
def extend(tab, q):
    for x in range(q):
        tab.append((tab[x]+tab[x+1])/(tab[x+1]-tab[x]))


# funkcja liczaca srednia
def average(tab):
    average = sum(tab)/len(tab)
    print("Średnia: ", average)


# funkcja liczaca miedane
def median(tab):
    sort(tab)
    if len(tab) % 2 == 0:
        med = (tab[(len(tab)//2)]+tab[(len(tab)//2)-1])/2
    else:
        med = tab[(len(tab)//2)]
    print("Mediana: ", med)


start = time.time()
L = [1, 2]
extend(L, 46)
print(L)
average(L)
median(L)
repeat(L)
x = time.time() - start
print("Czas działania programu przy liscie: ", x)
