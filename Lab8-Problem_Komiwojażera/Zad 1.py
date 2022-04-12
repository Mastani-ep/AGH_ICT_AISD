# dowolna sciezka
from random import randint
import math


class City:
    def __init__(self, a, b, c):
        self.name = c
        self.x = a
        self.y = b

    def length_path(self, city):
        return math.sqrt((self.x-city.x)*(self.x-city.x)+(self.y-city.y)*(self.y-city.y))


def create_path(path):
    global cities
    wsp_exist = [0]
    while len(path) != 100:
        x = randint(0, 99)
        if x not in wsp_exist:
            path.append(cities[x])
            wsp_exist.append(x)

    path.append(cities[0])


def len_paths(path):
    length = 0
    for i in range(len(path)-1):
        length += path[i].length_path(path[i+1])
    return length


f = open('TSP.txt', 'r')
cities = []
for line in f:
     cities.append(City(float(line.split('\t', 2)[1]), float((line.split('\t', 2)[2]).split('\n', 1)[0]), int(line.split('\t', 2)[0])))

f.close()
path = [cities[0]]
create_path(path)
print("Path length: ", len_paths(path))
print("Path: ", end='')
for i in range(len(path)-1):
    print(str(path[i].name) + '--', end='')
print(str(path[len(path)-1].name))
