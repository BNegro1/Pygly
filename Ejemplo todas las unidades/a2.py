import numpy as np

def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_primos(n):
    primos = [num for num in range(2, n+1) if es_primo(num)]
    return primos

try:
    limite = int(input("Ingrese un número límite: "))
    primos_encontrados = encontrar_primos(limite)
    print("Números primos encontrados:", primos_encontrados)

    arreglo_unidimensional = np.array(primos_encontrados)
    print("Arreglo unidimensional:", arreglo_unidimensional)

    arreglo_bidimensional = np.reshape(arreglo_unidimensional, (len(primos_encontrados)//2, 2))
    print("Arreglo bidimensional:\n", arreglo_bidimensional)

except ValueError:
    print("Por favor, ingrese un número válido.")

except Exception as e:
    print("Ocurrió un error:", e)
