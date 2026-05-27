# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 5: Excepciones múltiples con else y finally

try:
    a = 10
    b = input("Introduce un número: ")
    result = a / b
except TypeError as e_tipo:
    print(f"Error de tipo detectado: {e_tipo}")
except ZeroDivisionError as e_cero:
    print(f"Error matemático detectado: {e_cero}")
else:
    # JUSTIFICACIÓN: solo se ejecuta si no ocurrió ninguna excepción.
    print(f"Resultado correcto: {result}")
finally:
    # JUSTIFICACIÓN: siempre se ejecuta, haya o no error.
    print("Fin del bloque de división.")

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError as e_indice:
    print(f"Error de índice detectado: {e_indice}")
else:
    print("Acceso correcto a la lista.")
finally:
    print("Fin del bloque de lista.")
