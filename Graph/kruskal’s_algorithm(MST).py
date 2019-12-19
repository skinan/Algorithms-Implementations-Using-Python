from Graph.graph import Graph


def krushkal_algo(graph):
    edge_count = 0
    mst_list = []  # List to maintain MST(Minimum Spanning Tree).
    num_nodes = graph.number_of_nodes
    check_list = []  # A List To Identify Cycles.

    for i in range(num_nodes):
        check_list.append({i})

    # print(check_list)
    for e in graph.list_of_edges:
        if edge_count == num_nodes - 1:
            break
        elif check_list[e.source_node].isdisjoint(check_list[e.destination_node]):
            check_list[e.source_node] = check_list[e.source_node] | check_list[e.destination_node]  # Union Operation 
            # Set of connections for source and destination are same because of being undirected graph.
            for i in check_list[e.source_node]:
                check_list[i] = check_list[e.source_node]
            # Consider the following edge connection as a part of Minimum Spanning Tree.
            mst_list.append(e)
            # Count how many edges or connection are added till now in MST.
            edge_count += 1
    print()
    print("Minimum Spanning Tree:")
    for answer in mst_list:
        print("Source --> Destination == Weight: ", answer.source_node, "-->", answer.destination_node,
              "==", answer.value)


def main():
    g = Graph(int(input("Enter Number Of Nodes of Your Graph: ")))
    g.create_graph_with_edges(int(input("Enter The Number Of Edges : ")))  # Take The Graph Input
    g.sort_edges_by_value()  # Sort The Edges By Weight
    krushkal_algo(g)


if __name__ == '__main__':
    main()
