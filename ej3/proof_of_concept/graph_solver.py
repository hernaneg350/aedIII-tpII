import sys

n = int(sys.stdin.readline())


def read_edge(line):
    edge_data = line.split(' ')
    return tuple(map(lambda x: int(x), edge_data))


def adjacency_from_input():
    all_weights = 0
    destruction_weights = 0
    adjacency_matrix = [[(False, 0) for j in range(0, n)] for i in range(0, n)]
    for edge_line in sys.stdin:
        edge = read_edge(edge_line)
        v1 = edge[0]
        v2 = edge[1]
        is_present = edge[2] == 1
        weight = edge[3]

        all_weights += weight

        if is_present:
            destruction_weights += weight

        adjacency_matrix[v1][v2] = (is_present, weight)
        adjacency_matrix[v2][v1] = (is_present, weight)
    return (adjacency_matrix, all_weights, destruction_weights)


class BacktrackingAlgorithm:
    def __init__(self, n, adjacency_matrix, all_weights, destruction_weights):
        self.adjacency_matrix = adjacency_matrix
        self.destruction_total = destruction_weights
        self.current_min = all_weights
        self.n = n


    def get_connected_component(self, vertex, connection_set):
        result = None
        for connected_component in connection_set:
            if vertex in connected_component:
                result = connected_component
                break

        return result

    def recursion(self, connection_set, current_destruction_weight, current_construction_weight, i, j):
        if i == self.n - 1:
            if len(connection_set) == 1 and all(map(lambda x: len(x) == n, connection_set)) and current_destruction_weight + current_construction_weight < self.current_min:
                self.current_min = current_destruction_weight + current_construction_weight
            return

        if current_construction_weight > self.current_min:
            return

        next_i = i + 1 if j + 1 == n else i
        next_j = i + 2 if j + 1 == n else j + 1

        v1 = i
        v2 = j

        v1_connected_component = self.get_connected_component(v1, connection_set)
        v2_connected_component = self.get_connected_component(v2, connection_set)

        construction_weight = self.adjacency_matrix[v1][v2][1]
        existed = self.adjacency_matrix[v1][v2][0]
        needs_construction = not existed

        if v1_connected_component is None or v2_connected_component is None or v1_connected_component != v2_connected_component:
            new_connection_set = connection_set
            if v1_connected_component is None:
                v1_connected_component = frozenset({v1})
            else:
                new_connection_set = new_connection_set - frozenset({v1_connected_component})

            if v2_connected_component is None:
                v2_connected_component = frozenset({v2})
            else:
                new_connection_set = new_connection_set - frozenset({v2_connected_component})

            self.recursion(
                new_connection_set | frozenset({v1_connected_component | v2_connected_component}),
                current_destruction_weight - construction_weight if existed else current_destruction_weight,
                current_construction_weight + construction_weight if needs_construction else current_construction_weight,
                next_i,
                next_j
            )

        self.recursion(
            connection_set,
            current_destruction_weight,
            current_construction_weight,
            next_i,
            next_j
        )

    def run(self):
        self.recursion(frozenset({}), self.destruction_total, 0, 0, 1)


graph_data = adjacency_from_input()
algorithm = BacktrackingAlgorithm(n, graph_data[0], graph_data[1], graph_data[2])

algorithm.run()

print(algorithm.current_min)
