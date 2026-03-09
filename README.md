# 📚 Parcial 1 - Compiladores y Lenguajes de Programación

Este repositorio contiene las soluciones detalladas para el primer parcial de la asignatura. Todas las implementaciones siguen las restricciones de control manual (if/else) y el uso de herramientas específicas como Flex, Bison y ANTLR.

---

## 🔹 Punto 1: AFD para Movimientos de Ajedrez

### Enunciado
Escriba un programa que reconozca movimientos de ajedrez (ej: `p->k4`, `kbpXqn`). Debe usar un Autómata Finito Determinista (AFD) manual con estructuras `if/else`.

### Explicación
Se implementó un AFD que procesa la cadena carácter por carácter.

- **Estado S0/S1:** Valida las piezas iniciales (`p, k, b, q, r`).
- **Estado S2/S3:** Identifica el conector de movimiento `->` o de captura `X`.
- **Estado S4:** Valida el destino (casilla o pieza capturada).

El diseño evita librerías de expresiones regulares para cumplir con la restricción de **control manual del autómata**.

### Cómo ejecutarlo

```bash
python3 punto1_ajedrez.py
```

---

## 🔹 Punto 2: AFD para Identificadores (IDs)

### Enunciado
Implemente un AFD para reconocer identificadores que cumplan con la regla:

```
[A-Za-z][A-Za-z0-9]*
```

Es decir:

- Deben comenzar con una **letra**
- Pueden continuar con **letras o números**

### Explicación

El programa utiliza dos archivos para demostrar modularidad.

**1️⃣ `AFDdeIDs.py`**

Contiene la lógica del autómata con estados:

- `q0` → estado inicial
- `q1` → estado de aceptación

Utiliza la función `ord()` para validar rangos ASCII de:

- letras (`A-Z`, `a-z`)
- números (`0-9`)

**2️⃣ `pruebas.py`**

Importa el AFD y ejecuta una batería de pruebas:

- 3 identificadores aceptados
- 2 rechazados

Se utilizan bloques `try/except` para manejar errores.

### Cómo ejecutarlo

```bash
python3 pruebas.py
```

---

## 🔹 Punto 3: Calculadora de Raíz Cuadrada (Flex & Bison)

### Enunciado

Escriba un programa en **C** que implemente una calculadora de **raíz cuadrada para números reales** usando:

- **Flex**
- **Bison**

El cálculo debe usar el método **Newton-Raphson**.

Requisitos:

- La **entrada** debe venir desde un **archivo de texto**
- La **salida** debe mostrarse por **consola**

### Explicación

El sistema está compuesto por tres archivos:

#### 🔹 Flex (`lexer.l`)
Tokeniza los elementos del lenguaje:

- palabra `sqrt`
- paréntesis
- números reales

#### 🔹 Bison (`parser.y`)
Define la gramática del lenguaje y utiliza el puntero `yyin` para redirigir la entrada desde:

```
entrada.txt
```

#### 🔹 C (`CalcNewton.c`)
Implementa el **método numérico de Newton-Raphson** basado en:

```
https://github.com/jofsanchezci/metodo_newton_Rapson.git
```

El algoritmo garantiza convergencia mediante:

- iteraciones sucesivas
- tolerancia de `1e-10`

### Cómo ejecutarlo

1️⃣ Crear el archivo `entrada.txt`

```
sqrt(144)
```

2️⃣ Compilar y ejecutar

```bash
flex lexer.l
bison -d parser.y
gcc lex.yy.c parser.tab.c CalcNewton.c -lm -o calc
./calc
```

---

## 🔹 Punto 4: Comparación de Rendimiento (C vs Python)

### Enunciado

Realice una comparación de rendimiento entre:

- un **lenguaje compilado** (C)
- un **lenguaje interpretado** (Python)

usando una **función recursiva**.

### Explicación

Se utilizó el algoritmo de **Fibonacci recursivo** para calcular:

```
Fibonacci(40)
```

#### 🔹 C

Al ser compilado a **código máquina nativo**:

- gestiona las llamadas recursivas directamente en el **stack**
- tiene menor sobrecarga de ejecución

#### 🔹 Python

Al ser interpretado:

- cada llamada se maneja dentro de la **Python Virtual Machine (PVM)**
- se crean objetos adicionales
- aumenta el tiempo de ejecución

### Resultado observado

```
C ≈ 0.5 segundos
Python ≈ 7.7 segundos
```

### Cómo ejecutarlo

#### Para C

```bash
gcc fib.c -o fib_c
time ./fib_c
```

#### Para Python

```bash
time python3 figo.py
```

---

## 🔹 Punto 5: ANTLR para Secuencia Fibonacci

### Enunciado

Escriba un programa usando **ANTLR** que calcule la secuencia de Fibonacci.

Formato de entrada:

```
FIBO(20)
```

Debe retornar **toda la secuencia**, por ejemplo:

```
0, 1, 1, 2, 3, 5, 8, 13...
```

El **lenguaje objetivo** debe ser:

```
Python
```

### Explicación

El sistema se compone de dos partes:

#### 🔹 Gramática (`Fibo.g4`)

Define la estructura:

- léxica
- sintáctica

para reconocer el comando:

```
FIBO(numero)
```

#### 🔹 Listener (`main.py`)

Cuando el parser detecta la expresión válida:

1. Se ejecuta una función
2. Se genera la secuencia de Fibonacci **de forma iterativa**
3. Se formatea la salida como:

```
0, 1, 1, 2, 3, 5, 8...
```

para imprimirla en consola.

### Cómo ejecutarlo

Generar el parser con ANTLR:

```bash
antlr4 -Dlanguage=Python3 Fibo.g4
```

Ejecutar el programa:

```bash
python3 main.py
```

Ingresar en consola:

```
FIBO(8)
```

Luego presionar:

```
Ctrl + D
```

---

# 🛠️ Requisitos del Sistema

Para ejecutar todos los puntos del parcial se necesita tener instalado:

- **Python 3.x**
- **GCC** (Compilador de C)
- **Flex**
- **Bison**
- **ANTLR4**

Instalar runtime de ANTLR para Python:

```bash
pip install antlr4-python3-runtime
```

---