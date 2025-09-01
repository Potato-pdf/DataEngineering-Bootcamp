class directed_graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex in self.graph:
            return "Vertex already in graph"
        self.graph[vertex] = []
    def add_edge(self, edge):
        start = edge.get_start()
        end = edge.get_end()
        if start not in self.graph or end not in self.graph:
            raise ValueError(f"Vertex {start.get_name()} or {end.get_name()} not in graph")
        self.graph[start].append(end)

class edge:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def __str__(self):
        return self.start.get_name() + "->" + self.end.get_name()

class vertex:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name