def groupify(binary_matrix):
    """
    Finds all distinct groups of 1's in a 2x2 binary matrix
    :param binary_matrix: A 2x2 binary matrix
    :type binary_matrix: list
    :return: A matrix with all nodes, arranged in a disjoint set forest
    :rtype: list
    """

    n, m = len(binary_matrix), len(binary_matrix[0])
    set_matrix = [[None for _ in range(m)] for _ in range(n)]

    for i, row in enumerate(binary_matrix):
        for j, cell in enumerate(row):
            if cell == 1:
                set_matrix[i][j] = Node(j, i)

    for i in range(n):
        for j in range(m):
            if set_matrix[i][j]:
                for k in range(i + 1, i - 2, -1):
                    for l in range(j + 1, j - 2, -1):
                        if n > k >= 0 and m > l >= 0:
                            if set_matrix[k][l]:
                                set_matrix[i][j].union(set_matrix[k][l])
    return set_matrix


def get_set_forest(set_matrix):
    set_forest = set()

    for row in set_matrix:
        for cell in row:
            if cell:
                set_forest.add(cell.parent)
    return set_forest


if __name__ == '__main__':
    from random import choice

    def main(matrix):
        set_matrix = groupify(matrix)
        for row in set_matrix:
            for cell in row:
                print(cell if cell else '.', end='')
            print()

        print(get_set_forest(set_matrix))


    """ MATRICIES """
    M1 = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1],
          [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

    M2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    M3 = [[0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
          [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

    M4 = [[1, 1],
          [1, 1],
          [1, 1],
          [1, 1],
          [0, 0],
          [1, 1]]

    M5 = [[1, 0, 1],
          [1, 1, 0],
          [1, 0, 0]]

    M6 = [[1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1]]

    _l = [0,0,0,0,0,0,1]
    n, m = 100, 100
    M7 = [[choice(_l) for _ in range(m)] for _ in range(n)]
    """ END MATRICIES """

    main(M1)
