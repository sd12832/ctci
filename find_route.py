import unittest
from graph import *

def find_route(graph, node1, node2):

    print('Finding route.')
    queue = []




class Test(unittest.TestCase):

    def test_route(self):
        rand_graph = Graph()
        rand_graph.make_randTree(20)
        rand_graph.add_randEdge(20)
        find_route(3, 15)
        paths = rand_graph.find_all_paths(4,15)
        print(paths)


if __name__ == '__main__':
    unittest.main()