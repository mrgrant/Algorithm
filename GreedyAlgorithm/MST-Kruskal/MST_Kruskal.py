from itertools import islice


class UF():
    def __init__(self, N):
        """
        Initialize an empty union find object with N items.
        :param N: Number of items in the union find object
        """

        self._parent = list(range(N))
        self._count = N
        self._rank = [0] * N

    def find(self, p):
        """Find the set parents for item p"""
        parent = self._parent
        while p != parent[p]:
            p = parent[p] = parent[parent[p]]  # Path compression using halving
        return p

    def count(self):
        """Return number of items"""
        return self._count

    def connected(self, p, q):
        """Check if the items p and q are on the same set or not"""
        return self.find(p) == self.find(q)

    def union(self, p, q):
        parent = self._parent
        rank = self._rank
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        self._count -= 1
        if rank[i] < rank[j]:
            parent[i] = j
        elif rank[i] > rank[j]:
            parent[j] = i
        else:
            parent[j] = i
            rank[i] += 1


def kruskal(edges, N, k):
    """
    Clustering the nodes using Kruskal's algorithm
    :param edges: a list of all edges
    :param N: number of vertices
    :param k: number of clusters desired
    :return: minimum distance between two clusters
    """
    edges.sort(key=lambda x: x[2])
    dis = []
    uf = UF(N)
    for i in range(len(edges)):
        if uf.count() == 1:
            break
        p = edges[i][0] - 1
        q = edges[i][1] - 1
        if uf.connected(p, q) is not True:
            if uf.count() <= k:
                dis.append(edges[i][2])
            uf.union(p, q)
    return min(dis)


def load_graph(filename):
    edges = []
    with open(filename, 'r') as f:
        cnt = 0
        for line in f:
            if cnt == 0:
                N = int(line)
            else:
                x, y, d = line.split()
                edges.append([int(x), int(y), int(d)])
            cnt += 1
    return N, edges


if __name__ == '__main__':
    # N = 6
    k = 20
    N, edge = load_graph('edge_test.txt')
    cost = kruskal(edge, N, k)
    print(cost)
