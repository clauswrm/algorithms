""" An implementation of the Edmonds-Karp algorithm to find maximum flow. """
__author__ = 'Claus Martinsen'

from math import inf
from collections import deque


def edmonds_karp(capacity_matrix, s, t):
    """
    Finds the maximum flow (i.e. the maximum throughput) from node a to node b
    given a matrix of the capacity between the nodes.

    The Edmonds-Karp algorithm is an implementation of the Ford-Fulkerson
    method.

    :param capacity_matrix: An n*n matrix where m[i][j] indicates the capacity
     from node i to node j and n is the total number of nodes in the graph.
    :type capacity_matrix: list
    :param s: The source/start node.
    :type s: int
    :param t: The drain/end node.
    :type t: int
    :return: An n*n matrix of maximum flow where m[i][j] indicates the flow
     from node i to node j.
    :rtype: list
    """
    n = len(capacity_matrix)
    queue = deque()
    flow_net = [[0 for _ in range(n)] for _ in range(n)]
    residual_net = [[capacity_matrix[y][x] for x in range(n)] for y in range(n)]
    augmenting_values = [0 if x != t else -1 for x in range(n)]

    while augmenting_values[t] != 0:  # While we find an augmenting path
        # Reset the values
        predecesor_values = [None for _ in range(n)]
        augmenting_values = [0 for _ in range(n)]
        augmenting_values[s] = inf
        queue.clear()
        queue.appendleft(s)

        while augmenting_values[t] == 0 and queue:
            # While we have not augmented the drain, or run out of nodes
            u = queue.pop()
            for v in range(n):  # Try to push more flow
                if u != v and capacity_matrix[u][v] != 0 or capacity_matrix[v][u] != 0:
                    if capacity_matrix[u][v] != 0:
                        residual_net[u][v] = capacity_matrix[u][v] - flow_net[u][v]
                    else:
                        residual_net[u][v] = flow_net[v][u]
                    if residual_net[u][v] > 0 and augmenting_values[v] == 0:
                        if augmenting_values[u] < residual_net[u][v]:
                            augmenting_values[v] = augmenting_values[u]
                        else:
                            augmenting_values[v] = residual_net[u][v]
                        predecesor_values[v] = u
                        queue.appendleft(v)

        u, v = predecesor_values[t], t
        while u is not None:  # Update the flow in the augmenting path
            if capacity_matrix[u][v] != 0:
                flow_net[u][v] = flow_net[u][v] + augmenting_values[t]
            else:
                flow_net[v][u] = flow_net[v][u] - augmenting_values[t]
            u, v = predecesor_values[u], u

    return flow_net


def get_node_flow(flow_net, node):
    """
    Returns the sum of the flow into minus the sum of the flow out from the
    node.

    In a maximum flow network, this function returns 0 for all nodes except
    for the source (wich returns -max_flow) and drain (wich returns max_flow).
    """
    flow = 0
    n = len(flow_net)
    for i in range(n):
        flow += flow_net[i][node]
        flow -= flow_net[node][i]
    return flow


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    a = [[0, 13, 13, 0, 0, 0],
         [0, 0, 0, 14, 0, 0],
         [0, 4, 0, 9, 12, 0],
         [0, 0, 0, 0, 0, 4],
         [0, 0, 0, 7, 0, 20],
         [0, 0, 0, 0, 0, 0]]

    source_node, drain_node = 0, 5
    flow_network = edmonds_karp(a, source_node, drain_node)

    for row in flow_network:
        print(row)

    print('Maximum flow:', get_node_flow(flow_network, drain_node))
