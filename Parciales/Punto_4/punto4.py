
import sys
import time


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 35

    t1 = time.perf_counter()
    resultado = fibonacci(n)
    t2 = time.perf_counter()

    ms = (t2 - t1) * 1000
    print(f"Fibonacci({n}) = {resultado}")
    print(f"Tiempo Python (ms): {ms:.3f}")


if __name__ == "__main__":
    main()
