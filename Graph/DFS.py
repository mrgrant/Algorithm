# Deep First Search
def generate_explored_dic(graph):
    explored_dic = {}
    for node in graph:
        explored_dic[node] = 0
    return explored_dic


def DFS(graph, s):
    explored[s] = 1
    for v in graph[s]:
        if explored[v] == 0:
            DFS(graph, v)


if __name__ == '__main__':
    graph = {"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }
    explored = generate_explored_dic(graph)
    DFS(graph, 'a')
    print('a')
