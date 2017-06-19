class Route:
    def __init__(self, premium, cost):
        self.premium = premium
        self.cost = cost

    def __str__(self):
        return str(int(self.premium)) + " " + str(self.cost)


class Edge:
    def __init__(self, v1, v2, data):
        self.vertices = (v1, v2)
        self.data = data


class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges


class Trip:
    def __init__(self, graph, origin, destination):
        self.graph = graph
        self.origin = origin
        self.destination = destination

        premium_routes = filter(lambda edge: edge.data.premium, self.graph.edges)

        self.k = len(premium_routes)

    def __str__(self):
        return """{n} {m}
{origin} {destination} {k}
{edges}
-1 -1""".format(
            n=self.graph.n,
            m=len(self.graph.edges),
            origin=self.origin + 1,
            destination=self.destination + 1,
            k=self.k,
            edges="\n".join(map(lambda edge: " ".join([
                str(edge.vertices[0] + 1),
                str(edge.vertices[1] + 1),
                str(edge.data)]), self.graph.edges)))

