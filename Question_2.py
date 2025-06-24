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


class Person:
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

    def get_person_detail(self):
        return (f"Name  : {self.name}\n"
                f"Age   : {self.age}\n"
                f"Gender: {self.gender}\n"
                f"E-mail: {self.email}")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


alice = Person("Alice", "20", "Female", "alice20@gmail.com")
ben = Person("Ben", "21", "Male", "ben21@gmail.com")
chloe = Person("Chloe", "22", "Female", "chloe22@gmail.com")
alex = Person("Alex", "20", "Male", "alex20@gmail.com")
emma = Person("Emma", "19", "Female", "emma19@gmail.com")
