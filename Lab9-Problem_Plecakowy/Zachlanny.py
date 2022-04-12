import time


class Package:
    def __init__(self, a, b, c, d):
        self.id = a
        self.width = b
        self.height = c
        self.value = d
        self.den_val = d/(b*c)


f = open('packages20.txt', 'r')
i = 0
packages = []
for line in f:
    if i <= 1:
        i += 1
    else:
        packages.append(Package(int(line.split(',', 4)[0]), int(line.split(',', 4)[1]), int(line.split(',', 4)[2]), int(line.split(',', 4)[3])))
f.close()
#
#
start = time.time()
sorter = lambda x: (x.den_val)
packages = sorted(packages, key=sorter, reverse=True)

x = 20
knapsack = [x for i in range(x)]
knapsack_value = 0
for i in range(len(packages)):
    put = False
    for j in range(x - packages[i].height + 1):
        poss = True
        for k in range(packages[i].height):
            if knapsack[j+k] < packages[i].width:
                poss = False
                break
        if poss:
            put = True
            knapsack_value += packages[i].value
            print("Package", packages[i].id, "was put in knapsack.")
            for k in range(packages[i].height):
                knapsack[j + k] -= packages[i].width
            break
    if not put:
        for j in range(x - packages[i].width + 1):
            poss = True
            for k in range(packages[i].width):
                if knapsack[j + k] < packages[i].height:
                    poss = False
                    break
            if poss:
                put = True
                print("Package", packages[i].id, "(diverted) was put in knapsack.")
                knapsack_value += packages[i].value
                for k in range(packages[i].width):
                    knapsack[j + k] -= packages[i].height
                break
print("Knapsack:", knapsack)
print("Knapsack value:", knapsack_value)
print("time:", time.time()-start)