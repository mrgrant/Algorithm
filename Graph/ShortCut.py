import random
import copy
import math


def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
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


if __name__ == '__main__':
    # read graph from txt
    graph = {}
    with open("data.txt") as f:
        for line in f:
            x, *y = map(int, line.split())
            graph[x] = y

    vertices = generate_vertices(graph)
    edges = generate_edges(graph)
    MinCut = []
    n = len(vertices)
    N = int((n**2)*math.log(n, math.exp(1)))
    for i in range(N):
        v = copy.deepcopy(vertices)
        e = copy.deepcopy(edges)
        MinCut.append(contraction(v, e))

    # print(MinCut)
    print(min(MinCut))
