from random import randint
from mergesort import mergesort
from insertionsort import insertionsort
import time

# przyjelam ciag o dlugosci 10^4 i 100 iteracji

insertion_sort_time = []
merge_sort_time = []
# insertion_sort
for i in range(100):
    array = []
    for k in range(10000):
        array.append(randint(0, 100000000))
    start = time.time()
    insertionsort(array)
    insertion_sort_time.append(time.time()-start)


# merge_sort
for i in range(100):
    array = []
    for k in range(10000):
        array.append(randint(0, 100000000))
    start = time.time()
    mergesort(array, 0, len(array)-1)
    merge_sort_time.append(time.time()-start)

insertion_sort_time.sort()
merge_sort_time.sort()
sum_insertion = sum(insertion_sort_time)
sum_merge = sum(merge_sort_time)
average_insertion = sum_insertion/100
average_merge = sum_merge/100

print("Czas wszystkich sortowań dla insertionsorta:", sum_insertion, "s.")
print("Czas najszybszego sortowania dla insertionsorta:", insertion_sort_time[0], "s.")
print("Czas najwolniejszego sortowania dla insertionsorcie:", insertion_sort_time[99], "s.")
print("Średni czas sortowania dla insertionsorta:", average_insertion, "s.")
print("Czas wszystkich sortowań dla mergesorta:", sum_merge, "s.")
print("Czas najszybszego sortowania dla mergesorta:", merge_sort_time[0], "s.")
print("Czas najwolniejszego sortowania dla mergesorta:", merge_sort_time[99], "s.")
print("Średni czas sortowania dla mergesorta:", average_merge, "s.")
