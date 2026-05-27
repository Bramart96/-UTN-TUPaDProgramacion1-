
# Ejercicio 3 - Agenda sin listas

lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

def mostrar_lunes():
    print("Lunes:", lunes1, lunes2, lunes3, lunes4)

def mostrar_martes():
    print("Martes:", martes1, martes2, martes3)

op = ""
while op != "5":
    print("1 Reservar 2 Cancelar 3 Ver día 4 Resumen 5 Salir")
    op = input("Opción: ")

    if op == "1":
        dia = input("1 Lunes 2 Martes: ")
        nombre = input("Nombre: ")
        while not nombre.isalpha():
            nombre = input("Error nombre: ")

        if dia == "1":
            if lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Lleno")
        elif dia == "2":
            if martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("Lleno")

    elif op == "3":
        dia = input("1 Lunes 2 Martes: ")
        if dia == "1":
            mostrar_lunes()
        else:
            mostrar_martes()
