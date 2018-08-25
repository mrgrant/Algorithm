def insert_max(arr, ins):
    """
    insert in max heap and bubble up
    :param arr: origin array
    :param ins: insert number i
    :return:
    """
    arr.append(ins)
    i = len(arr)-1
    p = len(arr)//2 - 1
    while i > 0:
        if arr[i] < arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
            i = p
            p = (p+1)//2 - 1
        else:
            break


def insert_min(arr, ins):
    """
    insert in min heap and bubble up
    :param arr: origin array
    :param ins: insert number i
    :return:
    """
    arr.append(ins)
    i = len(arr)-1
    p = len(arr)//2 - 1
    while i > 0:
        if arr[i] > arr[p]:
            arr[i], arr[p] = arr[p], arr[i]
            i = p
            p = (p+1)//2 - 1
        else:
            break


def max_heapify(arr, i):
    n = len(arr)
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[i]:
        smallest = l
    else:
        smallest = i
    if r < n and arr[r] < arr[smallest]:
        smallest = r
    if not smallest == i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        max_heapify(arr, smallest)


def min_heapify(arr, i):
    n = len(arr)
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < n and arr[r] > arr[largest]:
        largest = r
    if not largest == i:
        arr[i], arr[largest] = arr[largest], arr[i]
        min_heapify(arr, largest)
        
        
def extract_min(arr):
    """
    Extract min and Bubble Down
    :param arr: original array
    :return: 
    """
    n = len(arr)
    arr[0], arr[n-1] = arr[n-1], arr[0]
    max_min = arr.pop(n-1)
    min_heapify(arr, 0)
    return max_min


def extract_max(arr):
    """
    Extract max and Bubble down
    :param arr: original array
    :return: 
    """
    n = len(arr)
    arr[0], arr[n-1] = arr[n-1], arr[0]
    min_max = arr.pop(n-1)
    max_heapify(arr, 0)
    return min_max
    

def median_maintainace(min_heap, max_heap, a):
    """
    median maintainace when input a new number
    :param min_heap:a heap saves the numbers less than median
    :param max_heap:a heap saves the number larger than median
    :param a:new input number
    :return:median
    """
    length = len(min_heap) + len(max_heap) + 1
    if length == 1:
        max_heap.append(a)
        return a
    else:
        if a >= max_heap[0]:
            insert_max(max_heap, a)
        else:
            insert_min(min_heap, a)
        if len(min_heap) > length//2:
            ext = extract_min(min_heap)
            insert_max(max_heap, ext)
        elif len(max_heap) > length//2 and length % 2 == 0:
            ext = extract_max(max_heap)
            insert_min(min_heap, ext)
    return max_heap[0]


if __name__ == '__main__':
    min_heap = []
    max_heap = []
    alist = []
    with open('Median.txt', 'r') as f:
        for i in f.readlines():
            alist.append(int(i))

    median = []
    for i in range(len(alist)):
        m = median_maintainace(min_heap, max_heap, alist[i])
        median.append(m)

    print(sum(median)//10000)
