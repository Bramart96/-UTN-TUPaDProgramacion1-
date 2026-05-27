
# ACTIVIDAD PRACTICA UTN - ARCHIVOS PYTHON
# Profe, todo organizado en funciones para poder estar mas ordenado y llamar al bloque por actividad si asi se requiere!.
# El archivo "productos.txt" esta creado en la carpeta raiz.

# El siguiente bloque crea el archivo productos.txt con 3 productos (a modo prueba)

def actividad1():
    with open("productos.txt", "w") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,850,15\n")
        archivo.write("Goma,75,50\n")
    print("✅ Archivo creado correctamente.\n")

# El siguiente bloque lee y muestra productos de archivo productos.txt

def actividad2():
    print("📦 Lista de productos:")
    print("-" * 45)
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            partes   = linea.strip().split(",")
            nombre   = partes[0]
            precio   = partes[1]
            cantidad = partes[2]
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    print("-" * 45)

# El siguiente bloque pide al usuario un nuevo producto y lo agrega al archivo productos.txt

def actividad3():
    print("\n➕ Agregar nuevo producto:")
    print("-" * 45)
    
    nombre   = input("Ingresá el nombre del producto: ")
    precio   = input("Ingresá el precio: ")
    cantidad = input("Ingresá la cantidad: ")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f"\n✅ Producto '{nombre}' agregado correctamente.\n")

# El siguiente bloque lee el archivo productos.txt y carga los productos en una lista de diccionarios   

def actividad4():
    """Carga los productos del archivo en una lista de diccionarios"""
    productos = []

    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            producto = {
                "nombre"  : partes[0],
                "precio"  : float(partes[1]),
                "cantidad": int(partes[2])
            }
            productos.append(producto)

    print("\n📋 Lista de diccionarios cargada:")
    print("-" * 45)
    for p in productos:
        print(p)
    print("-" * 45)

    return productos  

# El siguiente bloque busca un producto por nombre en la lista de diccionarios y muestra su información

def actividad5(productos):
    """Busca un producto por nombre en la lista de diccionarios"""
    print("\n🔍 Buscar producto:")
    print("-" * 45)

    nombre_buscar = input("Ingresá el nombre del producto a buscar: ")

    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"\n✅ Producto encontrado:")
            print(f"   Nombre  : {p['nombre']}")
            print(f"   Precio  : ${p['precio']}")
            print(f"   Cantidad: {p['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print(f"\n❌ El producto '{nombre_buscar}' no existe.\n")
    
    print("-" * 45)

# El siguiente bloque actualiza la cantidad de un producto y sobrescribe el archivo con la lista actualizada

def actividad6(productos):
    """Sobrescribe el archivo con la lista de productos actualizada"""
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    
    print("\n💾 Archivo actualizado correctamente.\n")


actividad1()
actividad2()
actividad3()
productos = actividad4()  
actividad5(productos)
actividad6(productos)