import unittest
import math

class Node():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        print('Node value is ' + str(self.value))


class Row():
    def __init__(self, values):
        self.nodes = []

        for value in values:
            node = Node(value)
            self.nodes.append(node)

    def __str__(self):
        for i, node in enumerate(self.nodes):
            print('Column ' + str(i) + ' contains' + str(node))


class Matrix():
    # We are assuming this to be a square matrix

    def __init__(self, matrix):
        print('Matrix rotation has been initialized' + '\n')
        self.matrix = []
        for i_row in matrix:
            o_row = Row(i_row)
            self.append(o_row)

    def __str(self):
        for i, row in enumerate(self.matrix):
            print('Row ' + str(i) + ' values are below' + '\n')

    def rotate(self):

        n_layers = math.floor(len(self.matrix) / 2)
        layer_id = 0
        temp = None

        while layer_id <= n_layers:
            # Per layer
            temp = self.matrix[layer_id][layer_id]
            for i, column in enumerate(self.matrix[layer_id]):
                self.matrix[layer_id][i] = self.matrix[layer_id+i][layer_id]
                self

                # Everything for each layer needs to happen in here


            layer_id += 1

        return rotated


class Test(unittest.TestCase):
    def test_matrix_rotate(self):

        # Input Matrix

        input_row1 = [1, 3, 4]
        input_row2 = [5, 7, 10]
        input_row3 = [2, 5, 2]

        input_matrix = [input_row1, input_row2, input_row3]

        # Output Matrix

        output_row1 = [2, 5, 1]
        output_row2 = [5, 7, 3]
        output_row3 = [2, 10, 4]

        output_matrix = [output_row1, output_row2, output_row3]

        matrix = Matrix(input_matrix)

        output_result = matrix.rotate()

        self.assertEqual(output_result, output_matrix)


if __name__ == '__main__':
    unittest.main()