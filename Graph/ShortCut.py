import random
import copy
import math
import time

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            if [neighbor, node] in edges:
                pass
            else:
                edges.append([node, neighbor])
    return edges


def generate_vertices(graph):
    vertices = []
    for node in graph:
        vertices.append(node)
    return vertices


def contraction(ver, e):
    while len(ver) > 2:
        idx = random.randrange(0, len(e))
        [u, v] = e.pop(idx)
        ver.remove(u)
        newedges = []
        for i in range(len(e)):
            if e[i][0] == u:
                e[i][0] = v
            elif e[i][1] == u:
                e[i][1] = v
            if e[i][0] != e[i][1]:
                newedges.append(e[i])
        e = newedges
    return len(e)


def load_data(filename):
    graph = {}
    with open(filename) as f:
        for line in f:
            x, *y = map(int, line.split())
            graph[x] = y
    return graph


if __name__ == '__main__':
    # read graph from txt
    # graph = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
    graph = load_data('data.txt')
    vertices = generate_vertices(graph)
    edges = generate_edges(graph)
    MinCut = []
    n = len(vertices)
    N = int((n**2)*math.log(n, math.exp(1)))
    t1 = time.clock()
    for i in range(1500):
        v = copy.deepcopy(vertices)
        e = copy.deepcopy(edges)
        MinCut.append(contraction(v, e))
    # print(MinCut)
    print(min(MinCut))
    t2 = time.clock()
    print(t2-t1)
