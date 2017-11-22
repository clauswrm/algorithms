""" A solution to the all-pairs shortest path problem. """
__author__ = 'Claus Martinsen'


def floyd_warshall(adjacency_weight_matrix):
    """
    Finds the shortest path between all pairs of vertecies in a graph with no negative cycles.

    :param adjacency_weight_matrix: An n*n matrix representing the edge weights in an n-vertex
     directed graph. AWM[i][j] denotes the egde weight from vertex i to vertex j.
    :type adjacency_weight_matrix: list
    :returns: An n*n matrix where R[i][j] denotes the shortest path from vertex i to vertex j.
    :rtype: list
    """
    dist = adjacency_weight_matrix.copy()
    n = len(adjacency_weight_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == '__main__':
    # Only executed when this module is run directly
    # The following is an example of how to use the algorithm

    from math import inf  # Used to denote "no path" between two nodes

    d = [[0  , 2  , inf, inf, inf, inf],
         [inf, 0  , 1  , inf, 4  , inf],
         [-2 , inf, 0  , inf, 2  , inf],
         [inf, 4  , inf, 0  , inf, 3  ],
         [inf, inf, inf, 1  , 0  , 2  ],
         [inf, inf, inf, inf, inf, 0  ]]

    for row in floyd_warshall(d):
        print(row)
