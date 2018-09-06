def load_data(filename):
    a = []
    with open(filename) as f:
        for line in f:
            a.append(int(line.strip()))
        return a


def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid + 1
        elif midval > x:
            hi = mid
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    # using set to reduce searching time
    data = load_data('data.txt')
    data.sort()
    ret = set()
    d = set(data)
    for t in range(-10000, 10001):
        for i in d:
            x = t - i
            if x in d and t not in ret:
                ret.add(t)
                break
        print(t)
    print(len(ret))
