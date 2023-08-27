import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

def cargarTexto(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
        return texto
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
        return None
    
def limpiarTexto(texto):
    texto = re.sub(r'\s+', ' ', texto)
    texto = re.sub(r'#.*\n', '\n', texto)    
    return texto


def calcularSimilitud(texto1, texto2):
    # Tokenización y eliminación de "stopwords"
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()

    listaTokens1 = []
    for palabra in word_tokenize(texto1):
        if palabra.lower() not in stop_words:
            listaTokens1.append(stemmer.stem(palabra.lower()))

    listaTokens2 = []
    for palabra in word_tokenize(texto2):
        if palabra.lower() not in stop_words:
            listaTokens2.append(stemmer.stem(palabra.lower()))
    # Convertir los tokens a cadenas de texto
    proceso1 = ' '.join(listaTokens1)
    proceso2 = ' '.join(listaTokens2)
    vectorizar = TfidfVectorizer()
    matristfidf = vectorizar.fit_transform([proceso1, proceso2])
    calculaSimilitud = cosine_similarity(matristfidf[0], matristfidf[1])[0][0] * 100
    return calculaSimilitud

def main():
    print("Similitud entre codigos")
    a1 = input("Ingrese el nombre del archivo 1: ")
    a2 = input("Ingrese el nombre del archivo 2: ")
    t1 = cargarTexto(a1)
    t2 = cargarTexto(a2)
    
    if t1 is not None and t2 is not None:
        t1 = limpiarTexto(t1)
        t2 = limpiarTexto(t2)
        similitud = calcularSimilitud(t1, t2)
        print(f"Porcentaje de similitud: {similitud:.2f}%")
main()