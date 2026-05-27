
# Ejercicio 2 - Login

usuario_ok = "alumno"
clave_ok = "python123"

intentos = 0
acceso = False

while intentos < 3:
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_ok and clave == clave_ok:
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("1 Estado 2 Cambiar clave 3 Mensaje 4 Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error número")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Fuera de rango")
        elif opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error mínimo 6")
            else:
                confirmar = input("Confirmar: ")
                if nueva == confirmar:
                    clave_ok = nueva
                    print("Clave cambiada")
                else:
                    print("No coincide")
        elif opcion == 3:
            print("Seguí adelante, vos podés!")
