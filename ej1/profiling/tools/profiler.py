from subprocess32 import Popen, PIPE, STDOUT
import resource

previous_program_time = 0


def previous_program_time_set(x):
    global previous_program_time
    previous_program_time = x


def run_algorithm(instance):
    process = Popen(['../bin/runner'], stdout=None, stdin=PIPE, stderr=STDOUT)
    process_input = instance
    process.communicate(input=bytearray(process_input))

    current_program_time = resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime
    algorithm_time = current_program_time - previous_program_time
    previous_program_time_set(current_program_time)
    return algorithm_time


def profile_algorithm(instance, runs):
    results_list = []
    for i in range(0, runs):
        results_list.append(run_algorithm(instance))
    return average(results_list)


def average(ls):
    return reduce(lambda x, y: x + y, ls) / len(ls)


def calclate_averages(n_results, n_avg_times):
    n_results_average = average(n_results)
    n_avg_times.append(n_results_average)
    del n_results[:]


def profile_instances(generator, precision):
    previous_n = -1
    n_results = []
    n_avg_times = []
    for (current_n, instance) in generator():
        if previous_n >= 0 and previous_n != current_n:
            calclate_averages(n_results, n_avg_times)

        previous_n = current_n

        result = profile_algorithm(instance, precision)
        n_results.append(result)

    calclate_averages(n_results, n_avg_times)

    return n_avg_times
