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
                    print("Found pattern:", i, s)
                    count += 1
    print("Number of found patterns:", count)


f = open('1000_pattern.txt', 'r')
matrix = []
for line in f:
    matrix.append(line)
f.close()
pattern = "ABC"
print("Naive algorithm")
naive(matrix, pattern)
