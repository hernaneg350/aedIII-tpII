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

### Run time complexity does not get affected by density
#write_csv('results/density.csv',
#    [['density', 'time']] +
#    rows_to_columns([
#        [0.0] + [1.0 / calc for calc in range(1, 30)],
#        profile_instances(instancegenerators.variable_density_generator(30), 100),
#    ])
#)

write_csv('results/n_growth.csv',
    [['n', 'time']] +
    rows_to_columns([
        [n for n in range(20, 100)],
        profile_instances(instancegenerators.grow_n_generator(20, 100), 100),
    ])
)