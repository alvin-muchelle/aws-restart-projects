def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True

def generate_prime(start, end):
    prime_numbers = []
    for i in range(start, end + 1):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers

def save_to_file(primes, filename):
    with open(filename, "w") as file:
        for prime in primes:
            file.write(f"{prime}\n")

def test_results(filename):
    with open(filename, 'r') as file:
        primes = [int(line.strip()) for line in file]
    
    expected_primes = generate_prime(1, 250)
    if primes == expected_primes:
        print("Test passed: The results.txt file contains the correct prime numbers.")
    else:
        print("Test failed: The results.txt file does not contain the correct prime numbers.")

if __name__ == "__main__":
    prime_numbers = generate_prime(1,250)
    save_to_file(prime_numbers, "results.txt")

test_results("results.txt")