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
                        print("Found pattern:", z, s)
                        count += 1

            if s < n-m:
                t = (d*(t-ord(matrix[z][s])*h) + ord(matrix[z][s+m])) % q

                if t < 0:
                    t = t+q
    print("Number of found patterns:", count)


f = open('1000_pattern.txt', 'r')
matrix = []
for line in f:
    matrix.append(line)
f.close()
pattern = "ABC"
d = 1000
q = 1001
print("Rabin-Karp algorithm")
rabin_karp(matrix, pattern, d, q)
