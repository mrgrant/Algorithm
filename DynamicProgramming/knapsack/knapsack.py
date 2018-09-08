# knapsack problem
import copy


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


def knapsack_big(W, N, data):
    # compress the array in two column
    A = [[None for x in range(W + 1)] for y in range(2)]
    for x in range(W + 1):
        A[0][x] = 0

    for i in range(1, N):
        for x in range(W+1):
            if data[i-1][1] > x:
                A[1][x] = A[0][x]
            else:
                A[1][x] = max(A[0][x], A[0][x-data[i-1][1]]+data[i-1][0])
        A[0] = copy.copy(A[1])
        print(i)
    return A


if __name__ == '__main__':
    # data[i][value, weight]
    W, N, data = load_data('knapsack_big.txt')
    # A1 = knapsack(W, N, data)
    # print(A1[N-1][W])

    A = knapsack_big(W, N, data)  # 4243395
    print(A[1][W])
