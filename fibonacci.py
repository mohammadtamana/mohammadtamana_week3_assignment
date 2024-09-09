def fibonacci_iterative(n):
    """Calculate Fibonacci sequence up to n using an iterative approach."""
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n, a=0, b=1, sequence=None):
    """Calculate Fibonacci sequence up to n using a recursive approach."""
    if sequence is None:
        sequence = []
    
    if a > n:
        return sequence
    
    sequence.append(a)
    return fibonacci_recursive(n, b, a + b, sequence)

# Example usage
n = 20

print(f"Fibonacci sequence up to {n} (iterative):")
print(fibonacci_iterative(n))

print(f"Fibonacci sequence up to {n} (recursive):")
print(fibonacci_recursive(n))