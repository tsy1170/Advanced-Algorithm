import random
import threading
import time

# Function to generate 100 random numbers
def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

# Threaded function to generate a set and store in result dict
def generate_set(name, result_dict):
    result_dict[name] = generate_random_numbers()

# One round without threads
def run_round_without_threads(round_num):
    results = {}
    start_time = time.time_ns()

    for i in range(1, 4):
        results[f"Set_{i}"] = generate_random_numbers()

    end_time = time.time_ns()
    time_elapsed = end_time - start_time
    print(f"[Sequential] Round {round_num}: {time_elapsed:,} ns")
    return time_elapsed

# One round with threads
def run_round_with_threads(round_num):
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
    time_elapsed = end_time - start_time
    print(f"[Multithreaded] Round {round_num}: {time_elapsed:,} ns")
    return time_elapsed

# Main execution
def main():
    rounds = 10
    print("=== Running Sequential (No Threads) ===")
    total_seq_time = 0
    for i in range(1, rounds + 1):
        total_seq_time += run_round_without_threads(i)
    avg_seq = total_seq_time // rounds
    print(f"\nAverage Time (Sequential): {avg_seq:,} ns")

    print("\n=== Running Multithreaded ===")
    total_thread_time = 0
    for i in range(1, rounds + 1):
        total_thread_time += run_round_with_threads(i)
    avg_thread = total_thread_time // rounds
    print(f"\nAverage Time (Multithreaded): {avg_thread:,} ns")

    # Optional comparison
    print("\n=== Summary ===")
    print(f"Sequential Average Time   : {avg_seq:,} ns")
    print(f"Multithreaded Average Time: {avg_thread:,} ns")

if __name__ == "__main__":
    main()
