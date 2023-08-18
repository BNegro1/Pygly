def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_hasta_n(n):
    print("Números primos hasta", n, ":")
    for num in range(2, n + 1):
        if es_primo(num):
            print(num, end=" ")

try:
    limite = int(input("Ingresa un límite: "))
    imprimir_primos_hasta_n(limite)
except ValueError:
    print("Ingresa un valor numérico válido.")