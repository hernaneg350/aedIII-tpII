import sys

class UDS:
    def __init__(self, n):
        self.height = [1 for i in range(0, n)]
        self.parent = [i for i in range(0, n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.height[x] < self.height[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x

        if self.height[x] == self.height[y]:
            self.height[x] += 1


n = int(sys.stdin.readline())

def read_edge(line):
    edge_data = line.split(' ')
    return tuple(map(lambda x: int(x), edge_data))


def edges_from_input():
    construction_queue = []
    destruction_queue = []
    for edge_line in sys.stdin:
        edge = read_edge(edge_line)
        v1 = edge[0]
        v2 = edge[1]
        is_present = edge[2] == 1
        weight = edge[3]

        if is_present:
            destruction_queue.append((v1, v2, weight))
        else:
            construction_queue.append((v1, v2, weight))

    return (construction_queue, destruction_queue)


class KruskalAlgorithm:

    def __init__(self, n, construction_queue, destruction_queue):
        self.destruction_queue = sorted(destruction_queue, cmp=lambda x, y: y[2] - x[2])
        self.construction_queue = sorted(construction_queue, key=lambda x: x[2])
        self.min = 0
        self.uds = UDS(n)

    def run(self):
        for edge in self.destruction_queue:
            if self.uds.find(edge[0]) != self.uds.find(edge[1]):
                self.uds.union(edge[0], edge[1])
            else:
                self.min += edge[2]

        for edge in self.construction_queue:
            if self.uds.find(edge[0]) != self.uds.find(edge[1]):
                self.min += edge[2]
                self.uds.union(edge[0], edge[1])

edges = edges_from_input()
algorithm = KruskalAlgorithm(n, edges[0], edges[1])

algorithm.run()

print(algorithm.min)