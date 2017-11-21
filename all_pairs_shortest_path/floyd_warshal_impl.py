__author__ = "Claus Martinsen"


def floyd_warshall(graph_weight_matrix: list):
    dist = graph_weight_matrix.copy()
    n = len(graph_weight_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]


if __name__ == '__main__':
    from math import inf # Used to denote "no path" between two nodes

    d = [[0  , 2  , inf, inf, inf, inf],
         [inf, 0  , 1  , inf, 4  , inf],
         [-2 , inf, 0  , inf, 2  , inf],
         [inf, 4  , inf, 0  , inf, 3  ],
         [inf, inf, inf, 1  , 0  , 2  ],
         [inf, inf, inf, inf, inf, 0  ]]

    floyd_warshall(d)
