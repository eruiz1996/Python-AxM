# Unidad 1. Aprender a tomar notas
## Clase 01
### Jupyter Notebooks.

- ¿Qué son?
    - `IPython`
    - Celdas tipo Code y Markdown
- Ejecutar comandos de la CMD
    - Uso del `pip`
- Renderizar $\LaTeX{}$
- Sintaxis Markdown
    - Títulos
    - Formateando textos
    - Listas
    - Tablas
    - Links
    - Atajos de teclado

### Obsidian.
- Filosofía: Cerebro digital.
- Uso de Markdown
- Vista gráfica

---

# Unidad 2. Conceptos fundamentales
## Clase 02
### Memoria en la computación
#### Tipos de datos
- Built-in scalar types
    - `int`
    - `float`
    - `bool`
    - `str`
    - Función `type()`
- Variables
    - Tipado dinámico
    - Creación de variables
    - Reglas para crear nombres de variables
### Comentarios
- En una línea
- En multilínea
- *Escape character* (`\`)
    - Salto de línea (`\n`)
    - Salto de tabulador (`\t`)
### Función `print()`
- Parámetro `sep`
- Parámetro `end`
### Operadores
- Aritméticos
- Lógicos
- Relaciones

---

## Clase 03
- Función `input()`
- Casting
- Ejercicios:
    - Promedio de calificaciones
    - De Celsius a Fahrenheit
    - IMC
### Sentencias de Control
#### Sentencias condicionales
- `if`
- `if`-`else`
- `if`-`elif`-`else`
- Ejercicios:
    - Mayoría de edad
    - Máquina de helados
### Formateo de `str`
- Método `format()`
- `f-strings`
    - Presición de decimales
    - Separador de miles
    - Números consecutivos
- Ejercicios:
    - De Fahrenheit a Celsius
    - Millones de Pesos
    - Mayoría de Edad
    - Verificador de Contraseña
        - Función `len()`
        - Operador `in`

---

## Clase 04
### Listas
- Indexación
    - Acceder al último elemento
    - Slicing
- Mutabilidad
    - Modificar
    - Casting entre `str` y `list`
    - Agregar elementos
        - Método `append()`
        - Sumar listas
        - Método `extend()`
        - Método `insert()`
    - Eliminar elementos
        - Método `pop()`
        - Método `clear()`
- Almacenamiento de datos
- Funciones de agregación
    - `sum()`
    - `max()`
    - `min()`
- Función `range()`
### Tuplas
- Creación de tuplas
- Principales usos
- Métodos
    - `count()`
    - `index()`

---

## Clase 05
### Sentencias de control (*continuación*)
#### Ciclos
- Ciclo `for`
    - Función *enumerate()*
    - Función *zip()*
    - Incrementos
    - Ejercicio de vectores
- Métodos de los `str`
- Ciclo `while`
### Funciones
- Sin parámetros
    - Sin valor de retorno
    - Con valor de retorno
    - Con múltiples valores de retorno
- Con parámetros
    - Múltiples parámetros
    - Parámetros por defecto
    - Ejercicios
        - Operadores de Identidad
- Funciones recursivas
- Funciones con parámetros indeterminados

---

## Clase 06
- Funciones anónimas (`lambda`)
    - Un parámetro
    - Dos parámetros
    - Aplicando otras funciones
### Buit-in Python
- Diccionarios
    - Acceder
    - Modificar
    - Agregar
    - Métodos `keys()` y `values()`
    - Iterar sobre un diccionario
        - `items()`
    - Diccionarios vacíos
- Conjuntos
    - Conjuntos vacíos
    - A partir de un iterable
    - Métodos `union()` e `intersection()`
### Manejo de Excepciones
- Estructura `try`-`except`
- Manejo específico
- Estructura `try`-`except`-`else`-`finally`
### Listas por comprensión
- Con `if`
- Con `if`-`else`
### Paradigmas de la Programación
- Programación imperativa
- Programación descriptiva
    - Funcional
    - Reactiva
- Programación Orientada a Objetos

---

# Unidad 3. Programación Orientada a Objetos
## Clase 07 
### Abstracción
- Clases
- Instancias
- Definiendo una clase
- La instanciación
- Definiendo atributos
#### Dunder methods
- Método constructor (`__init__`)
    - Parámetro `self`
- Método `__str__`
### Métodos propios
### Ejercicios
- Clase `Car`
- Clase `Alumno`
- Clase `Celular`
### Herencia
- Clase Padre
- Clase Hijo
- Modificando atributos de la clase Padre
### Encapsulamiento
### Polimorfismo
### Modularización
- Importar módulos
- Importa funciones y objetos

---

## Clase 08
### Teoría
- Interactuando con *Spyder*
- Módulo `numpy`
    - Arreglos
        - Slicing
        - Filtrado
    - Matrices
        - Atributo `shape`
        - Slicing
        - Trasponer (atributo `T`)
        - Matrices especiales
            - Identidad
            - De Ceros
            - De Unos
        - Multiplicación de matrices
    - Vectorización
- Módulos `random`
    - Números pseudo-aleatorios
    - Método `seed()`
    - Método `choice()`
    - `random()` en `numpy`
- Módulos propios
- Módulo `matplotlib`
    - Visualizando gráficos
- Módulo `pandas`
    - Ejercicio Práctico
### Práctica
- Conjetura de Collatz
- Ejercicio de simulación