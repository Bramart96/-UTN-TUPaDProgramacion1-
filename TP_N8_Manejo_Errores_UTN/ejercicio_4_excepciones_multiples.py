# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 4: Excepciones múltiples

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
except TypeError as e_tipo:
    # JUSTIFICACIÓN: int / str produce TypeError.
    print(f"Error de tipo detectado: {e_tipo}")
except ZeroDivisionError as e_cero:
    # JUSTIFICACIÓN: división por cero si el divisor fuera numérico y valiera 0.
    print(f"Error matemático detectado: {e_cero}")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e_indice:
    # JUSTIFICACIÓN: el índice solicitado no existe en la lista.
    print(f"Error de índice detectado: {e_indice}")
