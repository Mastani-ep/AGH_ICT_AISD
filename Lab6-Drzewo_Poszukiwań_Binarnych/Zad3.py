from random import randint
import time


class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printTree(self, x="", level=0):
        if self.left and self.right:
            self.left.printTree(x + "-" * level + str(self.value), level + 1)
            self.right.printTree("   " * (level + 1) + " " * level, level + 1)
        elif self.left:
            self.left.printTree(x + "-" * level + str(self.value), level + 1)
        elif self.right:
            self.right.printTree(x + "-" * level + str(self.value), level + 1)
        else:
            print(x +"-" * level + str(self.value))

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Tree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Tree(value)

    def search(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if not self.left:
                return False
            return self.left.search(value)
        elif not self.right:
            return False
        return self.right.search(value)

    def minimum(self):
        if self.left:
            return self.left.minimum()
        else:
            return self.value

    def maximum(self):
        if self.right:
            return self.right.maximum()
        else:
            return self.value


def real_insert(x):
    global Roots
    if x % 1 == 0.5:
        if len(Roots) == 0:
            Roots.append(Tree(x))
        else:
            for i in range(len(Roots)):
                if Roots[i].value == x:
                    break
                elif Roots[i].value > x and i == 0:
                    Roots.insert(i, Tree(x))
                elif i == len(Roots) - 1:
                    Roots.append(Tree(x))
                    break
                elif Roots[i].value < x and Roots[i + 1].value > x:
                    Roots.insert(i + 1, Tree(x))
                    break
    else:
        if len(Roots) == 0:
            Roots.append(Tree(int(x) + 0.5))
            Roots[0].insert(x)
        else:
            for i in range(len(Roots)):
                if Roots[i].value == int(x) + 0.5:
                    Roots[i].insert(x)
                    break
                elif Roots[i].value > int(x) + 0.5 and i == 0:
                    Roots.insert(i, Tree(int(x) + 0.5))
                    Roots[i].insert(x)
                elif i == len(Roots) - 1:
                    Roots.append(Tree(int(x) + 0.5))
                    Roots[i + 1].insert(x)
                    break
                elif Roots[i].value < (int(x) + 0.5) and Roots[i + 1].value > int(x)+0.5:
                    Roots.insert(i + 1, Tree(int(x) + 0.5))
                    Roots[i + 1].insert(x)
                    break


def real_printTree():
    global Roots
    for i in range(len(Roots)):
        Roots[i].printTree()


def real_search(x):
    global Roots
    if x % 1 == 0.5:
        for i in range(len(Roots)):
            if Roots[i].value == x:
                return True
            elif i == len(Roots)-1:
                return False
    else:
        for i in range(len(Roots)):
            if Roots[i].value == (int(x) + 0.5):
                return Roots[i].search(x)
            elif i == (len(Roots) - 1):
                return False


def real_minimum(y):
    global Roots
    for i in range(len(Roots)):
        if Roots[i].value == y:
            return Roots[i].minimum()
        elif i == (len(Roots)-1):
            return False


def real_maximum(y):
    global Roots
    for i in range(len(Roots)):
        if Roots[i].value == y:
            return Roots[i].maximum()
        elif i == (len(Roots)-1):
            return False


# sprawdzamy czasy
# generuje tablice z przykladowymi mozliwymi liczbami
array = []
array_min_max = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
time_insert = []
time_search = []
time_maximum = []
time_minimum = []
average_time_insert = 0
average_time_search = 0
average_time_maximum = 0
average_time_minimum = 0

for i in range(1000):
    array.append(i/100)

for i in range(10000):
    Roots = []
    for j in range(1000):
        real_insert(array[randint(0, 999)])
    start = time.time()
    real_insert(array[randint(0, 999)])
    time_insert.append(time.time()-start)
average_time_insert = sum(time_insert)/10000
print("Sredni czas insert dla 1000 elementow:", average_time_insert)

Roots = []
for j in range(1000):
    real_insert(array[randint(0, 999)])


for i in range(10000):
    start = time.time()
    p = real_search(array[randint(0, 999)])
    time_search.append(time.time() - start)
average_time_search = sum(time_search)/10000
print("Sredni czas search dla 1000 elementow:", average_time_search)

for i in range(10000):
    start = time.time()
    p = real_minimum(array_min_max[randint(0, 9)])
    time_minimum.append(time.time() - start)
average_time_minimum = sum(time_minimum)/10000
print("Sredni czas minimum dla 1000 elementow:", average_time_minimum)

for i in range(10000):
    start = time.time()
    p = real_maximum(array_min_max[randint(0, 9)])
    time_maximum.append(time.time() - start)
average_time_maximum = sum(time_maximum)/10000
print("Sredni czas maximum dla 1000 elementow:", average_time_maximum)
