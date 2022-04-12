import time
from random import randint
# tworzenie listy
n = 1000
T = [randint(-1000, 1000) for i in range(n)]


# petla na obiekcie iterowanym
def iteration():
    for i in T:
        print(i)


# jak w C++
def c():
    for i in range(len(T)):
        print(T[i])


start = time.time()
c()
x = time.time() - start
start = time.time()
iteration()
print("Czas petli jak w C++: ", x, "Czas petli obiektu iterowanego: ", time.time() - start)
