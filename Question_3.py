import random
import threading
import time


def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]


def generate_set(name, result_dict):
    result_dict[name] = generate_random_numbers()


def run_round_without_threads():
    results = {}
    start_time = time.time_ns()

    for i in range(1, 4):
        results[f"Set_{i}"] = generate_random_numbers()

    end_time = time.time_ns()
    return end_time - start_time


def run_round_with_threads():
    results = {}
    threads = []
    start_time = time.time_ns()

    for i in range(1, 4):
        t = threading.Thread(target=generate_set, args=(f"Set_{i}", results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time_ns()
    return end_time - start_time


def main():
    rounds = 10
    total_seq_time = 0
    total_thread_time = 0

    print("\nRunning Both Modes for 10 Rounds:")
    print("===================================================================================")
    print("{:^10}".format("Round") + "{:^25}".format("Sequential (ns)") + "{:^25}".format("Multithreading (ns)") + "{:^25}".format("Time Difference (ns)"))
    for i in range(1, rounds + 1):
        seq_time = run_round_without_threads()
        thread_time = run_round_with_threads()
        diff = seq_time - thread_time

        print(f"{i:^10}" + f"{seq_time:^25,}" + f"{thread_time:^25,}" + f"{diff:^25,}")

        total_seq_time += seq_time
        total_thread_time += thread_time
    print("===================================================================================")

    total_diff_time = total_seq_time - total_thread_time
    avg_seq = total_seq_time // rounds
    avg_thread = total_thread_time // rounds
    avg_diff = avg_seq - avg_thread


    print("\n\nSummary:")
    print("=====================================================================================")
    print("{:<12}".format("") + "{:^25}".format("Sequential (ns)") + "{:^25}".format("Multithreading (ns)") + "{:^25}".format("Time Difference (ns)"))
    print("{:<12}".format("Total Time") + f"{total_seq_time:^25,}" + f"{total_thread_time:^25,}" + f"{total_diff_time:^25,}")
    print("{:<12}".format("Average Time") + f"{avg_seq:^25,}" + f"{avg_thread:^25,}" + f"{avg_diff:^25,}")
    print("=====================================================================================")



if __name__ == "__main__":
    main()
