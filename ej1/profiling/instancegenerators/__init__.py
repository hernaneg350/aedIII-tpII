import random
from trip import Trip, Graph, Route, Edge


def max_edges(n):
    return (n * (n - 1)) / 2


def max_additional_edges(n):
    return max_edges(n) - (n - 1)


def is_last(connected_component_index, connected_component_count):
    return connected_component_index == connected_component_count - 1


def random_cost(min, max):
    def cost_generator(edge_index):
        return random.randint(1, 50)
    return cost_generator


def constant_cost(constant):
    def cost_generator(edge_index):
        return constant
    return cost_generator


def incremental_cost(min, max):
    def cost_generator(edge_index):
        return edge_index
    return cost_generator


def generate_graph_with_density(n, k, density, generate_cost):
    possible_edges = [(v1, v2) for v1 in range(0, n) for v2 in range(v1 + 1, n)]
    max_edge_count = int(float(max_edges(n)) * density)
    random.shuffle(possible_edges)
    graph_edges = possible_edges[0:max_edge_count]
    graph_edges = map(lambda (i, edge): Edge(edge[0], edge[1], Route(i < k, generate_cost(i))), enumerate(graph_edges))
    return Graph(n, graph_edges)


def connected_component_edges(base_n, n, m, k, generate_cost):
    v0 = base_n
    edge_index = 0
    for v1 in range(base_n + 1, base_n + n):
        yield Edge(v0, v1, Route(edge_index < k, generate_cost(edge_index)))
        edge_index += 1

    additional_edges = [(v1, v2) for v1 in range(v0 + 1, base_n + n) for v2 in range(v1 + 1, base_n + n)]
    random.shuffle(additional_edges)
    for additional_edge_index in range(0, m):
        additional_edge = additional_edges[additional_edge_index]
        yield Edge(additional_edge[0], additional_edge[1], Route(edge_index < k, generate_cost(edge_index)))
        edge_index += 1


def generate_general_graph(n, k, density, connected_component_count, generate_cost):
    edges = []

    base_connected_component_vertex_count = n // connected_component_count
    last_connected_component_vertex_count = base_connected_component_vertex_count + (n % connected_component_count)

    for connected_component_index in range(0, connected_component_count):
        this_connected_component_vertex_count = base_connected_component_vertex_count

        if is_last(connected_component_index, connected_component_count):
            this_connected_component_vertex_count = last_connected_component_vertex_count

        start_vertex = connected_component_index * base_connected_component_vertex_count

        edge_count = int(max_additional_edges(this_connected_component_vertex_count) * density)
        edges.extend(connected_component_edges(start_vertex, this_connected_component_vertex_count, edge_count, k, generate_cost))
        k -= edge_count

    return Graph(n, edges)


def generate_graph(n, k, density, connected_component_count=None, generate_cost=random_cost(1, 50)):
    if connected_component_count is None:
        return generate_graph_with_density(n, k, density, generate_cost)
    else:
        return generate_general_graph(n, k, density, connected_component_count, generate_cost)


from variable_cost_generator import f as variable_cost_generator
from variable_density_generator import f as variable_density_generator
from growing_k_generator import f as growing_k_generator
from growing_n_generator import f as growing_n_generator
