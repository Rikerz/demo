# https://leetcode.com/discuss/interview-question/436073/
from collections import defaultdict


def find_critical_nodes(num_nodes, num_edges, edges):
    # If we are missing a parameter, there is nothing to return.
    if not (num_nodes and num_edges and edges):
        return []

    # Do DFS from each node blacklisting node + 1 from the DFS.
    # If the DFS doesn't find every other node,
    # the blacklisted node is critical.
    connections_map = defaultdict(list)
    for edge in edges:
        connections_map[edge[0]].append(edge[1])
        connections_map[edge[1]].append(edge[0])

    def traverse(node, visited_nodes, blacklisted_node):
        visited_nodes.add(node)
        connections = connections_map[node]
        for connected_node in connections:
            if (
                connected_node == blacklisted_node
                or connected_node in visited_nodes
            ):
                continue

            traverse(connected_node, visited_nodes, blacklisted_node)

    critical_nodes = []
    for start_node in range(num_nodes):
        blacklisted_node = (start_node + 1) % num_nodes
        visited_nodes = set()
        traverse(start_node, visited_nodes, blacklisted_node)
        if len(visited_nodes) < (num_nodes - 1):
            critical_nodes.append(blacklisted_node)

    return critical_nodes
