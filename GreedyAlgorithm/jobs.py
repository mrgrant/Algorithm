def score(data, num):
    for i in range(num):
        score = data[i][0] / data[i][1]
        data[i].insert(0, score)
    data.sort(reverse=True)

    for i in range(num-1):
        if data[i][0] == data[i+1][0]:
            if data[i][1] < data[i+1][1]:
                data[i], data[i+1] = data[i+1], data[i]
    
    return data


def completion_time(data, num):
    length = 0
    sum_of_c = 0
    for i in range(num):
        length += data[i][2]
        sum_of_c += length*data[i][1]
    return sum_of_c


def load_data(filename):
    alist = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.split())
            alist.append([x, y])
    return alist


if __name__ == '__main__':
    data = load_data('jobs.txt')
    num = len(data)
    data_score = score(data, num)
    c_time = completion_time(data_score, num)
    print(c_time)
