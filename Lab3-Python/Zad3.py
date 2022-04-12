import random
import math


# area of rectangle
def rectangle(k, m, ymax):
    return (m-k)*ymax


# limits of integration
a = 0
b = 2
# max of sin used as one of the sides of rectangle
fmax = 1
# number of all points in rectangle
N = 10000
# arrays - coordinates of points
xrand = []
yrand = []
for i in range(N):
    xrand.append(random.uniform(a, b))

for i in range(N):
    yrand.append(random.uniform(0, fmax))
# points under graph
N_p = 0
for i in range(N):
    if yrand[i] <= math.sin(xrand[i]):
        N_p += 1
    else:
        pass

integral = (N_p/N)*rectangle(a, b, fmax)
print("Result of integration:", integral)

# for greater N the accuracy is better
