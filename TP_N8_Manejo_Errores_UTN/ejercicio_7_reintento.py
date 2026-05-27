# Trabajo Práctico N°8 - Manejo de Errores (UTN)
# Ejercicio 7: Validación con reintento controlado

while True:
    try:
        entrada = input("Ingrese un número a validar (o escriba 'salir' para cancelar): ")

        # Permite al usuario salir del programa de forma controlada
        if entrada.lower() == "salir":
            print("Operación cancelada. Saliendo del programa...")
            break

        numero = float(entrada)
        print(f"¡Excelente! El número validado es: {numero}")
        break

    except ValueError:
        # JUSTIFICACIÓN: el valor ingresado no puede convertirse a número.
        print("Debe ingresar un número válido. Intente nuevamente.")
    except Exception as error:
        # JUSTIFICACIÓN: captura cualquier otra excepción inesperada.
        print(f"Se produjo un error inesperado: {error}")
    finally:
        # JUSTIFICACIÓN: informa el cierre de cada intento.
        print("Intento finalizado.\n")
