from . import generate_graph, constant_cost
from trip import Trip


def f(k, min_n, max_n):
    def g():
        for n in range(min_n, max_n):
            graph = generate_graph(n, k, density=0.5, generate_cost=constant_cost(30))
            trip = Trip(graph, 0, n - 1)
            yield (n, str(trip))
    return g