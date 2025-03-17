def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Ejemplo de uso
n = 10
print(f"El número de Fibonacci en la posición {n} es {fibonacci_iterative(n)}")