# Find all Strong Connected Components in O(V+E) time using Kosaraju's Two-pass algorithm
import collections


def dfs_loop(garph):
    """
    :param garph: search in the graph
    :return: finishing time dict
    """
    f = []
    seen = set()

    def dfs(node):

        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
        # set finishing time
        f.append(node)

    g = collections.OrderedDict(sorted(graph.items(), key=lambda k: k[0], reverse=True))

    for node in g:
        if node not in seen:
            seen.add(node)
            dfs(node)
    return f


def reverse(graph):
    # reverse the graph
    graph_rev = {}
    for node in graph:
        for neightbor in graph[node]:
            graph_rev.setdefault(neightbor, []).append(node)
    return graph_rev


def dfs_second(graph, f):
    """
    2nd Deep First Search
    :param graph: reversed graph
    :param f: finishing time order dict
    :return: Strong Connect Components
    """
    result = []
    seen = set()

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                dfs(neighbor)
        temp.append(node)
        return temp

    while len(f) != 0:
        node = f.pop()
        if node not in seen:
            seen.add(node)
            temp =[]
            scc = dfs(node)
            result.append(scc)
    return result


if __name__ == '__main__':
    graph = {
        1: [7],
        2: [5],
        3: [9],
        4: [1],
        5: [8],
        6: [3, 8],
        7: [4, 9],
        8: [2],
        9: [6]
    }

    graph_rev = reverse(graph)
    f = dfs_loop(graph)

    print(dfs_second(graph_rev, f))
