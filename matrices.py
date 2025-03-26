# Función para ingresar una nueva persona
def ingresar_persona():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    dni = input("Ingrese el DNI: ")
    
    # Ingresar los teléfonos como lista separada por comas
    telefonos = input("Ingrese los teléfonos (separados por coma): ").split(',')
    
    # Ingresar los hijos como lista separada por comas
    hijos = input("Ingrese los nombres de los hijos (separados por coma): ").split(',')
    
    # Crear una lista con la información de la persona
    persona = [nombre, apellido, dni, telefonos, hijos]
    
    return persona

# Función para mostrar todos los datos
def mostrar_datos(matriz):
    if len(matriz) == 0:
        print("No hay datos ingresados.")
    else:
        for persona in matriz:
            print(f"Nombre: {persona[0]} {persona[1]}")
            print(f"DNI: {persona[2]}")
            print(f"Teléfonos: {', '.join(persona[3])}")
            print(f"Hijos: {', '.join(persona[4])}")
            print(f"Cantidad de teléfonos: {len(persona[3])}")
            print(f"Cantidad de hijos: {len(persona[4])}")
            print("-" * 40)

# Función para filtrar por DNI
def filtrar_por_dni(matriz):
    dni_buscar = input("Ingrese el DNI para filtrar: ")
    encontrado = False
    for persona in matriz:
        if persona[2] == dni_buscar:
            print(f"Nombre: {persona[0]} {persona[1]}")
            print(f"DNI: {persona[2]}")
            print(f"Teléfonos: {', '.join(persona[3])}")
            print(f"Hijos: {', '.join(persona[4])}")
            print(f"Cantidad de teléfonos: {len(persona[3])}")
            print(f"Cantidad de hijos: {len(persona[4])}")
            print("-" * 40)
            encontrado = True
            break
    if not encontrado:
        print("No se encontró ninguna persona con ese DNI.")

# Función para mostrar el menú
def mostrar_menu():
    print("\n----- Menú -----")
    print("1. Ingresar nueva persona")
    print("2. Mostrar todos los datos")
    print("3. Filtrar por DNI")
    print("4. Salir")

# Función principal
def main():
    matriz = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            persona = ingresar_persona()
            matriz.append(persona)
        elif opcion == '2':
            mostrar_datos(matriz)
        elif opcion == '3':
            filtrar_por_dni(matriz)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
