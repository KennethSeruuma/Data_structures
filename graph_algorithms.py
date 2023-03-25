# graphs and their representation

num_nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 4), (0, 4), (1, 3)]

# adjacency lists
# 0 : 1,4
# 1 : 0,2,3,4
# 2 : 1,3
# 3 : 1,2,4
# 4 : 0,1,3

# lets create a class to represent a graph as an adjacent list 

class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(len(num_nodes))]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def add_edge(self, edge):
        n1, n2 = edge
        self.data[n1].append(n2)
        self.data[n2].append(n1)
    def remove_edge(self, edge):
        n1, n2 = edge
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)
    def to_adjacency_matrix(self):
        n = len(num_nodes)
        table = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i in self.data[j]:
                    table[i][j] = 1
                else:
                    table[i][j] = 0
        return table

    def __repr__(self):
        return "\n".join(["{} : {}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()

#graph1 = Graph(num_nodes, edges)
#print (graph1)

# Qn. write a function to add an edge to a graph represented 
# as an adjacency list; i have included it in the code
# Qn. write a function to remove an edge from a graph represented as an adjaceny list


#edge = (0, 3)
#graph1.add_edge(edge)
#print(graph1)
#graph1.remove_edge(edge)
#print(graph1)

# adjacency matrix
# represent a graph as an adjacency matrix; i added it to the code
#print(graph1.to_adjacency_matrix())

# Breadth First Search BFS
def bfs(graph, root):
    queue = []
    discovered = [False] * len(graph.data)
    discovered[root] = True
    distance = [None] * len(graph.data)
    queue.append(root)
    distance[root] = 0
    parent = [None] * len(graph.data)
    idx = 0
    while idx < len(queue):
        # dequeue
        current = queue[idx]
        idx += 1
        # check all edges of current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)
    return queue, distance, parent

#print(bfs(graph1, 3))

# write a program to check if all the nodes in the graph are connected

# DFS

def dfs(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []

    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result

#print(dfs(graph1, 3)) 

# write a program to detect a cycle in a graph
# a cycle is a path that leads a node to it'self

# weighted and directed graphs

class graph:
    def __init__(self, num_nodes, edges, weighted=False, directed=False):
        self.num_nodes = num_nodes
        self.weighted = weighted
        self.directed = directed 
        self.data = [[] for _ in range(len(num_nodes))]
        self.weight = [[] for _ in range(len(num_nodes))]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{} : {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result += "{} : {}\n".format(i, nodes)
        return result
    def __str__(self):
        return self.__repr__()

#graph2 = graph(num_nodes, edges)
#print(graph2)

num_nodes3 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
edges3 = [(0,1,3),(0,3,2),(0,8,4),(1,7,4),(2,7,2),(2,3,6),(2,5,1),(3,4,1),(4,8,8),(5,6,8)]

graph3 = graph(num_nodes3, edges3, weighted=True)
#print(graph3)

#num_nodes4 = [0, 1, 2, 3, 4]
#edges4 = [(0,1),(1,2),(2,3),(2,4),(4,2),(3,0)]

#graph4 = graph(num_nodes4, edges4, directed=True)
#print(graph4)

# Qn. write a function to find the length of the shortest 
# path between two nodes in a weighted directed graph

def update_distances(graph, current, distance, parent=None):
    # update distances of current node neighbors
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current
def pick_next_node(distance, visited):
    # pick the next un visited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node         
            min_distance = distance[node]
    return min_node

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []
    distance[source] = 0
    queue.append(source)
    idx = 0

    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        visited[current] = True
        idx += 1
        # update distances of all the neighbors
        update_distances(graph, current, distance, parent)
        # find the first unvisited node with the smallest distance
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

    return distance[target], parent

num_nodes7 = [0,1,2,3,4,5]
edges7 = [(0,1,4),(0,2,2),(1,2,5),(1,3,10),(2,4,3),(4,3,4),(3,5,11)]
graph7 = graph(num_nodes7, edges7, weighted=True, directed=True)

#print(graph7)

#print(shortest_path(graph7, 0, 5))
#print(shortest_path(graph3, 0, 7))
print(shortest_path(graph3, 2, 8))

# implement a binary heap, to overcome the inefficiencies in 
# performing a shortest_path algorithm i.e, (n+m)n
# it has a min heap, and or, a max heap
