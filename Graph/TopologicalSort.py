def topological_sort(graph, node):
    result = []
    seen = set()

    def recusive(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recusive(neighbor)
        result.insert(0, node)

    recusive(node)
    return result


if __name__ == '__main__':
    graph = {
        "a": ["b", "c", "d"],
        "b": [],
        "c": ["d"],
        "d": []
    }
    print(topological_sort(graph, 'a'))

