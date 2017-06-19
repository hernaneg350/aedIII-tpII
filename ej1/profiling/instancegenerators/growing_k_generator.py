from . import generate_graph, constant_cost
from trip import Trip


def f(n, max_k):
    def g():
        for k in range(0, max_k):
            graph = generate_graph(n, k, density=0.5, generate_cost=constant_cost(30))
            trip = Trip(graph, 0, n - 1)
            yield (k, str(trip))
    return g
