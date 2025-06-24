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


def main():
    rounds = 10
    table_sizes = [1009, 2003]

    for round_num in range(1, rounds + 1):
        print(f"\n=== Round {round_num} ===")
        print(f"Table size: {table_sizes[0]}")

        ic_numbers = [generate_ic() for _ in range(1000)]
        table_1009 = insert_to_hash_table(ic_numbers, table_sizes[0])
        table_2003 = insert_to_hash_table(ic_numbers, table_sizes[1])

        for i in range (table_sizes[0]):
            print(f"Table[{i}]", end="")
            for values in table_1009[i]:
                print(f" --> {values}", end="")
            print()
        
        print()
        print(f"Table size: {table_sizes[1]}")

        for i in range (table_sizes[1]):
            print(f"Table[{i}]", end="")
            for values in table_2003[i]:
                print(f" --> {values}", end="")
            print()


if __name__ == "__main__":
    main()
