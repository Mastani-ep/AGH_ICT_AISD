# from random import randint


def mergesort(array, left, right):
    if left < right:
        middle = (left+right)//2
        mergesort(array, left, middle)
        mergesort(array, middle+1, right)
        merge(array, left, middle, right)


def merge(array, left, middle, right):
    left_array = array[left:middle + 1]
    right_array = array[middle + 1:right + 1]

    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            array[left] = left_array[left_index]
            left_index += 1
        else:
            array[left] = right_array[right_index]
            right_index += 1
        left += 1

    while left_index < len(left_array):
        array[left] = left_array[left_index]
        left_index += 1
        left += 1

    while right_index < len(right_array):
        array[left] = right_array[right_index]
        right_index += 1
        left += 1

# tu byla tylko proba
# example = []
# print("Enter N:")
# N = int(input())
# for i in range(N):
#     example.append(randint(0, 1000000))
# print(example)
# mergesort(example, 0, len(example)-1)
# print(example)
