import numpy as np

def encontrar_primos(n):
    primos = []
    criba = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if criba[p]:
            for i in range(p * p, n + 1, p):
                criba[i] = False
        p += 1
    for p in range(2, n + 1):
        if criba[p]:
            primos.append(p)
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
