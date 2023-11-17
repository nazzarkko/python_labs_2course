def topological_sort_for_govern(graph):
    def our_dfs_function(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                our_dfs_function(neighbor)
        result.append(node)

    visited = set()
    result = []

    for node in graph:
        if node not in visited:
            our_dfs_function(node)

    return result

with open("governin.txt", "r") as file:
    input_data = file.read().splitlines()

our_graph = {}

for line in input_data:
    node, neighbor = line.split()
    if node not in our_graph:
        our_graph[node] = []
    our_graph[node].append(neighbor)

result_order = topological_sort_for_govern(our_graph)

with open("governout.txt", "w") as file:
    file.write("\n".join(result_order))
