import pytest

from python_rust_package import (fibonacci_iterative_python,
                                 fibonacci_iterative_rust,
                                 fibonacci_recursive_python,
                                 fibonacci_recursive_rust)


@pytest.mark.parametrize("n", [1, 5, 10, 20])
@pytest.mark.parametrize(
    "fib",
    [
        pytest.param(fibonacci_iterative_rust, id="it_rust"),
        pytest.param(fibonacci_recursive_rust, id="re_rust"),
        pytest.param(fibonacci_iterative_python, id="it_py"),
        pytest.param(fibonacci_recursive_python, id="rec_py"),
    ],
)
def test_fib_perf(fib, n, benchmark):
    benchmark.group = f"Fibonacci at {n}"
    benchmark(fib, n)
