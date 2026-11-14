print("Bienvenido al registro de estudiantes.")
input("Presione Enter para continuar al menú...")
print("Cargando el menú...")

print("bienvenido al menu, maestro")
print("Por favor, seleccione una opción:")

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Registrar estudiante")
    print("2. Mostrar a todos los estudiantes registrados")
    print("3. Consultar el promedio de algún estudiante")
    print("4. Mostrar estadísticas generales del grupo")
    print("5. Salir del programa")

def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    nombre_formateado = nombre.title()

    if nombre_formateado in estudiantes:
        print(f"El estudiante {nombre_formateado} ya está registrado.")
        return

    calificaciones = []
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        calificaciones.append(calificacion)
    estudiantes[nombre_formateado] = calificaciones
    print(f"Estudiante {nombre_formateado} registrado exitosamente.")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\n--- ESTUDIANTES REGISTRADOS ---")
    for nombre, calificaciones in estudiantes.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"Nombre: {nombre}, Calificaciones: {calificaciones}")

def consultar_promedio(estudiantes):
    nombre = input("Ingrese el nombre del estudiante para consultar su promedio: ").strip()
    if nombre in estudiantes:
        calificaciones = estudiantes[nombre]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de {nombre} es: {promedio:.2f}")
    else:
        print(f"No se encontró al estudiante {nombre}.")

def mostrar_estadisticas(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    total_estudiantes = len(estudiantes)
    promedios = [sum(calificaciones) / len(calificaciones) for calificaciones in estudiantes.values()]
    promedio_general = sum(promedios) / total_estudiantes
    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"Total de estudiantes registrados: {total_estudiantes}")
    print(f"Promedio general del grupo: {promedio_general:.2f}")

estudiantes = {}

def consultar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante para consultar su promedio: ").strip()
    nombre_formateado = nombre.title()

    if nombre_formateado in estudiantes:
        calificaciones = estudiantes[nombre_formateado]
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"El promedio de {nombre_formateado} es: {promedio:.2f}")
    else:
        print(f"No se encontró al estudiante {nombre_formateado}.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        registrar_estudiante(estudiantes)
    elif opcion == "2":
        mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        consultar_estudiante(estudiantes)
    elif opcion == "4":
        mostrar_estadisticas(estudiantes)
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")