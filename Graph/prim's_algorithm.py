#import numpy as np
from Graph.graph import Graph



def main():
    #print(np.full([5, 5], None))

    print("Prim's Algorithm")
    g = Graph(5)
    g.create_graph_with_edges(7)
    #g.create_graph_with_edges()
    g.make_adjacency_matrix()
    print(g.temp_array)
    g.temp_array[:,3] = None # Change All Values of a Certain Columnn
    print(g.temp_array)

if __name__ == '__main__':
    main()
