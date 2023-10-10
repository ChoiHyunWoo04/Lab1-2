import random
import time

def selectionSort(l):
    for i in range(len(l)):
        min_idx = i
        for j in range(i+1, len(l)):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]

    return l

def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l

def insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key > l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key

    return l


list1 = [i for i in range(10000)]

random.shuffle(list1)
start1 = time.time()
selectionSort(list1)
end1 = time.time()

random.shuffle(list1)
start2 = time.time()
bubbleSort(list1)
end2 = time.time()

random.shuffle(list1)
start3 = time.time()
insertionSort(list1)
end3 = time.time()

random.shuffle(list1)
start4 = time.time()
list1.sort()
end4 = time.time()

print(f"selectionSort: {end1 - start1}초")
print(f"bubbleSort: {end2 - start2}초")
print(f"insertionSort: {end3 - start3}초")
print(f"list1.sort: {end4 - start4}초")
