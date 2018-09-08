# knapsack problem
def load_data(filename):
    alist = list()
    with open(filename, 'r') as f:
        cnt = 0
        for line in f:
            if cnt == 0:
                W, N = line.split()
                W, N = int(W), int(N)
            else:
                value, weight = line.split()
                alist.append([int(value), int(weight)])
            cnt += 1
    return W, N, alist


def knapsack(W, N, data):
    A = [[None for x in range(W+1)]for y in range(N)]
    for x in range(W+1):
        A[0][x] = 0

    for i in range(1, N):
        for x in range(W+1):
            if data[i-1][1] > x:  # data index from 0 to N-1
                A[i][x] = A[i-1][x]
            else:
                A[i][x] = max(A[i-1][x], A[i-1][x-data[i-1][1]]+data[i-1][0])
    return A


if __name__ == '__main__':
    # data[i][value, weight]
    W, N, data = load_data('knapsack1.txt')
    A = knapsack(W, N, data)
    print(A[N-1][W])
