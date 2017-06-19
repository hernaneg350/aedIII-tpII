import csv
import instancegenerators
from profiler import profile_instances


def write_csv(csv_file_name, results):
    with open(csv_file_name, 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for result in results:
            csv_writer.writerow(result)


def rows_to_columns(matrix):
    return [list(x) for x in zip(*matrix)]

## Run time complexity does not get affected by strongly connected components
write_csv('results/connected_components.csv',
    [['connected_component_count', 'time']] +
    rows_to_columns([
        [n for n in range(2, 200)],
        profile_instances(instancegenerators.variable_components_generator(200), 100),
    ])
)

### Run time complexity in low vs high density grpahs
write_csv('results/high_vs_low_density.csv',
    [['n', 'high_density', 'low_density']] +
    rows_to_columns([
        [n for n in range(2, 201)],
        profile_instances(instancegenerators.grow_n_generator(2, 200, 1.0), 10),
        profile_instances(instancegenerators.grow_n_generator(2, 200, 0.0), 10),
    ])
)

### Run time complexity approches n**2 for low density graphs
write_csv('results/low_density_vs_n_2.csv',
    [['n', 'n^2', 'time']] +
    rows_to_columns([
        [n for n in range(2, 201)],
        [n**2 for n in range(2, 201)],
        profile_instances(instancegenerators.grow_n_generator(2, 200, 0.0), 10),
    ])
)

### Run time complexity approches n**3 for high density graphs
write_csv('results/high_density_vs_n_3.csv',
    [['n', 'n^3', 'time']] +
    rows_to_columns([
        [n for n in range(2, 201)],
        [n**3 for n in range(2, 201)],
        profile_instances(instancegenerators.grow_n_generator(2, 200, 1.0), 10),
    ])
)
