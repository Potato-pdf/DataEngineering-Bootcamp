class directed_graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex in self.graph:
            return "Vertex already in graph"
        self.graph[vertex] = []
    def add_edge(self, edge):
        # You can implement edge addition logic here
        # For now, just pass to avoid syntax errors
        pass

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