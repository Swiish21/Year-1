def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

terms = int(input("Enter the number of Fibonacci sequence to generate: "))
result = fibonacci_sequence(terms)

print(f"The first {terms} terms of the Fibonacci sequence are: {result}")
