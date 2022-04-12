import time


def naive(matrix, pattern):
    n = len(matrix)
    m = len(pattern)
    count = 0
    for i in range(n - m + 1):
        for s in range(n - m + 1):
            check_poz = True
            for j in range(m):
                if matrix[i][s+j] != pattern[j]:
                    check_poz = False
                    break
            if check_poz:
                check_pion = True
                for k in range(m - 1):
                    if matrix[i+k+1][s] != pattern[k+1]:
                        check_pion = False
                        break
                if check_pion:
                    # print("Found pattern:", i, s)
                    count += 1
    # print("Number of found patterns:", count)


def rabin_karp(matrix, pattern, d, q):
    m = len(pattern)
    n = len(matrix)
    h = 1
    count = 0
    for i in range(m-1):
        h = (h*d) % q
    for z in range(n-m+1):
        p = 0
        t = 0
        j = 0
        for i in range(m):
            p = (d*p + ord(pattern[i])) % q
            t = (d*t + ord(matrix[z][i])) % q
        for s in range(n-m+1):
            if p == t:
                for j in range(m):
                    if matrix[z][s+j] != pattern[j]:
                        break

                j += 1
                if j == m:
                    check_pion = True
                    for k in range(m - 1):
                        if matrix[z + k + 1][s] != pattern[k + 1]:
                            check_pion = False
                            break
                    if check_pion:
                        # print("Found pattern:", z, s)
                        count += 1
            if s < n-m:
                t = (d*(t-ord(matrix[z][s])*h) + ord(matrix[z][s+m])) % q

                if t < 0:
                    t = t+q
    # print("Number of found patterns:", count)


pattern = "ABC"
d = 1000
q = 1001
time_naive = []
time_rk = []
f = open('1000_pattern.txt', 'r')
matrix = []
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time()-start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 1000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 1000:", (sum(time_rk)/100), "s.")

f = open('2000_pattern.txt', 'r')
matrix = []
time_naive = []
time_rk = []
d = 2000
q = 2003
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time()-start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 2000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 2000:", (sum(time_rk)/100), "s.")

f = open('3000_pattern.txt', 'r')
matrix = []
d = 3000
q = 3001
time_naive = []
time_rk = []
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time() - start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 3000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 3000:", (sum(time_rk)/100), "s.")

f = open('4000_pattern.txt', 'r')
matrix = []
time_naive = []
time_rk = []
d = 4000
q = 4001
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time() - start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 4000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 4000:", (sum(time_rk)/100), "s.")

f = open('5000_pattern.txt', 'r')
matrix = []
time_naive = []
time_rk = []
d = 5000
q = 5003
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time() - start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 5000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 5000:", (sum(time_rk)/100), "s.")

f = open('8000_pattern.txt', 'r')
matrix = []
time_naive = []
time_rk = []
d = 8000
q = 8009
for line in f:
    matrix.append(line)
f.close()

for i in range(100):
    start = time.time()
    naive(matrix, pattern)
    time_naive.append(time.time() - start)
    start = time.time()
    rabin_karp(matrix, pattern, d, q)
    time_rk.append(time.time() - start)

print("Average time for naive algorithm and matrix 8000:", (sum(time_naive)/100), "s.")
print("Average time for Rabin-Karp algorithm and matrix 8000:", (sum(time_rk)/100), "s.")
