__author__ = 'solomina'


def transform_matrix(a):
    """
    Transpose and print a matrix
    initial matrix [[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12]]
    result matrix [[1, 5, 9],
                    [2, 6, 10],
                    [3, 7, 11],
                    [4, 8, None]]
    :param a: [[1,2,3,4],[5,6,7,8],[9,10,11]]
    :return: None
    Expected result: (#1 is the best solution)
        [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, None]]
        TUPLES [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, None)]
        ZIP [(1, 5, 9), (2, 6, 10), (3, 7, 11)]
    """
    # list_of_lists
    print map(lambda *i: list(i), *a)

    # list_of_ tuples
    print "TUPLES", map(None, *a)

    # ome_values_missing
    print "ZIP", zip(*a)

init_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

if __name__ == '__main__':
    transform_matrix(init_list)
