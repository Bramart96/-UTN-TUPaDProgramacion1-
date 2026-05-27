# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 1: Identificación de errores
# Consigna: marcar los errores originales con comentarios explicativos.

# BLOQUE 1: Error de tipo en una división
a = 10
b = input("Introduce un número: ")   # input() siempre retorna str
result = a / b  # Error: TypeError -> no se puede dividir int / str sin conversión previa
print(f"Resultado: {result}")

# BLOQUE 2: Error de índice fuera de rango
numbers = [1, 2, 3]
print(numbers[5])  # Error: IndexError -> el índice 5 no existe (válidos: 0, 1, 2)
