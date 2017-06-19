from tools.csv_tools import write_csv, rows_to_columns
from tools.profiler import profile_instances
from instancegenerators import growing_k_generator


write_csv('results/k_growth.csv',
    [['k', 'k^2', 'time']] +
    rows_to_columns([
        [k for k in range(0, 100)],
        [k**2 for k in range(0, 100)],
        profile_instances(growing_k_generator(n=50, max_k=100), precision=10)
    ])
)