class UDGraph:
    def __init__(self):
        self.adj_list = dict()

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)
        else:
            raise ValueError("One or both vertices not founded!")

    def listOutGoingAdjacentVertex(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list.get(vertex, [])

    def print_adj_list(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")


g = UDGraph()
vertex = ['A', 'B', 'C', 'D']

for i in range(len(vertex)):
    g.addVertex(vertex[i])

g.addEdge(vertex[0], vertex[1])
g.addEdge(vertex[0], vertex[2])
g.addEdge(vertex[0], vertex[3])
g.addEdge(vertex[1], vertex[0])
g.addEdge(vertex[1], vertex[2])
g.addEdge(vertex[1], vertex[3])
g.addEdge(vertex[2], vertex[1])
g.addEdge(vertex[2], vertex[3])
g.addEdge(vertex[3], vertex[2])

g.print_adj_list()
print()
print(g.listOutGoingAdjacentVertex(vertex[0]))

