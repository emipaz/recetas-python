
# Iterador Personalizado Reutilizable: `Rango`

## **Archivo:** rango.py`

Implementación de un iterador personalizado que extiende la funcionalidad del `range()` nativo de Python con soporte para:

### Características Principales:
- ✅ **Pasos decimales** - Soporta `Rango(0, 1, 0.1)` con precisión configurable
- ✅ **Reutilizable** - El mismo objeto se puede iterar múltiples veces
- ✅ **Validación robusta** - Validación de tipos y parámetros con mensajes claros
- ✅ **Búsqueda eficiente** - Método `__contains__` que verifica membresía sin iterar
- ✅ **Cálculo de longitud** - `len()` funciona con pasos enteros y flotantes
- ✅ **Comparación** - Soporte de igualdad entre objetos `Rango`

#### Métodos Implementados:

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `__init__(*args, pres=1)` | Inicializa el rango con validación | `Rango(0, 10, 2)` |
| `__iter__()` | Retorna generador reutilizable | `for x in rango:` |
| `__next__()` | Generador interno con precisión | `next(iter(rango))` |
| `__len__()` | Calcula longitud sin iterar | `len(rango)` |
| `__contains__(valor)` | Búsqueda matemática eficiente | `5 in rango` |
| `__eq__(otro)` | Comparación entre rangos | `rango1 == rango2` |
| `__repr__()` | Representación de depuración | `repr(rango)` |
| `__str__()` | Representación legible | `str(rango)` |

##### Sintaxis:
```python
# Un parámetro: inicio en 0
Rango(5)                          # [0, 1, 2, 3, 4]

# Dos parámetros: paso de 1
Rango(2, 5)                       # [2, 3, 4]

# Tres parámetros: paso personalizado
Rango(0, 10, 2)                   # [0, 2, 4, 6, 8]

# Con pasos decimales
Rango(0, 1, 0.2, pres=1)          # [0.0, 0.2, 0.4, 0.6, 0.8]

# Paso negativo (descendente)
Rango(10, 0, -1.5)                # [10, 8.5, 7.0, 5.5, ...]
```

##### Casos de Uso Avanzados:
```python
# Reutilización: mismo objeto, múltiples iteraciones
it = Rango(0, 5)
print(list(it))  # [0, 1, 2, 3, 4]
print(list(it))  # [0, 1, 2, 3, 4] ✅ Se reinicia automáticamente

# Búsqueda eficiente: O(1) sin iterar
it = Rango(0, 10, 0.5)
print(1.5 in it)  # True (0 + 3×0.5)
print(1.6 in it)  # False (no es múltiplo de 0.5)

# Longitud con pasos flotantes
it = Rango(0, 1, 0.1, pres=1)
print(len(it))    # 10

# Comparación
rango1 = Rango(0, 10, 2)
rango2 = Rango(0, 10, 2)
print(rango1 == rango2)  # True
```

##### Manejo de Errores:
```python
from rango import Rango, RangoError

try:
    Rango(0, 10, 0)      # ❌ paso=0
except RangoError as e:
    print(e)             # ❌ 'paso' no puede ser cero

try:
    Rango("inicio", 10)  # ❌ tipo inválido
except RangoError as e:
    print(e)             # ❌ 'inicio' debe ser número
```

## Tests Unitarios:

### **Archivo:** `test_rango.py`

Incluye pruebas exhaustivas:
- ✅ Pasos enteros y flotantes (positivos y negativos)
- ✅ Validación de tipos e excepciones
- ✅ Comportamiento de `__contains__` con precisión flotante
- ✅ Cálculo correcto de `__len__`
- ✅ Reutilización de objetos
- ✅ Comparación de instancias

**Ejecutar tests:**
```bash
python -m pytest test_rango.py -v
# o
python -m unittest test_rango.py -v
```

## Ventajas sobre `range()` nativo:

| Característica | `range()` | `Rango` |
|---|---|---|
| Pasos decimales | ❌ | ✅ |
| Reutilizable | ✅ | ✅ |
| `len()` | ✅ | ✅ |
| `in` (búsqueda) | ✅ | ✅ (más eficiente) |
| Mensajes de error | ❌ | ✅ (detallados) |
| Precisión decimal | ❌ | ✅ |

### Documentación:
- Estilo Google completo
- Type hints implícitos
- Ejemplos en docstrings
- Manejo robusto de excepciones