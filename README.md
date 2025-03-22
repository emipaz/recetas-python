# Recetas Python

Basados en el libro de recetas de Python de David Beazley, este repositorio contiene ejemplos de código y ejercicios para aprender Python.

## Capitulo 1

### cap1-1-5.ipynb

#### 1.1. Desempaquetamiento de variables
#### 1.2. Desempaquetar elementos de iterables de longitud arbitraria
#### 1.3. Mantener la última N líneas (colas de collections.deque)
#### 1.4. Encontrar los elementos más grandes o más pequeños (heapq)
#### 1.5. Cola Prioritaria

### cap1-6-12.ipynb

#### 1.6 Asignacion de claves de varios valores a un diccionario (Multidict usandop collections.defaultdict)
#### 1.7. Mantener los diccionarien en orden (collections.OrderedDict)
#### 1.8. Calculando con diccionarios (zip, min, max)
#### 1.9. Encontrar puntos en común en dos diccionarios (keys, items) uso de operaciones de conjuntos & | -
#### Encontrar numeros impares que no son primos usando conjuntos por comprensión
#### 1.10 Eliminando duplicados de una secuencia manteniendo el orden (hashable)
#### 1.11. Nombrar un slice (slice)
#### 1.12. Determinar los elementos más frecuentes en una secuencia (collections.Counter)

### cap1-13-16.ipynb#

#### 1.13. Ordenar una lista de diccionarios por un campo común (operator.itemgetter)
#### 1.14. Ordenar objetos sin soporte a comparación (attrgetter)
#### 1.15. Agrupar registros por campos de interés (itertools.groupby)
#### 1.16. Filtrar elementos de una secuencia (comprensión de listas y itertools.compress)

### cap1-17-19.ipynb

#### 1.17. Asignación de nombres a elementos de una tupla (collections.namedtuple)
#### 1.18. Transdformar y reducir datos al mismo tiempo (generadores de expresiones max, min, sum)
#### 1.19. Combinar múltiples mapeos en un solo mapeo (collections.ChainMap)

## Capitulo 2 (Strings and Text)

### cap2-1-6.ipynb

#### 2.1 División de cadenas en cualquiera de los delimitadores múltiplesas
#### 2.2 Coincidencia de texto al principio o al final de una cadena (str.startswith, str.endswith)
#### 2.3 Coincidencia de cadenas mediante patrones de comodines de Shell (fnmatch)
#### 2.4 Coincidencia de cadenas mediante (str.find, str.endswith, str.startswith)
#### 2.5 Buscar y reemplazar texto (str.replace, re.sub, re.subn)
#### 2.6 Búsqueda y reemplazo de texto sin distinción entre mayúsculas y minúsculas (re.IGNORECASE)

### cap2-7-13.ipynb

#### 2.7 Especificar una expresión regular para la coincidencia mas corta
#### 2.8 Escribir una expresión regular para patrones de varias línea
#### 2.9 Normalizar texto Unicode para comparación o impresión (unicodedata.normalize)
#### 2.10 Eliminar signos de puntuación de texto (str.translate)
#### 2.11 Eliminación de caracteres no deseados
#### 2.12 Desinfectar y limpiar el texto
#### 2.13 Alinear cadenas de texto

### cap2-14-15.ipynb

#### 2.14 Combinar y concatenar cadenas (str.join)
#### 2.15 Interpolación de variables en cadenas (str.format, format_map , vars() , \_\_missing\_\_ , sys._getframe() )
### 2.16 Camnio de formato de texto a un numero fijo de columnas (Textwrap.fill)
### 2.17 Manejo de HTML y XML (html.escape, html.unescape)
### 2.18 Tokenización de texto (re.scaner.search) token_expr.ipynb
### 2.19 Escribir un analizador de descenso recursivo simple ()
### 2.20 Realización de operaciones de texto en cadenas de bytes (bytes, bytearray, startwith, endswith, split, replace, re)

## Capitulo 3 (Numbers, Dates, and Times)

### cap3-1-5.ipynb

#### 3.1 Redondeo de números (round)
#### 3.2 Realizar cálculos decimales precisos (Decimal)
#### 3.3 Formateo de números para salida (format)
#### 3.4 TTrabajar con Enteros binario, octal y hexadecimal (bin, oct, hex)
#### 3.5 Empaquetado y desempaquetado de números enteros grandes a partir de bytes

### cap3-6-9.ipynb

#### 3.6 Trabajando con números complejos (complex)
#### 3.7 Trabajar con Infinity y NaNs (float, math.isinf, math.isnan)
#### 3.8 Calcular con fracciones (Fraction)
#### 3.9 Calcular con grandes arreglos (numpy)