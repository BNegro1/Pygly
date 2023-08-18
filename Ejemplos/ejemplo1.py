def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

try:
    num = int(input("Ingresa un número: "))
    
    if num < 0:
        print("Los números primos son mayores que 1.")
    elif es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Ingresa un valor numérico válido.")
