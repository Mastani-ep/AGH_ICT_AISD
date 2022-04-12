from random import randint
import time

class Package:
    def __init__(self, a, b, c, d):
        self.id = a
        self.width = b
        self.height = c
        self.value = d
        self.den_val = d/(b*c)


f = open('packages1000.txt', 'r')
i = 0
packages = []
for line in f:
    if i <= 1:
        i += 1
    else:
        packages.append(Package(int(line.split(',', 4)[0]), int(line.split(',', 4)[1]), int(line.split(',', 4)[2]), int(line.split(',', 4)[3])))
f.close()


sorter = lambda x: (x.den_val)
packages = sorted(packages, key=sorter, reverse=True)

z = 1000
knapsack = [z for i in range(z)]
knapsack_value = 0
for i in range(len(packages)):
    put = False
    for j in range(z - packages[i].height + 1):
        poss = True
        for k in range(packages[i].height):
            if knapsack[j+k] < packages[i].width:
                poss = False
                break
        if poss:
            put = True
            knapsack_value += packages[i].value
            for k in range(packages[i].height):
                knapsack[j + k] -= packages[i].width
            break
    if not put:
        for j in range(z - packages[i].width + 1):
            poss = True
            for k in range(packages[i].width):
                if knapsack[j + k] < packages[i].height:
                    poss = False
                    break
            if poss:
                put = True
                knapsack_value += packages[i].value
                for k in range(packages[i].width):
                    knapsack[j + k] -= packages[i].height
                break
print(knapsack)
print(knapsack_value)

start = time.time()
for i in range(100):
    x = randint(1, len(packages)-1)
    y = randint(1, len(packages)-1)
    packages[x], packages[y] = packages[y], packages[x]
    knapsack_value_copy = 0
    knapsack = [z for l in range(z)]
    for i in range(len(packages)):
        put = False
        for j in range(z - packages[i].height + 1):
            poss = True
            for k in range(packages[i].height):
                if knapsack[j + k] < packages[i].width:
                    poss = False
                    break
            if poss:
                put = True
                knapsack_value_copy += packages[i].value
                for k in range(packages[i].height):
                    knapsack[j + k] -= packages[i].width
                break
        if not put:
            for j in range(z - packages[i].width + 1):
                poss = True
                for k in range(packages[i].width):
                    if knapsack[j + k] < packages[i].height:
                        poss = False
                        break
                if poss:
                    put = True
                    knapsack_value_copy += packages[i].value
                    for k in range(packages[i].width):
                        knapsack[j + k] -= packages[i].height
                    break
    if knapsack_value_copy > knapsack_value:
        knapsack_value = knapsack_value_copy

print(knapsack_value)
print("Time:", time.time()-start)