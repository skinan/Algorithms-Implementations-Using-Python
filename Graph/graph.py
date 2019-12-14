from Graph.node import Node
from Graph.edge import Edge
import numpy as np


class Graph:
    def __init__(self, nodes):
        self.adjacency_matrix = []
        self.number_of_nodes = nodes
        self.number_of_edges = None
        self.list_of_nodes = []
        self.list_of_edges = []
        self.temp_array = np.full(shape=[nodes, nodes], fill_value=None)

    def create_nodes(self):

        for i in range(self.number_of_nodes):
            self.list_of_nodes.append(Node(i))

    def reset_node_status(self):
        for i in range(self.number_of_nodes):
            self.list_of_nodes[i].reset_node_status()

    def create_graph(self):

        for i in range(self.number_of_nodes):
            print("Enter Connections From Node " + str(i) + ":")
            temp_list = [0] * self.number_of_nodes
            connection_list = list(map(int, input().split(" ")))
            for c in connection_list:
                temp_list[c] = 1
            self.adjacency_matrix.append(temp_list)

    def print_matrix(self):

        for row in self.adjacency_matrix:
            print(row)

    def create_graph_with_edges(self, edges):
        self.number_of_edges = edges
        print("Give Input In This Order: ")
        print("Source Destination Weight")
        for i in range(self.number_of_edges):
            s, d, v = map(int, input().split(" "))
            self.list_of_edges.append(Edge(s, d, v))

    def sort_edges_by_value(self):
        self.list_of_edges.sort(key=lambda x: x.value)

    def make_adjacency_matrix(self):

        # Adjacency Matrix For Undirected Graph With Given Weight.
        #self.adjacency_matrix = [[None]*self.number_of_nodes]*self.number_of_nodes
        for i in self.list_of_edges:
            # self.adjacency_matrix[i.source_node][i.destination_node] = i.value
            # self.adjacency_matrix[i.destination_node][i.source_node] = i.value
            self.temp_array[i.source_node][i.destination_node] = i.value
            self.temp_array[i.destination_node][i.source_node] = i.value
