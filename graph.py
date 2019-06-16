# Christina Chan

import random


# IMPLEMENTING A GRAPH ######
class Graph(object):
    # used http://www.python-courses.eu/graphs_python.php
    # for reference (following 7 functions)
    def __init__(self, graph_dict={}):
        # initialize the Graph object
        self.__graph_dict = graph_dict

    def vertices(self):
        # return list of vertices
        return list(self.__graph_dict.keys())

    def edges(self):
        # returns edges of graph
        return self.__generate_edges()

    def add_vertex(self, vertex):
        # if the vertex does not exist in graph, add it
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        # add an edge if they are not already connected
        # assumes edge is of type tuple, list or set
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        # static method, generates edges of graph
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        # string representation of the graph
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    # METHODS NEEDED TO GENERATE A RANDOM CONNECTED GRAPH ###

    def vertices_count(self):
        # returns the number of unique vertices in graph
        return len(self.__graph_dict.keys())

    def make_randTree(self, n):
        # generate a random tree on n-vertices
        for i in range(0, n):
            # create our list of n vertices
            self.add_vertex(i)
        for j in range(1, n):  # 1 to n ensures all nodes are connected
            # make j and p neighbours
            p = random.randint(0, j - 1)
            self.add_edge({j, p})

    def add_randEdge(self, k):
        # add up to k random edges
        n = self.vertices_count()
        for i in range(1, k):
            v1 = random.randint(0, n - 1)
            v2 = random.randint(0, n - 1)
            # if v1 isn't v2, and v1 and v2 are not already neighbours
            # make v1 and v2 neighbours
            if v1 != v2:
                if v1 in self.__graph_dict:
                    self.__graph_dict[v1].append(v2)
                else:
                    self.__graph_dict[v1] = [v2]

    # METHODS NEEDED TO DETERMINE GRAPH DIAMETER ###

    def find_all_paths(self, start_v, end_v, path=[]):
        # finds all paths from start_v to end_v in graph
        graph = self.__graph_dict
        path = path + [start_v]
        if start_v == end_v:
            return [path]
        if start_v not in graph:
            return []
        paths = []
        for v in graph[start_v]:
            if v not in path:
                extended_paths = self.find_all_paths(v, end_v, path)  # recursively
                for p in extended_paths:
                    paths.append(p)  # add all of the extended_paths to original list
        return paths

    def diameter(self):
        # calculate the diameter of the graph
        # diameter is the max distance between any two pairs of vertices
        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v)) for j in range(i + 1, len(v) - 1)]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)  # orders the list
            smallest_paths.append(smallest)
        smallest_paths.sort(key=len)  # sorts the list so longest path is at the end
        diameter = len(smallest_paths[-1])
        return diameter