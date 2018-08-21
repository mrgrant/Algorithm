import random


def quicksort(A):
    less = []
    equal = []
    greater = []
    if len(A) > 1:
        # random pivots
        pivot = A[random.randrange(len(A))]
        for x in A:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return A
    

if __name__ == "__main__":
    alist = random.sample(range(10000000),1000000)
    # new = quicksort(alist)
    # print(new)
