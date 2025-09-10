class graphs:

    def __init__(self) -> None:
        
        self.adj_list = {}

    def add_vertex(self , vertex):

        if vertex not in self.adj_list:

            self.adj_list[vertex] = []


    
    def add_edges(self , vertex_1 , vertex_2 , weight):

        self.add_vertex(vertex=vertex_1)
        self.add_vertex(vertex=vertex_2)

        self.adj_list[vertex_1].append((vertex_2 , weight))
        self.adj_list[vertex_2].append((vertex_1 , weight))

    def display_graph(self):

        for vertex in self.adj_list:

            print(f"{vertex} --> {self.adj_list[vertex]}")


g1 = graphs()

g1.add_vertex("A")
g1.add_vertex("Z")
g1.add_vertex("C")
g1.add_vertex("F")

g1.add_edges("A" , "F" , 9)  # A --> F
g1.add_edges("C" , "Z" , 8)  # C --> Z
g1.add_edges("A" , "Z" , 6)  # A --> Z

g1.display_graph()
