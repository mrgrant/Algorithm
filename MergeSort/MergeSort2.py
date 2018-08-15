def Merge(left_list,right_list):
    i = 0
    j = 0
    alist = []
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            alist.append(left_list[i])
            i = i + 1
        elif left_list[i] > right_list[j]:
            alist.append(right_list[j])
            j = j + 1
    alist += left_list[i:]
    alist += right_list[j:]
    return alist

def MergeSort(origin_list):
    if len(origin_list)>1:
        mid = len(origin_list)//2
        left_list = origin_list[:mid]
        right_list = origin_list[mid:]
        left_list = MergeSort(left_list)
        right_list = MergeSort(right_list)
        return Merge(left_list,right_list)
    else:
        return origin_list

alist = [54, 26, 93, 17]
res = MergeSort(alist)
print(res)
