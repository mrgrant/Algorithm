# Find Minimum Spinning Tree using Heap data structure
from itertools import islice


class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    # swap two nodes of min heap. Needed for min heapify
    def swapMinHeapNode(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def min_heapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right

        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)
            self.min_heapify(smallest)

    def extractMin(self):
        if self.isempty() is True:
            return
        # Store the root node
        root = self.array[0]
        # Replace root node with last node
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
        # Update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        # Reduce heap size and heapify root
        self.size -= 1
        self.min_heapify(0)

    def isEmpty(self):
        return True if self.size == 0 else False

    def decraseKey(self, v, dist):
        # Get the index of v in heap array
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i-1)//2][1]:
            self.pos[self.array[i][0]] = (i-1)//2
            self.pos[self.array[(i-1)//2][0]] = i
            self.swapMinHeapNode(i, (i-1)//2)
            i = (i-1)//2

    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


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


def prim_mst(graph):

if __name__ == '__main__':
    # graph = {
    #     'S': {'V': 1, 'W': 4},
    #     'V': {'W': 2, 'T': 6, 'S': 1},
    #     'W': {'S': 4, 'T': 3, 'V': 2},
    #     'T': {'V': 6, 'W': 3}}
    graph = load_graph('edges.txt')
    if not is_connect(graph):
        print('Graph not connect!!!')
    else:
        t, cost = prim_mst(graph)
        print(t)
        print(cost)
