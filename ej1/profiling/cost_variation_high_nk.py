from tools.csv_tools import write_csv, rows_to_columns
from tools.profiler import profile_instances
from instancegenerators import variable_cost_generator

write_csv('results/cost_variation_high_nk.csv',
    [['iteration', 'time_1', 'time_2', 'time_3']] +
    rows_to_columns([
        [i for i in range(0, 200)],
        profile_instances(variable_cost_generator(n=100, k=20, max_iterations=100), precision=100),
        profile_instances(variable_cost_generator(n=100, k=20, max_iterations=100), precision=100),
        profile_instances(variable_cost_generator(n=100, k=20, max_iterations=100), precision=100)
    ])
)