
# Práctico 11 - Recursividad
# UTN - TUP

# ================================================================
# EJERCICIO 1 - Factorial recursivo
# ================================================================

def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Parámetros:
        n (int): Número entero no negativo.

    Retorna:
        int: El factorial de n.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def mostrar_factoriales(i, limite):
    """
    Muestra de forma recursiva el factorial de cada entero entre i y el límite.

    Parámetros:
        i (int): Valor actual desde el que se calcula.
        limite (int): Valor máximo hasta el que se muestran factoriales.
    """
    if i > limite:
        return
    print(f"  {i}! = {factorial(i)}")
    mostrar_factoriales(i + 1, limite)


def ejercicio_1():
    """Interfaz de usuario para el Ejercicio 1: Factorial."""
    print("\n[ EJERCICIO 1 - Factorial Recursivo ]")
    try:
        n = int(input("  Ingresá un número entero positivo: "))
        if n <= 0:
            print("  ⚠ Error: debe ser un entero mayor a 0.")
        else:
            print(f"\n{'='*45}")
            print(f"  FACTORIALES del 1 al {n}")
            print(f"{'='*45}")
            mostrar_factoriales(1, n)
    except ValueError:
        print("  ⚠ Error: ingresá un número entero válido.")


# ================================================================
# EJERCICIO 2 - Serie de Fibonacci
# ================================================================

