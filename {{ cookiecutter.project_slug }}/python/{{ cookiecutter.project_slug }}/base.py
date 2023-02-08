def fibonacci_recursive_python(n: int) -> int:
    if n < 2:
        return n
    return fibonacci_recursive_python(n - 1) + fibonacci_recursive_python(n - 2)


def fibonacci_iterative_python(n: int) -> int:
    if n < 2:
        return n

    a, b = 0, 1
    c = 0
    for _ in range(2, n):
        c = a + b
        a, b = b, c
    return c
