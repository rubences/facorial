def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Calcular el factorial de 5
print(factorial_iterativo(1000))