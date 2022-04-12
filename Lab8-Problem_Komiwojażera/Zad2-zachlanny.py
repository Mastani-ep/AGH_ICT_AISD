# zachlanny
from math import sqrt, inf
import time


class City:
    def __init__(self, a, b, c):
        self.name = c
        self.x = a
        self.y = b

    def length_path(self, city):
        return sqrt((self.x-city.x)*(self.x-city.x)+(self.y-city.y)*(self.y-city.y))


start = time.time()
f = open('TSP.txt', 'r')
cities = []
for line in f:
    cities.append(City(float(line.split('\t', 2)[1]), float((line.split('\t', 2)[2]).split('\n', 1)[0]), int(line.split('\t', 2)[0])))
f.close()


visited = [cities[0]]
len_path = 0
j = 0
len_cities = len(cities)-1
len_cities_2 = len(cities)
index_list = [0 for i in range(100)]
index_list[0] = 1
while j != len_cities:
    len_closest = inf
    closest = None
    for i in range(len_cities_2):
        if index_list[i] == 0:
            if len_closest > visited[j].length_path(cities[i]):
                len_closest = visited[j].length_path(cities[i])
                closest = cities[i]
                k = i
    len_path += len_closest
    visited.append(closest)
    index_list[k] = 1
    j += 1

visited.append(cities[0])
len_path += visited[len(visited)-2].length_path(visited[len(visited)-1])
print("Path length for greedy algorithm: ", len_path)
print("Path: ", end='')
for i in range(len(visited)-1):
    print(str(visited[i].name)+"--", end='')
print(str(visited[len(visited)-1].name))
print("Time: ", time.time()-start)
