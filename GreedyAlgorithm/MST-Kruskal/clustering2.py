from itertools import islice


class UF:
    def __init__(self, N, vertices):
        """
        Initialize an empty union find object with N items.
        :param N: Number of items in the union find object
        """

        self._parent = {i: i for i in vertices}
        self._count = N
        self._rank = {i: 0 for i in vertices}

    def find(self, p):
        """Find the set parents for item p"""
        parent = self._parent
        while p != parent[p]:
            p = parent[p]  # !!cannot apply path compression to this problem
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


def load_data(filename):
    data = set()
    with open(filename, 'r') as f:
        for line in islice(f, 1, None):
            str = ''.join(line.split())
            num = int(str, 2)
            if num in data:
                continue
            data.add(num)
    return data, len(data)


def cluster(vertices, N, bit):
    """
    clustering all vertices
    :param vertices:
    :param N: number of non-duplicate vertices
    :param bit: all bits of binary number
    :return: clusters
    """
    uf = UF(N, vertices)

    for node in vertices:
        # using bit-shifting to find possible vertices belongs to the origin vertices and cluster them together
        x2 = 1
        for i in range(bit):
            x1 = 1
            for j in range(i+1):
                x = x1 | x2  # e.g. x1 = 00010, x2 = 00001, x1|x2 = 00011
                new_node = node ^ x
                if new_node in vertices:
                    if uf.connected(node, new_node) is not True:
                        uf.union(node, new_node)
                x1 = x1 << 1
            x2 = x2 << 1
    return uf.count()


if __name__ == '__main__':
    bit = 24
    vertices, N = load_data('clustering_big.txt')
    k = cluster(vertices, N, bit)
    print(N, k)
