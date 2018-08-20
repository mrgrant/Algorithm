def MergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left_list = alist[:mid]
        right_list = alist[mid:]
        # recursive calls
        MergeSort(left_list)
        MergeSort(right_list)

        # merge array
        i = 0
        j = 0
        k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                alist[k] = left_list[i]
                i = i + 1
            elif left_list[i] > right_list[j]:
                alist[k] = right_list[j]
                j = j + 1
            k = k + 1
        while i == len(left_list) and j < len(right_list):
            alist[k] = right_list[j]
            j = j + 1
            k = k + 1
        while i < len(left_list) and j == len(right_list):
            alist[k] = left_list[i]
            i = i + 1
            k = k + 1

import random
alist = random.sample(range(1000000),1000000)
MergeSort(alist)
