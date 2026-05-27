# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 2: Corrección lógica sin usar try-except

# BLOQUE 1: Corrección del TypeError
a = 10
b_valido = float(input("Introduce un número para dividir: "))  # Convertimos str a float
resultado_valido = a / b_valido
print(f"Resultado: {resultado_valido}")

# BLOQUE 2: Corrección del IndexError
numbers_valido = [1, 2, 3]
print(numbers_valido[2])  # Accedemos al último índice válido
