# Purpose: Learn and provide examples of Graphs

# What is a Graph?
"""
A graph is a non-linear data structure represented by Nodes (Vertex)
    that are connected by Edge's
An undirected graph is a graph in which edges do not have a direction
A directed graph is a graph in which the edges DO have a direction
If two nodes are connected by an edge, they have an adjacency
Graphs could also be unweighted or weighted
    This means that edges could have values assigned to them (weighted)
"""

# How can Graphs be represented?
"""
Adjacency Matrix:
    Could be a 2D Array where 0/1 represents the adjacency between nodes

       A   B   C
    A  0   1   0
    B  1   0   1
    C  0   1   0

Adjacency List:
    Could be represented by an array of linked lists
    The head of each linked list in the array is a node in the graph
        and it points to each adjacency it has
    
    A -> B
    B -> A -> C
    C -> B

    In Python, we could also use a dictionary:

    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
"""

# What is a Graph useful for?
"""
LOTS of different use cases:
    -Social Network (friendship connections)
    -Communication Network
    -Street Map
    -Relations between objects/people/networks
"""

# Graph operations and space
"""
Adjacency Matrix:
    Access: O(1)
    Insert:
        Vertex: O(V^2)
        Edge: O(1)
    Delete:
        Vertex: O(V^2)
        Edge: O(1)
    Space: O(V^2)

Adjacency List:
    Access: O(V) 
    Insert:
        Vertex: O(1)
        Edge: O(1)
    Delete:
        Vertex: O(V+E)
        Edge: O(E)
    Space: O(V + E)
"""

def main():
    pass

if __name__ == "__main__":
    main()