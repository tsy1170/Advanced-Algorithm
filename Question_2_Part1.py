class UDGraph:
    def __init__(self):
        self.adj_list = dict()

    def addVertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
        else:
            print("Vertex already exists")

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adj_list and to_vertex in self.adj_list:
            self.adj_list[from_vertex].append(to_vertex)
        else:
            raise ValueError("One or both vertices not founded!")

    def listOutGoingAdjacentVertex(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list.get(vertex, [])
        else:
            print("Vertex not founded")

    def print_adj_list(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
