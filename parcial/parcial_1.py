#clinica la fuerza
#• Número de historia clínica (un número entero).
#• Nombre del paciente (una cadena de texto).
#• Edad del paciente (un número entero).
#• Diagnóstico (una cadena de texto).
#• Cantidad de días de internación (un número entero).


#1. Interfaz del programa: mostrar un menu interactivo.
def mostrar_menu():
    print("--- sistema de gestion de clinica ---")
    print("1. Cargar paciente/s")
    print("2. mostrar todos los pacientes")
    print("3. buscar pacientes por numero de historial clinica")
    print("4. ordenar pacientes por numero de historial")
    print("5. mostrar pacientes con mas dias de internación")
    print("6. mostrar pacientes con menos dias de internación")
    print("7. cantidad de pacientes con mas de 5 dias de internación")
    print("8. promedio de dias de inernación de todos los pacientes")
    print("9. salir")

#2. Cargar pacientes: permitir al usuario ingresar los datos de los pacientes almacenado informacion en una lista
def cargar_pacientes():
    pacientes= []
    cantidad = int(input("ingrese la cantidad de pacientes a cargar: "))
    for _ in range(cantidad):
        historia_clínico= float(input("Ingrese el numero del historial clinica: "))
        nombre_de_paciente = (input("Ingrese el nombre del paciente: "))
        edad_del_paciente = float(input("Ingrese la edad del paciente: "))
        Diagnóstico = (input("Ingrese el diagnostico del paciente: "))
        días_de_internación = float(input("ingrese la cantidad de dias de internación: "))
        paciente = ([historia_clínico, nombre_de_paciente, edad_del_paciente,Diagnóstico,días_de_internación])
        pacientes.append(paciente)
    return pacientes

#3. Mostrar la lista de pacientes: imprimir los datos de los pacientes almacenados.
def mostrar_lista_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    print("pacientes = [")
    for paciente in pacientes:
        print(f"    [{paciente[0]}, \"{paciente[1]}\", {paciente[2]}, \"{paciente[3]}\", {paciente[4]}],")
    print("]")

#4. Búsqueda de pacientes: funcion que dado el num historial clinico buscar el la lista y mostrar los datos del paciente, o mostrar que no se encontro.
def buscar_pacientes(pacientes):
    historia_clinica = float(input("ingrese el numero de historia clinica a buscar: "))
    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            print(f"paciente encontrado: [{paciente[0]}, \"{paciente[1]}\", {paciente[2]}, \"{paciente[3]}\", {paciente[4]}]")
            return
    print(f"no se encontro paciente/s")

#5. Ordenamiento de pacientes: funcion que permita ordenar la lista de pacientes por num de historial en forma acendente.
def ordenar_pacientes(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
    n = len(pacientes)
    for i in range(n):
        for j in range(0, n-i-1):
            if pacientes[j][0] > pacientes[j+1][0]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                pacientes[j], pacientes[j+1] = pacientes[j+1], pacientes[j]
    print("Pacientes ordenados por Historia Clínica:")
    mostrar_lista_pacientes(pacientes)

# 6. Determinar el paciente con mayor cantidad de días de internación: mostrar al paciente con mas dias de internacion, mostrando sus datos.
def paciente_mas_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    # bandera mayor
    paciente_mas = pacientes[0]  
    for paciente in pacientes:
        if paciente[4] > paciente_mas[4]:
            paciente_mas = paciente
    print(f"Paciente con más días de internacion:\"[{paciente_mas[0]}, \"{paciente_mas[1]}\", {paciente_mas[2]}, \"{paciente_mas[3]}\", {paciente_mas[4]}]")

#7. Determinar el paciente con menor cantidad de días de internación: maostrar al paciente con menos dias de internacion, mostrando sus datos
def paciente_menos_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    # bandera menor
    paciente_menos = pacientes[0] 
    for paciente in pacientes:
        if paciente[4] < paciente_menos[4]: 
            paciente_menos = paciente  

    print(f"Paciente con más días de internacion:\"[{paciente_menos[0]}, \"{paciente_menos[1]}\", {paciente_menos[2]}, \"{paciente_menos[3]}\", {paciente_menos[4]}]")

#8. Cantidad de pacientes con días de internación mayor a 5 días: 
def contar_pacientes_mas_5_dias(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    # bandera contador
    contador = 0
    for paciente in pacientes:
        if paciente[4] > 5: 
            contador += 1 
    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

#9. Promedio de días de internación de todos los pacientes:
def promedio_dias_internacion(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    #contador de dias
    total_dias = 0 
    for paciente in pacientes:  
        total_dias += paciente[4] 
    promedio = total_dias / len(pacientes)
    print(f"Promedio de días de internación: {promedio}")


def menu():
    pacientes = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            pacientes = cargar_pacientes()
        elif opcion == '2':
            mostrar_lista_pacientes(pacientes)
        elif opcion == '3':
            buscar_pacientes(pacientes)
        elif opcion == '4':
            ordenar_pacientes(pacientes)
        elif opcion == '5':
            paciente_mas_dias_internacion(pacientes)
        elif opcion == '6':
            paciente_menos_dias_internacion(pacientes)
        elif opcion == '7':
            contar_pacientes_mas_5_dias(pacientes)
        elif opcion == '8':
            promedio_dias_internacion(pacientes)
        elif opcion == '9':
            print("Saliendo del sistema.")
            break
        else:
            print("opcion no valida, intenta de nuevo: ")
