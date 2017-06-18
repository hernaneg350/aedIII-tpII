import random

class Route3:
    def __init__(self, present, cost):
        self.present = present
        self.cost = cost

    def __str__(self):
        return ("1" if self.present else "0") + " " + str(self.cost)

class Edge:
    def __init__(self, v1, v2, data):
        self.vertices = (v1, v2)
        self.data = data

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

def print_graph(graph):
    return """{n}
{edges}
-1""".format(n=graph.n, edges="\n".join(map(lambda edge: " ".join([str(edge.vertices[0] + 1), str(edge.vertices[1] + 1), str(edge.data)]), graph.edges)))

def generate_graph(n, density):
    edge_pairs = []

    for v1 in range(0, n):
        for v2 in range(v1 + 1, n):
            edge_pairs.append((v1, v2))

    random.shuffle(edge_pairs)
    max_edge_count = (n * (n - 1)) / 2
    edge_count = int(max_edge_count * density)

    return Graph(n, [Edge(edge_pairs[i][0], edge_pairs[i][1], Route3(i < edge_count, random.randint(1, 20))) for i in range(0, len(edge_pairs))])

def variable_density_generator(calc_count):
    def g():
        n = 300

        density = 0.0
        instance = generate_graph(n, density)
        yield (density, print_graph(instance))

        for calc in range(1, calc_count):
            density = 1.0 / calc
            instance = generate_graph(n, density)
            yield (density, print_graph(instance))

    return g

def grow_n_generator(min_n, max_n, density):
    def g():
        for n in range(min_n, max_n + 1):
            max_c = 100
            connected_components = 1
            instance = generate_graph_density(n, density, connected_components, max_c)
            yield (n, print_graph(instance))
    return g
