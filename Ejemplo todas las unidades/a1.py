import numpy as np

def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(n):
    primos = []
    for i in range(2, n+1):
        if es_primo(i):
            primos.append(i)
    return primos

try:
    limite = int(input("Ingrese un número límite: "))
    primos_encontrados = encontrar_primos(limite)
    print("Números primos encontrados:", primos_encontrados)

    # Crear un arreglo unidimensional con numpy
    arreglo_unidimensional = np.array(primos_encontrados)
    print("Arreglo unidimensional:", arreglo_unidimensional)

    # Crear un arreglo bidimensional con numpy
    arreglo_bidimensional = np.reshape(arreglo_unidimensional, (len(primos_encontrados)//2, 2))
    print("Arreglo bidimensional:\n", arreglo_bidimensional)

except ValueError:
    print("Por favor, ingrese un número válido.")

except Exception as e:
    print("Ocurrió un error:", e)
