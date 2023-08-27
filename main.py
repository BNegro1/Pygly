import difflib
import os
def leerArchivo(arch):
    if not os.path.isfile(arch):
        print(f"El archivo {arch} no existe.")
        return None
    with open(arch, 'r', encoding='utf-8') as f:
        contenido = f.read()
        
    if os.stat(arch).st_size == 0:
        print(f"El archivo {arch} está vacio.")
        return None
    
    return contenido

def porcentajePlag(archivo1, archivo2):
    archContenido1 = leerArchivo(archivo1)
    archContenido2 = leerArchivo(archivo2)
    if archContenido1 is not None and archContenido2 is not None:
        r1 = difflib.SequenceMatcher(None, archContenido1, archContenido2)
        similitud1 = r1.ratio() * 100
        r2 = difflib.SequenceMatcher(None, archContenido2, archContenido1)
        similitud2 = r2.ratio() * 100
    
        promSimi = ((similitud1 + similitud2)/2)
    
        if promSimi == 100:
            print("Plagio. Ratio de similitud promedio: 100.0%")
        elif promSimi >= 60:
            print("Posible plagio, ratio de similitud promedio:", round(promSimi, 2), "%")
        else:
            print("Plagio improbable, ratio de similitud promedio:", round(promSimi, 2), "%")


print("Calcular de similitud entre dos archivos .py")
while True:
    ar1 = input("Ingrese el nombre del archivo 1: ")
    ar2 = input("Ingrese el nombre del archivo 2: ")
    
    if len(ar1) == 0 or len(ar2) == 0:
        print("Ingrese un archivo.")
    else:
        porcentajePlag(ar1, ar2)