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


Roots = []
# przygotowanie struktury z rysunku 1
real_insert(1.5)
real_insert(1.3)
real_insert(1.6)
real_insert(3.5)
real_insert(3.7)
real_insert(4.5)
real_insert(4.0)
real_insert(4.99)
real_insert(7.5)
real_insert(7.3)
real_insert(7.8)
real_insert(7.7)
real_insert(7.9)
real_insert(7.6)
real_insert(9.5)
real_insert(9.3)
real_printTree()
print("Zaczynamy prezentacje")
print("Wstawianie elementów (insert)")
# prezentacja funkcji
# wstawianie 3 elementów
real_insert(0.76)
real_insert(0.34)
real_insert(9.1)
real_insert(3.4)
real_insert(7.98)
real_insert(4.7)
real_insert(9.6)
real_printTree()
print("Wyszukiwanie elementu")
print("Czy w strukturze jest 7.6? :", real_search(7.6))
print("Czy w strukturze jest 4.1? :", real_search(4.1))
print("Szukanie maksimum")
print("Maksimum w drzewie o korzeniu 7.5:", real_maximum(7.5))
print("Maksimum w drzewie o korzeniu 4.5:", real_maximum(4.5))
print("Szukanie minimum")
print("Minimum w drzewie o korzeniu 7.5:", real_minimum(7.5))
print("Minimum w drzewie o korzeniu 9.5:", real_minimum(9.5))