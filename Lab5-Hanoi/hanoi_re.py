import time


def move(s, d):
    global count, source, destination, buffer
    d.append(s.pop())
    count += 1
    print(count, ")", source, "|", buffer, "|", destination)


def hanoi_re(n, sour, dest, buff):
    if n > 0:
        hanoi_re(n - 1, sour, buff, dest)
        move(sour, dest)
        hanoi_re(n - 1, buff, dest, sour)


# do zadania 3 z porownaniem
count = 0
discs = 3
source = [i for i in range(discs, 0, -1)]
destination = []
buffer = []
print("SOURCE", "|", "BUFFER", "|", "DESTINATION")
print(count, ")", source, "|", buffer, "|", destination)
start = time.time()
hanoi_re(discs, source, destination, buffer)
print("Czas układania wieży hanoi dla rekurencji: ", time.time()-start, "s")
print("Liczba wykonanych ruchów: ", count)
