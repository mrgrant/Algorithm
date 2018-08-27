# Find Single-Source Shortest Path using Dijkstra's Algorithm
def get_nodes(graph):
    nodes = set()
    for node in graph:
        nodes.add(node)
    return nodes


def dijkstra(graph, initial):
    """
    find shortest path using dijkstra's algorithm
    :param graph: input directed graph
    :param initial: start node
    :return:
    """

    visited = {initial: 0}
    path = {}
    nodes = get_nodes(graph)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph[min_node]:
            weight = current_weight + graph[min_node][edge]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[min_node] = edge
    return visited, path


if __name__ == '__main__':
    graph = {
        'S': {'V': 1, 'W': 4},
        'V': {'W': 2, 'T': 6},
        'W': {'T': 3},
        'T': {}}

    visit, path = dijkstra(graph, 'S')
    print(visit)