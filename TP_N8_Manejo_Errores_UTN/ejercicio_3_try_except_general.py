# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 3: Manejo general con try-except

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
    print(f"Resultado: {result}")
except Exception as error:
    # JUSTIFICACIÓN: Capturamos cualquier excepción para evitar que el programa se detenga.
    print(f"Se produjo un error en la división: {error}")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except Exception as error:
    # JUSTIFICACIÓN: Capturamos cualquier excepción para mantener el flujo del programa.
    print(f"Se produjo un error al acceder a la lista: {error}")
