import difflib

def leerArchivo(arch):
    with open(arch, 'r', encoding='utf-8') as f:
        contenido = f.read()       
    return contenido

def porcentajePlag(archivo1, archivo2):
    archContenido1 = leerArchivo(archivo1)
    archContenido2 = leerArchivo(archivo2)
    
    r = difflib.SequenceMatcher(None, archContenido1, archContenido2)
    similitud = r.ratio() * 100
    
    if similitud == 100:
        print("Plagio. Ratio de similitud: 100.0%")
    elif similitud >= 60:
        print("Posible plagio, ratio de similitud:", round(similitud, 2), "%")
    else:
        print("Plagio improbable, ratio de similitud:", round(similitud, 2), "%")

print("Calculadora de similitud entre dos archivos .py")
ar1 = input("Ingrese el nombre del archivo 1: ")
ar2 = input("Ingrese el nombre del archivo 2: ")

porcentajePlag(ar1, ar2)
