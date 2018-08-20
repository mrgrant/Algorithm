def count_and_merge(alist):
    cnt = 0
    if len(alist) > 1:
        mid = len(alist)//2
        left_list = alist[:mid]
        right_list = alist[mid:]
        cnt += count_and_merge(left_list)
        cnt += count_and_merge(right_list)

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                alist[k] = left_list[i]
                k = k + 1
                i = i + 1
            else:
                alist[k] = right_list[j]
                k = k + 1
                j = j + 1
                cnt += len(left_list)-i
        while j == len(right_list) and i < len(left_list):
            alist[k] = left_list[i]
            k = k + 1
            i = i + 1
            cnt += len(left_list) - i
        while i == len(left_list) and j < len(right_list):
            alist[k] = right_list[j]
            k = k + 1
            j = j + 1
    return cnt

alist = []
with open('MergeSort/IntegerArray.txt','r') as f:
    for i in f.readlines():
        alist.append(i)

res = count_and_merge(alist)
print(res)
