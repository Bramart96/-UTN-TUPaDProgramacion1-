# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 6: Validación de ingreso numérico

try:
    entrada = input("Ingrese un número: ")
    numero = float(entrada)
except ValueError:
    # JUSTIFICACIÓN: float() lanza ValueError cuando el texto no es numérico.
    print("Debe ingresar un número válido")
except Exception as error:
    # JUSTIFICACIÓN: captura de respaldo para cualquier error no previsto.
    print(f"Se produjo un error inesperado: {error}")
else:
    print(f"Número ingresado: {numero}")
