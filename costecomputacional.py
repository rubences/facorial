def numeros_pares_impares(n):

        # O(1) - Operación elemental
    print("Inicio del algoritmo - Coste O(1)")
    
    for i in range(1, n + 1):  # O(n) - Bucle for desde 1 hasta n
        print(f"Iteración {i} del bucle for - Coste O(n)")
        
        if i % 2 == 0:  # O(1) - Comparación en el if
            print(f"  Comparación if (i % 2 == 0) - Coste O(1)")
            # O(1) - Rama verdadera
            print(f"  Rama verdadera - Coste O(1)")
        else:
            print(f"  Comparación if (i % 2 != 0) - Coste O(1)")
            # O(2) - Rama falsa
            print(f"  Rama falsa - Coste O(2)")
    
    # O(1) - Operación elemental
    print("Fin del algoritmo - Coste O(1)")

# Ejemplo de uso
numeros_pares_impares(10)