def fibonacci(n):
    """
    Calcula el n-ésimo término de la serie de Fibonacci de forma recursiva.

    Parámetros:
        n (int): Posición en la serie (base 0).

    Retorna:
        int: El valor de Fibonacci en la posición n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci(i, limite):
    """
    Muestra de forma recursiva la serie de Fibonacci desde la posición i
    hasta el límite indicado.

    Parámetros:
        i (int): Posición actual en la serie.
        limite (int): Posición final de la serie a mostrar.
    """
    if i > limite:
        return
    print(f"  posición {i}: {fibonacci(i)}")
    mostrar_fibonacci(i + 1, limite)


def ejercicio_2():
    """Interfaz de usuario para el Ejercicio 2: Fibonacci."""
    print("\n[ EJERCICIO 2 - Serie de Fibonacci ]")
    try:
        n = int(input("  Ingresá la posición hasta donde mostrar la serie: "))
        if n < 0:
            print("  ⚠ Error: la posición debe ser un número no negativo.")
        else:
            print(f"\n{'='*45}")
            print(f"  SERIE DE FIBONACCI hasta posición {n}")
            print(f"{'='*45}")
            mostrar_fibonacci(0, n)
    except ValueError:
        print("  ⚠ Error: ingresá un número entero válido.")


# ================================================================
# EJERCICIO 3 - Potencia recursiva
# ================================================================

def potencia(base, exponente):
    """
    Calcula la potencia de un número usando recursión.

    Parámetros:
        base (float): La base de la potencia.
        exponente (int): El exponente, debe ser un entero no negativo.

    Retorna:
        float: El resultado de elevar la base al exponente.
    """
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)


def ejercicio_3():
    """Interfaz de usuario para el Ejercicio 3: Potencia."""
    print("\n[ EJERCICIO 3 - Potencia Recursiva ]")
    try:
        base = float(input("  Ingresá la base: "))
        exp  = int(input("  Ingresá el exponente (entero >= 0): "))
        if exp < 0:
            print("  ⚠ Error: el exponente debe ser no negativo.")
        else:
            resultado = potencia(base, exp)
            print(f"\n  Resultado: {base}^{exp} = {resultado}")
    except ValueError:
        print("  ⚠ Error: ingresá valores numéricos válidos.")


# ================================================================
# EJERCICIO 4 - Decimal a Binario
# ================================================================

def decimal_a_binario(n):
    """
    Convierte un número entero positivo a su representación binaria
    como cadena de texto, usando recursión.

    Parámetros:
        n (int): Número entero positivo en base decimal.

    Retorna:
        str: Representación binaria del número como cadena de texto.
    """
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)


def ejercicio_4():
    """Interfaz de usuario para el Ejercicio 4: Decimal a Binario."""
    print("\n[ EJERCICIO 4 - Decimal a Binario ]")
    try:
        n = int(input("  Ingresá un número entero positivo: "))
        if n < 0:
            print("  ⚠ Error: el número debe ser positivo.")
        else:
            print(f"\n  {n} en binario es: {decimal_a_binario(n)}")
    except ValueError:
        print("  ⚠ Error: ingresá un número entero válido.")


# ================================================================
# EJERCICIO 5 - Palíndromo
# ================================================================

def es_palindromo(palabra):
    """
    Determina si una cadena de texto es un palíndromo usando recursión.

    Parámetros:
        palabra (str): Cadena sin espacios ni tildes.

    Retorna:
        bool: True si la cadena es palíndromo, False si no lo es.
    """
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


def ejercicio_5():
    """Interfaz de usuario para el Ejercicio 5: Palíndromo."""
    print("\n[ EJERCICIO 5 - Palíndromo Recursivo ]")
    try:
        palabra = input("  Ingresá una palabra (sin espacios ni tildes): ").strip().lower()
        if not palabra:
            print("  ⚠ Error: la palabra no puede estar vacía.")
        else:
            resultado = es_palindromo(palabra)
            estado = "✔ SÍ es un palíndromo" if resultado else "✘ NO es un palíndromo"
            print(f"\n  '{palabra}' → {estado}")
    except ValueError:
        print("  ⚠ Error: entrada inválida.")


# ================================================================
# EJERCICIO 6 - Suma de dígitos
# ================================================================

def suma_digitos(n):
    """
    Calcula la suma de todos los dígitos de un número entero positivo
    usando recursión y operaciones matemáticas, sin convertir a string.

    Parámetros:
        n (int): Número entero positivo.

    Retorna:
        int: La suma de todos los dígitos del número.

    Ejemplos:
        suma_digitos(1234) -> 10   (1 + 2 + 3 + 4)
        suma_digitos(305)  ->  8   (3 + 0 + 5)
    """
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)


def ejercicio_6():
    """Interfaz de usuario para el Ejercicio 6: Suma de dígitos."""
    print("\n[ EJERCICIO 6 - Suma de Dígitos ]")
    try:
        n = int(input("  Ingresá un número entero positivo: "))
        if n < 0:
            print("  ⚠ Error: el número debe ser positivo.")
        else:
            resultado = suma_digitos(n)
            print(f"\n  Suma de dígitos de {n} = {resultado}")
    except ValueError:
        print("  ⚠ Error: ingresá un número entero válido.")


# ================================================================
# EJERCICIO 7 - Pirámide de bloques
# ================================================================

def contar_bloques(n):
    """
    Calcula el total de bloques para construir una pirámide, donde el nivel
    base tiene n bloques y cada nivel superior tiene uno menos.

    Parámetros:
        n (int): Número de bloques en el nivel base (entero positivo).

    Retorna:
        int: Total de bloques en toda la pirámide.

    Ejemplos:
        contar_bloques(1) ->  1   (1)
        contar_bloques(2) ->  3   (2 + 1)
        contar_bloques(4) -> 10   (4 + 3 + 2 + 1)
    """
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


def construir_suma(n):
    """
    Construye recursivamente la cadena que representa la suma de niveles
    de la pirámide, en formato "n + (n-1) + ... + 1".

    Parámetros:
        n (int): Nivel actual de la pirámide.

    Retorna:
        str: Cadena con la representación de la suma.
    """
    if n == 1:
        return "1"
    return str(n) + " + " + construir_suma(n - 1)


def ejercicio_7():
    """Interfaz de usuario para el Ejercicio 7: Pirámide de bloques."""
    print("\n[ EJERCICIO 7 - Pirámide de Bloques ]")
    try:
        n = int(input("  Ingresá la cantidad de bloques en la base: "))
        if n <= 0:
            print("  ⚠ Error: debe ser un entero mayor a 0.")
        else:
            total = contar_bloques(n)
            suma_str = construir_suma(n)
            print(f"\n  Pirámide con base de {n} bloques:")
            print(f"  {suma_str} = {total} bloques en total")
    except ValueError:
        print("  ⚠ Error: ingresá un número entero válido.")


# ================================================================
# EJERCICIO 8 - Contar dígito específico
# ================================================================

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito específico dentro de un número
    entero positivo, usando recursión y operaciones matemáticas.

    Parámetros:
        numero (int): Número entero positivo donde se busca el dígito.
        digito (int): Dígito a buscar, entre 0 y 9.

    Retorna:
        int: Cantidad de veces que el dígito aparece en el número.
    """
    coincide = 1 if (numero % 10) == digito else 0
    if numero < 10:
        return coincide
    return coincide + contar_digito(numero // 10, digito)


def ejercicio_8():
    """Interfaz de usuario para el Ejercicio 8: Contar dígito."""
    print("\n[ EJERCICIO 8 - Contar Dígito en un Número ]")
    try:
        numero = int(input("  Ingresá el número entero positivo: "))
        digito = int(input("  Ingresá el dígito a buscar (0-9): "))
        if numero < 0:
            print("  ⚠ Error: el número debe ser positivo.")
        elif not (0 <= digito <= 9):
            print("  ⚠ Error: el dígito debe estar entre 0 y 9.")
        else:
            resultado = contar_digito(numero, digito)
            print(f"\n  El dígito {digito} aparece {resultado} vez/veces en {numero}.")
    except ValueError:
        print("  ⚠ Error: ingresá valores numéricos válidos.")




EJERCICIOS = {
    1: ejercicio_1,
    2: ejercicio_2,
    3: ejercicio_3,
    4: ejercicio_4,
    5: ejercicio_5,
    6: ejercicio_6,
    7: ejercicio_7,
    8: ejercicio_8,
}


def main():
    """Función principal para ejecutar el programa."""
    print("=== PRÁCTICO 11 - RECURSIVIDAD ===")
    while True:
        print("\nSeleccioná un ejercicio para ejecutar:")
        for num in range(1, 9):
            print(f"  {num}. Ejercicio {num}")
        print("  0. Salir")
        try:
            opcion = int(input("Ingresá el número del ejercicio a ejecutar: "))
            if opcion == 0:
                print("¡Hasta luego!")
                break
            elif opcion in EJERCICIOS:
                EJERCICIOS[opcion]()
            else:
                print("  ⚠ Opción inválida, intentá de nuevo.")
        except ValueError:
            print("  ⚠ Error: ingresá un número entero válido.")
 
if __name__ == "__main__":
    main()
