import unittest
from Tree import *
from list2BST import *


def traverse_DFS(root, target_node_value, hash_route):
    # print('looking at node ' + str(root.value))
    if root.value == target_node_value:
        # print('found node ' + str(target_node_value))
        hash_route[root.value] = 1
        return 1
    else:
        if root.left_child:
            left_result = traverse_DFS(root.left_child, target_node_value,
                                       hash_route)
            if left_result == 1:
                hash_route[root.value] = 1
                return 1
        if root.right_child:
            right_result = traverse_DFS(root.right_child, target_node_value,
                                        hash_route)
            if right_result == 1:
                hash_route[root.value] = 1
                return 1


common_ancestor = None


def hash_check_DFS(root, target_node_value, hash_route):
    global common_ancestor

    if root.value == target_node_value:
        if root.value in hash_route:
            print('Found a common ancestor ' + str(root.value))
            if common_ancestor is None:
                common_ancestor = root.value
        return 1
    else:
        if root.left_child:
            left_result = hash_check_DFS(root.left_child, target_node_value,
                                         hash_route)
            if left_result == 1:
                if root.value in hash_route:
                    if common_ancestor is None:
                        print('Found a common ancestor ' + str(root.value))
                        common_ancestor = root.value
                return 1

        if root.right_child:
            right_child = hash_check_DFS(root.right_child, target_node_value,
                                         hash_route)

            if right_child == 1:
                if root.value in hash_route:
                    if common_ancestor is None:
                        print('Found a common ancestor ' + str(root.value))
                        common_ancestor = root.value
                return 1


def find_common_node(Tree, node1, node2):
    global common_ancestor

    print('Running the common ancestry finder')

    # First run DFS v1 with Hash
    hash_route= {}

    print('This value of node1 is ' + str(node1))
    traverse_DFS(Tree.root, node1, hash_route)

    print(hash_route)

    common_ancestor = None
    hash_check_DFS(Tree.root, node2, hash_route)
    if common_ancestor:
        return common_ancestor
    else:
        return None


class Test(unittest.TestCase):

    def test_basic_odd_case(self):
        array = [1, 4, 5, 8, 11, 15, 18]
        result_tree = BinaryTree(insert_list_BST(0, array))
        result_node = find_common_node(result_tree, 1, 18)
        self.assertEqual(result_node, 8)

    def test_basic_even_case(self):
        array = [1, 4, 5, 8, 11, 15, 18, 20]
        result_tree = BinaryTree(insert_list_BST(0, array))
        result_node = find_common_node(result_tree, 1, 8)
        self.assertEqual(result_node, 5)


if __name__ == '__main__':
    unittest.main()