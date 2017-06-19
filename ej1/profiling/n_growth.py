from tools.csv_tools import write_csv, rows_to_columns
from tools.profiler import profile_instances
from instancegenerators import growing_n_generator


write_csv('results/n_growth.csv',
    [['n', 'x^2', 'time']] +
    rows_to_columns([
        [n for n in range(20, 200)],
        [x**2 for x in range(20, 200)],
        profile_instances(growing_n_generator(k=20, min_n=20, max_n=200), precision=10)
    ])
)