from itertools import islice


def generate_vertices(graph):
    vertices = []
    for node in graph:
        vertices.append(node)
    return vertices


def is_connect(graph):
    def DFS(graph, s):
        seen.append(s)
        for v in graph[s]:
            if v not in seen:
                DFS(graph, v)

    seen = []
    vertices = generate_vertices(graph)
    DFS(graph, next(iter(graph)))
    if len(seen) == len(vertices):
        return True
    else:
        return False


def prim_mst(graph):
    s = next(iter(graph))
    visited = [s]
    t = []
    cost = 0
    v = generate_vertices(graph)
    length = len(v)
    v.remove(s)
    while len(visited) != length:
        min_node = None
        min_end = None
        for node in visited:
            for end in graph[node]:
                if end in v:
                    if min_node is None:
                        min_node = node
                    if min_end is None:
                        min_end = end
                    if min_end in graph[min_node] and graph[node][end] < graph[min_node][min_end]:
                        min_node = node
                        min_end = end
        
        t.append([min_node, min_end])
        visited.append(min_end)
        v.remove(min_end)
        cost += graph[min_node][min_end]
    
    return t, cost


def load_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in islice(f, 1, None):
            x, y, d = line.split()
            if int(x) not in graph:
                graph[int(x)] = {}
            if int(y) not in graph:
                graph[int(y)] = {}
            graph[int(x)][int(y)] = int(d)
            graph[int(y)][int(x)] = int(d)
    return graph


if __name__ == '__main__':
    # graph = {
    #     'S': {'V': 1, 'W': 4},
    #     'V': {'W': 2, 'T': 6, 'S': 1},
    #     'W': {'S': 4, 'T': 3, 'V': 2},
    #     'T': {'V': 6, 'W': 3}}
    graph = load_graph('edges_test.txt')
    if not is_connect(graph):
        print('Graph not connect!!!')
    else:
        t, cost = prim_mst(graph)
        print(t)
        print(cost)
