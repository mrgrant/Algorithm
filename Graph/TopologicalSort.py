def topological_sort(graph, node):
    result = []
    seen = set()

    def recusive_helper(node):
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                recusive_helper(neighbor)
        result.insert(0, node)

    recusive_helper(node)
    return result


if __name__ == '__main__':
    graph = {1: [3], 3: [5, 6], 5: [4], 4: [7], 7: [], 6: []}
    print(topological_sort(graph, 1))

