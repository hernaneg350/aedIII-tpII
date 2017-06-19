from tools.csv_tools import write_csv, rows_to_columns
from tools.profiler import profile_instances
from instancegenerators import variable_density_generator, max_edges


write_csv('results/density_variation.csv',
[['density', 'time']] +
    rows_to_columns([
        [float(edge_count) / float(max_edges(20)) for edge_count in range(10, max_edges(20))],
        profile_instances(variable_density_generator(n=20, k=10), precision=1000)
    ])
)