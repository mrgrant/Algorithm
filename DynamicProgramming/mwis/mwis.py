# Max Weight Independent Set
def load_data(filename):
    alist = []
    with open(filename, 'r') as f:
        cnt = 0
        for line in f:
            if cnt == 0:
                N = int(line)
            else:
                alist.append(int(line))
            cnt += 1
    return N, alist


def dp(w, N):
    A = {}
    A[-1], A[0], A[1] = 0, 0, w[0]
    for i in range(2, N+1):
        A[i] = max(A[i-1], A[i-2]+w[i-1])
    return A


def reconstruction(A, w):
    s = []
    i = len(w)
    while i >= 1:
        if A[i-1] >= A[i-2] + w[i-1]:
            i -= 1
        else:
            s.append(i)
            i -= 2
    return s


def find_vertices(v):
    str = ''
    for i in v:
        if i in s:
            str += '1'
        else:
            str += '0'
    return str


if __name__ == '__main__':
    N, weight = load_data('mwis.txt')
    A = dp(weight, N)
    s = reconstruction(A, weight)
    vertices = [1, 2, 3, 4, 17, 117, 517, 997]
    print(find_vertices(vertices))
    print(A[N])