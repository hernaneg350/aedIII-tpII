import random

class Route2:
    def __init__(self, tollbooth_cost):
        self.tollbooth_cost = tollbooth_cost

    def __str__(self):
        return str(self.tollbooth_cost)

class Edge:
    def __init__(self, v1, v2, data):
        self.vertices = (v1, v2)
        self.data = data

class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

def print_graph(graph):
    return """{n} {m}
{edges}
-1 -1""".format(n=graph.n, m=len(graph.edges), edges="\n".join(map(lambda edge: " ".join([str(edge.vertices[0]), str(edge.vertices[1]), str(edge.data)]), graph.edges)))

def subgraph_edges(base_n, n, m, max_c):
    for v1 in range(base_n, base_n + n):
        v2 = (v1 + 1) % n
        yield Edge(v1, v2, Route2(0))

    possible_edges = [Edge(v1, v2, Route2(max_c)) for v1 in range(base_n, base_n + n) for v2 in range(base_n, v1) + range(v1 + 2, base_n + n)]
    random.shuffle(possible_edges)
    for additional_edge_index in range(0, m):
        additional_edge = possible_edges[additional_edge_index]
        yield Edge(v1, v2, Route2(0))

def max_additional_edges(n):
    return (n * (n - 1)) - n

def generate_graph_density(n, density, connected_components, max_c):
    edges = []

    for connected_component_index in range(0, connected_components):
        base_connected_component_vertices = n // connected_components
        this_connected_component_vertices = base_connected_component_vertices

        if connected_component_index == connected_components - 1:
            this_connected_component_vertices += n % connected_components

        vertex_base = connected_component_index * (base_connected_component_vertices)

        edge_count = int(max_additional_edges(this_connected_component_vertices) * density)
        edges.extend(subgraph_edges(vertex_base, this_connected_component_vertices, edge_count, max_c))

    return Graph(n, edges)

def generate_graph_m(n, m, connected_components, max_c):
    edges = []

    for connected_component_index in range(0, connected_components):
        base_connected_component_vertices = n // connected_components
        this_connected_component_vertices = base_connected_component_vertices

        if connected_component_index == connected_components - 1:
            this_connected_component_vertices += n % connected_components

        vertex_base = connected_component_index * (base_connected_component_vertices)

        base_edge_count = base_connected_component_vertices * (connected_components - 1)
        odd_edge_count = (base_connected_component_vertices + n % connected_components)
        edge_count = (m - (base_edge_count + odd_edge_count)) // connected_components

        if connected_component_index == connected_components - 1:
            edge_count += (m - (base_edge_count + odd_edge_count)) % connected_components

        edges.extend(subgraph_edges(vertex_base, this_connected_component_vertices, edge_count, max_c))

    return Graph(n, edges)

def XXX(min_c, max_c):
    def g():
        for n in range(min_n, max_n + 1):
            instance = generate_graph(n, (n * (n - 1)) / 2 - (n - 1), 3, 100)
            yield (n, print_graph(instance))
    return g

def variable_components_generator(max_conn):
    def g():
        for conn in range(1, max_conn + 1):
            n = 600
            max_c = 100
            m = n
            instance = generate_graph_m(n, m, conn, max_c)
            yield (conn, print_graph(instance))
    return g

def grow_n_generator(min_n, max_n, density):
    def g():
        for n in range(min_n, max_n + 1):
            max_c = 100
            connected_components = 1
            instance = generate_graph_density(n, density, connected_components, max_c)
            yield (n, print_graph(instance))
    return g
