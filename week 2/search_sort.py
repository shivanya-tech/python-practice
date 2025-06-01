
# Week 2 — Search and Sort

def bsearch(v, L):
    # Recursive binary search
    if L == []:
        return False
    m = len(L) // 2
    if v == L[m]:
        return True
    if v < L[m]:
        return bsearch(v, L[:m])
    else:
        return bsearch(v, L[m+1:])

print(bsearch(7, [0, 1, 2, 4, 5, 9]))


def selection_sort(l):
    # In-place selection sort
    n = len(l)
    if n < 1:
        return l
    for i in range(n):
        mpos = i
        for j in range(i + 1, n):
            if l[j] < l[mpos]:
                mpos = j
        l[i], l[mpos] = l[mpos], l[i]
    return l

print(selection_sort([2, 5, 1, 4, 9, 0]))


def insertionSort(array):
    # Insertion sort algorithm
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

print(insertionSort([0, 1, 2, 4, 5, 9]))
