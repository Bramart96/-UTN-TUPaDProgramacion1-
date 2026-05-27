"""
Ejercicio 9
Agenda con claves compuestas (día, hora).
"""

# Este bloque crea una agenda usando tuplas (día, hora) como clave y evento como valor
agenda = {
    ("Lunes", "10:00"): "Reunión de equipo",
    ("Martes", "15:00"): "Clase de programación",
    ("Miércoles", "09:00"): "Entrenamiento"
}

dia = input("Ingresá un día: ")
hora = input("Ingresá una hora (HH:MM): ")

# Este bloque consulta si existe un evento en la clave compuesta ingresada
clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas en ese horario.")
