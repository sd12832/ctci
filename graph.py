import unittest
import random
import string
import pprint


# Class representing the Graph data strcuture
class Graph:

    def __init__(self):
        self.graph = {}

    def __str__(self):
        return str(self.graph)

    def add_vertex(self, vertex, edges=None):
        if edges is not None:
            self.graph[vertex] = edges
        else:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        if edge is not None:
            self.graph[vertex].append(edge)

    def generate_random_vertices(self, n):
        print('Generating vertices')
        ascii = list(string.ascii_letters)
        for _ in range(n):
            random_choice = random.choice(ascii)
            ascii.remove(random_choice)
            self.add_vertex(random_choice)

    def generate_random_edges(self, maximum_edges):
        print('Generating edges')
        for vertex in list(self.graph.keys()):
            available_nodes = list(self.graph.keys())
            for _ in range(random.randint(1, maximum_edges)):
                random_choice = random.choice(list(available_nodes))
                available_nodes.remove(random_choice)
                edge = random_choice
                if vertex is not edge:
                    self.add_edge(vertex, edge)


class Test(unittest.TestCase):

    def test_rand_graph(self):
        G = Graph()
        G.generate_random_vertices(20)
        G.generate_random_edges(5)
        print('The graph is ' + str(G))
        self.assertEqual(len(G.graph.keys()), 20)
        for vertex in list(G.graph.keys()):
            self.assertLessEqual(len(G.graph[vertex]), 5)


if __name__ == '__main__':
    unittest.main()