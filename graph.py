from node import Node


class Graph:
    def __init__(self, num):
        self.adjacency_matrix = []
        self.number_of_nodes = num
        self.list_of_nodes = []

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





