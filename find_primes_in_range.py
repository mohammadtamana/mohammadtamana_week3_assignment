def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    """Find all prime numbers in a given range [start, end]."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
start_range = 10
end_range = 50
prime_numbers = find_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range} are: {prime_numbers}")