class TreeNode:

    def __init__(self, level, value, child_vals):

        print('creating a node with the value ' + str(value))
        self.value = value
        self.level = level
        self.child_nodes = []

        if child_vals:
            for child_val in child_vals:
                self.child_nodes.append(TreeNode(self.level + 1,
                                                 child_val, []))

    def add_child(self, node):
        self.child_nodes.append(node)

    def __str__(self):
        print('Node value is ' + str(self.value) + '. Node level is '
              + str(self.level))


class BinaryTreeNode:

    def __init__(self, level, value, left_child_val=None,
                 right_child_val=None):

        print('creating a node with the value ' + str(value))
        self.value = value
        self.level = level
        self.left_child = None
        self.right_child = None

        if left_child_val:
            self.left_child = BinaryTreeNode(level + 1, left_child_val)

        if right_child_val:
            self.right_child = BinaryTreeNode(level + 1, right_child_val)

    def add_left_child(self, node):
        print('adding left child ' + str(node.value))
        self.left_child = node

    def add_right_child(self, node):
        print('adding right child ' + str(node.value))
        self.right_child = node

    def __str__(self):
        print('Node value is ' + str(self.value) + '. Node level is '
              + str(self.level))


class Tree:

    def __init__(self, node):
        print('creating a tree' + '\n')
        self.root = node

    def pre_order_print_node(self, root_node):
        print(' ' * 4 * root_node.level +  root_node.value)
        if root_node.child_nodes is not None:
            for child_node in root_node.child_nodes:
                self.pre_order_print_node(child_node)

    def __str__(self):
        print('printing out the tree' + '\n')
        self.pre_order_print_node(self.root)


class BinaryTree:

    def __init__(self, node):
        print('creating a tree' + '\n')
        self.root = node

    def in_order_print_node(self, root_node=None):

        if root_node is None:
            root_node = self.root

        if root_node.left_child:
            print(root_node.left_child + ',')

        self.in_order_print_node(root_node.value + ',')

        if root_node.right_child:
            self.in_order_print_node(root_node.right_child)

    def pre_order_print_node(self, root_node=None):

        if root_node is None:
            root_node = self.root

        print(' ' * 4 * root_node.level + str(root_node.value))

        if root_node.left_child:
            self.pre_order_print_node(root_node.left_child)

        if root_node.right_child:
            self.pre_order_print_node(root_node.right_child)

    def pre_order_array_creator(self, root_node=None, array=[]):

        if root_node is None:
            root_node = self.root

        if root_node.left_child:
            self.pre_order_array_creator(root_node.left_child, array)

        if root_node.value is not None:
            array.append(root_node.value)

        if root_node.right_child:
            self.pre_order_array_creator(root_node.right_child, array)

    def __str__(self):
        print('printing out the tree' + '\n')
        self.pre_order_print_node(self.root)







