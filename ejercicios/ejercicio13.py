'''
Cree un programa que permita al usuario elegir entre las siguientes opciones:
1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
3 - Cantidad de alumnos totales y promedio general.
4 - Quitar a un  alumno.
5 - Salir
'''


def quitar_alumno(lista_alumnos: list) -> None:
    entrada_usuario = input("Ingrese el nombre del alumno que quieres eliminar: ")
    for i in lista_alumnos:
        if entrada_usuario == i[0]:
            lista_alumnos.pop(i)
    
    if input("Quieres volver al menu? (si/no): ") == "si": menu()

def cantidad_alumnos_totales_promedio(lista_alumnos: list) -> None:
    print(f"La cantidad de alumnos total es: {len(lista_alumnos)}")
    suma_notas = 0
    for i in lista_alumnos:
        suma_notas += i[2]
    promedio = suma_notas / len(lista_alumnos)
    print(f"El promedio de las notas de todos los alumnos es {promedio}")

    if input("Quieres volver al menu? (si/no): ") == "si": menu()

def consultar_aprobados(lista_alumnos: list) -> None:
    for i in lista_alumnos:
        if i[2] >= 4:
            print(i[0])

    if input("Quieres volver al menu? (si/no): ") == "si": menu()

def agregar_alumno(lista_alumnos: list) -> None:
    entrada_usuario = input("Ingrese nombre, padrón y nota separados por una coma ',': ")
    entrada_usuario = entrada_usuario.split(",")
    entrada_usuario[2] = int(entrada_usuario[2])
    lista_alumnos.append(entrada_usuario)

    if input("Quieres volver al menu? (si/no): ") == "si": menu()

def menu(lista_alumnos: list) -> None:
    print('''
    1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
    2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
    3 - Cantidad de alumnos totales y promedio general.
    4 - Quitar a un  alumno.
    5 - Salir
    ''')
    eleccion = int(input("Ingrese el numero que corresponda a la opcion elegida: "))
    if eleccion == 1: agregar_alumno(lista_alumnos)
    elif eleccion == 2: consultar_aprobados(lista_alumnos)
    elif eleccion == 3: cantidad_alumnos_totales_promedio(lista_alumnos)
    elif eleccion == 4: quitar_alumno(lista_alumnos)

def main() -> None:
    lista_alumnos = [["matias", "1061232", 10], ["lucas", "213123", 0]]
    menu(lista_alumnos)

main()