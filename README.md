# Detección de Similitud de Código en Python

Este código en Python utiliza técnicas de procesamiento de lenguaje natural (NLP) y el modelo TF-IDF para detectar la similitud entre dos fragmentos de código en Python. El objetivo es determinar cuán similares son dos piezas de código en términos de su estructura y contenido.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas antes de ejecutar el código:

- NLTK (Natural Language Toolkit): Para el procesamiento de texto en lenguaje natural.
- scikit-learn: Para el cálculo de similitud utilizando TF-IDF y coseno.

## Funciones

### `cargarTexto(archivo)`

Esta función carga el contenido de un archivo de texto especificado. Toma el nombre del archivo como entrada y devuelve el texto contenido en el archivo o `None` si el archivo no existe.

### `limpiarTexto(texto)`

La función `limpiarTexto` toma un fragmento de texto como entrada y realiza dos pasos de limpieza:

1. Elimina múltiples espacios en blanco y tabulaciones, reemplazándolos por un solo espacio.
2. Elimina líneas de comentarios que comienzan con `#`. Esto es útil para eliminar comentarios de código Python y evitar que afecten la similitud.

### `calcularSimilitud(texto1, texto2)`

Esta función calcula la similitud entre dos fragmentos de texto. Primero, realiza los siguientes pasos para cada fragmento de texto:

1. Tokeniza el texto en palabras individuales.
2. Elimina palabras vacías ("stop words") del idioma inglés.
3. Realiza la derivación (stemming) de palabras utilizando el algoritmo de Porter.

Luego, convierte los tokens en cadenas de texto y crea una matriz TF-IDF (Term Frequency-Inverse Document Frequency) para los dos fragmentos de texto. Finalmente, calcula la similitud coseno entre las dos matrices TF-IDF y devuelve el resultado como un porcentaje de similitud.

## Uso

1. Asegurar de tener instaladas las bibliotecas mencionadas en los requisitos.
3. Ingresar el nombre de dos archivos de código con extesión ".py" cuando se solicite.
4. El código calculará la similitud entre los dos fragmentos de código y mostrará el resultado en forma de porcentaje de similitud en la salida estándar.

