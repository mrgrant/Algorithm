# in-place quick sort
# without taking extra memory
import random


def partition(array, l, r):
    pivot_idx = random.randint(l, r)
    p = array[pivot_idx]
    # swap the random pivot to the head of array
    array[l], array[pivot_idx] = array[pivot_idx], array[l]

    i = l + 1
    for j in range(l+1, r+1):
        # swap the number less than pivot at left of the array
        if array[j] < p:
            array[j], array[i] = array[i], array[j]
            i = i + 1
    array[l], array[i-1] = array[i-1], array[l]
    return i-1


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if end - start < 1:
        return

    i = partition(array, start, end)
    quicksort(array, start, i-1)
    quicksort(array, i+1, end)


if __name__ == "__main__":
    alist = [8, 2, 4, 5, 3]
    quicksort(alist)
    print(alist)
