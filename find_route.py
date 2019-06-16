import unittest
from graph import *
from collections import deque

def traverse(Graph, visited, queue, node1, node2):


def find_route(Graph, node1, node2):

    print('Finding route.')
    visited = {}
    queue = deque()

    if Graph[node1] is None or Graph[node2] is None:
        return False
    else:
        visited[node1] = True
        queue.append(node1)

        while queue:
            visiting = queue.dequeue()
            if visiting == node2:
                return True
            for node in Graph[visiting]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)


class Test(unittest.TestCase):

    # Dummy test in order to get the script rolling

    def test_nothing(self):
        self.assertEqual(1, 1)

    # Can't really run this test, since this would turn into a dijkstra's

    # def test_route(self):
    #     G = Graph()
    #     G.generate_random_vertices(20)
    #     G.generate_random_edges(5)
    #
    #     nodeA = random.choice(list(G.graph.keys()))
    #     nodeB = random.choice(list(G.graph.keys()))
    #
    #     while nodeA == nodeB:
    #         nodeB = random.choice(list(G.graph.keys()))
    #     route = find_route(nodeA, nodeB)
    #     prev_node = nodeA
    #     for node in route[1:]:
    #         self.assertIn(node, prev_node)
    #         prev_node = node


if __name__ == '__main__':
    unittest.main()