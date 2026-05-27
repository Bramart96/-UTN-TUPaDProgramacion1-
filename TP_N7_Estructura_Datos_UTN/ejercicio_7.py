"""
Ejercicio 7
Procesar asistencias repetidas a una capacitación.
"""

# Este bloque define una lista con nombres repetidos simulando asistencias múltiples
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]

print("Lista original:", asistencias)

# Este bloque convierte la lista en set para eliminar repetidos
asistieron = set(asistencias)
print("Asistieron al menos una vez:", asistieron)

# Este bloque cuenta cuántas veces asistió cada empleado
conteo = {}
for persona in asistencias:
    conteo[persona] = conteo.get(persona, 0) + 1

print("Cantidad de asistencias por empleado:", conteo)
