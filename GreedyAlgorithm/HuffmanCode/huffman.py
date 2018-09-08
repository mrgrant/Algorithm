import heapq


class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right
        self.root = root


def load_data(filename):
    alist = []
    with open(filename, 'r') as f:
        cnt = 0
        for line in f:
            if cnt == 0:
                N = int(line)
            else:
                alist.append((int(line), cnt))
            cnt += 1
    return N, alist


def huffman_encode(weight, N):
    # node[0]: weight, node[1]: children/another node
    while len(weight) > 1:
        l, r = heapq.heappop(weight), heapq.heappop(weight)
        node = HuffmanNode(l, r)
        heapq.heappush(weight, (l[0]+r[0], node))
    return heapq.heappop(weight)


def walk_tree(node, prefix="", code={}):
    # encode the huffman code by recursive calls
    if isinstance(node[1].left[1], HuffmanNode):
        walk_tree(node[1].left, prefix + "0", code)
    else:
        code[node[1].left[1]] = prefix + "0"
    if isinstance(node[1].right[1], HuffmanNode):
        walk_tree(node[1].right, prefix + "1", code)
    else:
        code[node[1].right[1]] = prefix + "1"
    return (code)


if __name__ == '__main__':
    N, weight = load_data('huffman.txt')
    heapq.heapify(weight)
    node = huffman_encode(weight, N)
    code = walk_tree(node)

    length = []
    for i in code:
        length.append(len(code[i]))
    print(max(length), min(length))
