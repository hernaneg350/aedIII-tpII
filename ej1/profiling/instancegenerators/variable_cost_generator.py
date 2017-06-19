from . import generate_graph, random_cost
from trip import Trip


def f(n, k, max_iterations):
    def g():
        for iteration in range(0, max_iterations):
            graph = generate_graph(n, k, density=0.5, generate_cost=random_cost(1, 50))
            trip = Trip(graph, 0, n - 1)
            yield (iteration, str(trip))
    return g
