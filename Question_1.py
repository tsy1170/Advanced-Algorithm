import random

def folding(key: str):
    if len(key) != 12 or not key.isdigit():
        raise ValueError("Key must be a 12-digit IC number.")

    hash_code = 0
    for i in range(0, 12, 4):
        chunk = key[i:i + 4]
        hash_code += int(chunk)

    return hash_code

def main():
    IC = input("Please enter IC number without dash: ")
    hash_code = folding(IC)



if __name__ == "__main__":
    main()