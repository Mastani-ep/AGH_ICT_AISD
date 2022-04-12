# from random import randint

def insertionsort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i-1
        while j >= 0 and array[j] > x:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = x

# to byla tylko proba
# example = []
# print("Enter N:")
# N = int(input())
# for k in range(N):
#     example.append(randint(0, 100000))
# print(example)
# insertionsort(example)
# print(example)
