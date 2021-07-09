'''
Cree un programa que permita al usuario elegir entre las siguientes opciones:
1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
3 - Cantidad de alumnos totales y promedio general.
4 - Quitar a un  alumno.
5 - Salir
'''

#Constantes que servirán de índices más adelante.
PADRON = 0
NOTA = 1
def agregar_alumno(alumnos : dict) -> None:
    '''
    Agrega el alumno al diccionario alumnos
    '''
    nombre = input("Nombre del alumno: ")
    padron = int(input("Padron del alumno: "))
    nota = float(input("Nota del alumno: "))
    alumnos[padron] = [nombre, nota]
def mostrar_aprobados(alumnos):
    '''
    Recibe un diccionario con los alumnos. Muestra en pantalla todos los alumnos con nota > 4
    '''
    print("Los alumnos aprobados son: ")
    for padron, datos in alumnos.items():
        if datos[NOTA] > 4:
            print(f"{alumnos[padron][0]}, nota: {datos[1]}") 
def quitar_alumno(alumnos : dict, padron : int) -> None:
    '''
    Elmina el alumno del diccionario alumnos
    '''
    del alumnos[padron]
def calcular_promedio(alumnos: dict) -> float:
    '''
    Calcular el promedio general
    '''
    cant_alumnos = 0
    suma_notas = 0
    for alumno in alumnos:
        cant_alumnos += 1
        suma_notas += alumnos[alumno][NOTA]
    return suma_notas / cant_alumnos
def main():
    alumnos = {}
    print("""
        1 - Agregar un alumno: debe solicitarse nombre, padrón y nota.
        2 - Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
        3 - Cantidad de alumnos totales y promedio general.
        4 - Quitar a un  alumno.
        5 - Salir
        """)
    opcion = int(input("Elige una opcion: "))
    while opcion != 5:
        if opcion == 1:
            #Pido al usuario los datos del alumno
            agregar_alumno(alumnos)
            print("Alumno agregado con exito")
        if opcion == 2:
            mostrar_aprobados(alumnos)
        if opcion == 3:
            suma_notas = 0
            for _, nota in alumnos.values():
                suma_notas += nota
            print(f"Alumnos totales: {len(alumnos)}, promedio general: {suma_notas/len(alumnos)}")
        if opcion == 4:
            padron = int(input("Ingrese el padron del alumno que desea eliminar: "))
            quitar_alumno(alumnos, padron)
            print("Alumno quitado con éxito")
        opcion = int(input("Vuelva a ingresar una opcion: "))
    print("Saliendo...")
main()