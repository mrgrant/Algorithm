def max_heapify(A, n, i):
    """
    max_heapify
    :param A: array A
    :param n: size of a heap
    :param i: root at index i
    :return:
    """
    l = 2*i+1
    r = 2*i+2
    if l < n and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < n and A[r] > A[largest]:
        largest = r
    if not largest == i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def build_max_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify(A, len(A), i)


def heap_sort(A):
    build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, i, 0)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heap_sort(arr)
    print(arr)


