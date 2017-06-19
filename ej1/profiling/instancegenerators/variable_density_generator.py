from . import max_edges, generate_graph, constant_cost
from trip import Trip

def f(n, k):
    max_m = max_edges(n)

    def g():
        for m in range(k, max_m):
            graph = generate_graph(n, k, density=m / max_m, generate_cost=constant_cost(30))
            trip = Trip(graph, 0, n - 1)
            yield (m, str(trip))
    return g
