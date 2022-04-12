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


# funkcje search, minimum, maximum zostaly zaprezentowane w pliku z zad 2
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
print("Prezentacja tekstowej wizualizacji dla danych z rysunku 1")
real_printTree()
real_insert(3.1)
real_insert(2.7)
real_insert(7.4)
real_insert(1.2)
real_insert(2.3)
real_insert(2.4)
real_insert(2.22)
print("Prezentacja tekstowej wizualizacji dla powiekszonego drzewa")
real_printTree()