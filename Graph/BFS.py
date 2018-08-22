import queue


def generate_explored_dic(graph):
    explored_dic = {}
    for node in graph:
        explored_dic[node] = 0
    return explored_dic


def generate_dist_dic(graph, s):
    dist_dic = {}
    for node in graph:
        if node == s:
            dist_dic[node] = 0
        else:
            dist_dic[node] = float('inf')
    return dist_dic


def BFS(graph, s):
    explored = generate_explored_dic(graph)
    explored[s] = 1
    dist = generate_dist_dic(graph, s)
    q = queue.Queue(0)
    q.put(s)
    while not q.empty():
        v = q.get()
        for w in graph[v]:
            if explored[w] == 0:
                dist[w] = dist[v] + 1
                explored[w] = 1
                q.put(w)
    return dist


if __name__ == '__main__':
    # read graph from txt
    graph = {}
    with open("data.txt") as f:
        for line in f:
            x, *y = map(int, line.split())
            graph[x] = y

    # graph1 = {"a": ["c"],
    #          "b": ["c", "e"],
    #          "c": ["a", "b", "d", "e"],
    #          "d": ["c"],
    #          "e": ["c", "b"],
    #          "f": []
    #          }

    dist1 = BFS(graph, 1)
    print(dist1)
    print('a')
