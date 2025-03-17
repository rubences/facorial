def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calcular el factorial del número 5
resultado = factorial(900)
print(f"El factorial de 5 es: {resultado}")