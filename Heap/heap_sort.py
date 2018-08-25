def parent(i):
    return i//2


def left(i):
    return 2*i+1


def right(i):
    return 2*i+2


def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= len(A)-1 and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A)-1 and A[r] > A[largest]:
        largest = r
    if not largest == i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 1, -1):
        A[0], A[i] = A[i], A[0]
        temp = A.pop()
        ret.append(temp)
        max_heapify(A, 0)


if __name__ == '__main__':
    A = [2, 5, 1, 6, 3]
    ret = []

    heap_sort(A)
    ret += A
    print(ret)

