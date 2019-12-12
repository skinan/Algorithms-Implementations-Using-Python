from graph import Graph
from collections import deque


def bfs(graph):

    graph_length = graph.number_of_nodes
    adj_matrix = graph.adjacency_matrix
    node_objects = graph.list_of_nodes
    
    queue = deque()
    
    queue.appendleft(2)
    print("The Traversal Order For Breadth First Search Is: ", end="")
    while len(queue) != 0:
        node = queue.pop()
        node_objects[node].mark_node()
        print(node, end=" ")
        for i in range(graph_length):
            if adj_matrix[node][i] == 1 and node_objects[i].status is False:
                node_objects[i].mark_node()
                queue.appendleft(i)
    print()


def dfs_search(graph, node, stack):
    graph_length = graph.number_of_nodes
    adj_matrix = graph.adjacency_matrix
    node_objects = graph.list_of_nodes

    for i in range(graph_length):
        if adj_matrix[node][i] == 1 and node_objects[i].status is False:
            node_objects[i].mark_node()
            stack.append(i)
            dfs_search(graph, i, stack)


def dfs(graph):
    node_objects = graph.list_of_nodes
    stack = []
    ans = []
    node = 2
    stack.append(2)
    node_objects[2].mark_node()
    while len(stack) != 0:
        dfs_search(graph, node, stack)
        node = stack.pop()
        ans.append(node)
    print("The Traversal Order For Depth First Search: ", end=" ")
    for i in reversed(ans):
        print(i, end=" ")
    print()


def main():
    num = int(input("What is the number nodes of your graph? : "))
    g = Graph(num)
    g.create_graph()
    print("Adjacency Matrix For This Graph Is:")
    g.print_matrix()
    g.create_nodes()
    bfs(g)
    g.reset_node_status()
    dfs(g)


if __name__ == '__main__':
    main()
