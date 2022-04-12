import time


def hanoi_it(n, sour, dest, buff):
    global count
    if n % 2 == 1:
        while len(sour) != 0 or len(buff) != 0:
            if count % 3 == 1:
                check_and_move(sour, dest)
            elif count % 3 == 2:
                check_and_move(sour, buff)
            elif count % 3 == 0:
                check_and_move(buff, dest)
    else:
        while len(sour) != 0 or len(buff) != 0:
            if count % 3 == 1:
                check_and_move(sour, buff)
            elif count % 3 == 2:
                check_and_move(sour, dest)
            elif count % 3 == 0:
                check_and_move(buff, dest)


def check_and_move(a, b):
    global count, source, destination, buffer
    if len(b) > 0 and len(a) > 0:
        if a[len(a) - 1] > b[len(b) - 1]:
            a.append(b.pop())
            print(count, ")", source, "|", buffer, "|", destination)
            count += 1
        else:
            b.append(a.pop())
            print(count, ")", source, "|", buffer, "|", destination)
            count += 1
    elif len(a) == 0:
        a.append(b.pop())
        print(count, ")", source, "|", buffer, "|", destination)
        count += 1
    elif len(b) == 0:
        b.append(a.pop())
        print(count, ")", source, "|", buffer, "|", destination)
        count += 1


# do zadania 3 z porownaniem
count = 1
discs = 3
source = [i for i in range(discs, 0, -1)]
destination = []
buffer = []
print("SOURCE", "|", "BUFFER", "|", "DESTINATION")
print("0 )", source, "|", buffer, "|", destination)
start = time.time()
hanoi_it(discs, source, destination, buffer)
print("Czas układania wieży hanoi dla iteracji: ", time.time()-start, "s")
print("Liczba wykonanych ruchów: ", count - 1)
