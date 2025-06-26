import random

def folding(key: str):
    if len(key) != 12 or not key.isdigit():
        raise ValueError("Key must be a 12-digit IC number.")

    hash_code = 0
    for i in range(0, 12, 4):
        chunk = key[i:i + 4]
        hash_code += int(chunk)

    return hash_code


def generate_ic():
    return ''.join(random.choices('0123456789', k=12))


def insert_to_hash_table(ic_list, table_size):
    table = [[] for _ in range(table_size)]
    for ic in ic_list:
        hash_code = folding(ic)
        index = hash_code % table_size
        table[index].append(ic)
    return table


def count_collisions(table):
    return sum(len(bucket) - 1 for bucket in table if len(bucket) > 1)


def main():
    rounds = 10
    table_sizes = [1009, 2003]

    total_collisions_1009 = 0
    total_collisions_2003 = 0

    for round_num in range(1, rounds + 1):
        print(f"\n=== Round {round_num} ===")
        print(f"Table size: {table_sizes[0]}")

        ic_numbers = [generate_ic() for _ in range(1000)]
        table_1009 = insert_to_hash_table(ic_numbers, table_sizes[0])
        table_2003 = insert_to_hash_table(ic_numbers, table_sizes[1])

        collisions_1009 = count_collisions(table_1009)
        collisions_2003 = count_collisions(table_2003)
        total_collisions_1009 += collisions_1009
        total_collisions_2003 += collisions_2003

        for i in range (table_sizes[0]):
            print(f"Table[{i}]", end="")
            for values in table_1009[i]:
                print(f" --> {values}", end="")
            print()
        print()
        print(f"Collisions for table size of 1009: {collisions_1009}")

        print()
        print(f"Table size: {table_sizes[1]}")

        for i in range (table_sizes[1]):
            print(f"Table[{i}]", end="")
            for values in table_2003[i]:
                print(f" --> {values}", end="")
            print()
        print()
        print(f"Collisions for table size of 2003: {collisions_2003}")

    total_insertions = rounds * 1000
    avg_collisions_1009 = (total_collisions_1009/total_insertions) * 100
    avg_collisions_2003 = (total_collisions_2003/total_insertions) * 100

    print()

    print("Summary:")
    print("===========================================================")
    print("{:^12}".format("Table size") + "{:^22}".format("Total Collisions") + "{:^20}".format("Average Collisions (%)"))
    print("{:^12}".format("1009") + f"{total_collisions_1009:^22,}" + f"{avg_collisions_1009:^20.2f}")
    print("{:^12}".format("2003") + f"{total_collisions_2003:^22,}" + f"{avg_collisions_2003:^20.2f}")
    print("===========================================================")

if __name__ == "__main__":
    main()
