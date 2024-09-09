# math_operations.py

def factorial(n):
    """Return the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def gcd(a, b):
    """Return the greatest common divisor of two numbers."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return the least common multiple of two numbers."""
    return abs(a * b) // gcd(a, b)

def power(base, exponent):
    """Return the base raised to the power of the exponent."""
    return base ** exponent

def main():
    # Using the factorial function
    number = 5
    print(f"Factorial of {number}: {factorial(number)}")

    # Using the GCD function
    num1 = 48
    num2 = 18
    print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")

    # Using the LCM function
    print(f"LCM of {num1} and {num2}: {lcm(num1, num2)}")

    # Using the power function
    base = 2
    exponent = 3
    print(f"{base} raised to the power of {exponent}: {power(base, exponent)}")

if __name__ == "__main__":
    main()