from Tree import *
import unittest
import math


def insert_list_BST(level, array):

    if len(array) == 1:

        return BinaryTreeNode(level, array[0])

    elif len(array) == 2:

        root_node = BinaryTreeNode(level, array[1])
        left_child = BinaryTreeNode(level+1, array[0])
        root_node.add_left_child(left_child)

        return root_node

    elif len(array) > 2:

        if len(array) % 2 == 0:
            mid_index = math.ceil(len(array) / 2)
            root_node = BinaryTreeNode(level, array[mid_index])
        else:
            mid_index = math.floor(len(array) / 2)
            root_node = BinaryTreeNode(level, array[mid_index])

        print('array[0: mid_index] is ' + str(array[0: mid_index]))
        print('array[mid_index+1:] is ' + str(array[mid_index+1:]))

        root_node.add_left_child(insert_list_BST(level+1, array[0: mid_index]))
        root_node.add_right_child(insert_list_BST(level+1, array[mid_index+1:]))

        return root_node


class Test(unittest.TestCase):

    def test_basic_odd_case(self):
        array = [1, 4, 5, 8, 11, 15, 18]
        result_tree = BinaryTree(insert_list_BST(0, array))
        # result_tree.pre_order_print_node()
        tree_array = []
        result_tree.pre_order_array_creator(result_tree.root, tree_array)
        self.assertEqual(array, tree_array)


if __name__ == '__main__':
    unittest.main()