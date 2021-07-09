"""
La facultad de Ingeniería de la Universidad de Buenos Aires nos encarga la confección de un sistema de análisis de
los alumnos activos que cursan carreras en dicha casa de estudios.
Para ello el sistema deberá permitir, a demanda del usuario, ingresar para cada alumno activo, lo siguiente:
 Padrón
 Nombre
 Apellido
 Carrera
 Cantidad de materias aprobadas
 Nota promedio
 Año de Ingreso

Luego el programa deberá permitir emitir los siguientes reportes:
a) Indicar la carrera que tiene los mejores alumnos en base al promedio de todos ellos.
b) Determinar el promedio de materias aprobadas de los alumnos de una carrera que se le solicita al usuario.
c) Determinar el apellido más frecuente en la facultad.
d) Determinar la antigüedad promedio de los alumnos (en base a la fecha de hoy) que estén en el último
cuarto de la carrera, suponiendo que todas las carreras tienen 48 materias.
"""

def antiguedad_alumnos(alumnos: dict) -> None:
    contador = 0
    suma = 0
    for values in alumnos.values():
        if values[3] >= 36:
            contador += 1
            suma += values[5]
    if contador == 0:
        print("No hay alumnos en ultimo anio.")
    else:
        promedio = suma / contador
        print(f"El promedio de antiguedad de los alumnos en ultimo anio de carrera es de {2021 - promedio} anios.")

def apellido_mas_frecuente(alumnos: dict) -> None:
    apellidos = {}
    for values in alumnos.values():
        if values[1] not in apellidos:
            apellidos[values[1]] = 1
        else:
            apellidos[values[1]] += 1
    apellido_mfrecuente = max(apellidos, key=apellidos.get)

    print(f"El apellido mas frecuente es {apellido_mfrecuente}")

def mejor_carrera(alumnos: dict) -> None:
    carreras = {}
    for values in alumnos.values():
        #carrera = values[2]
        #nota_promedio = values[4]
        if values[2] not in carreras:
            carreras[values[2]] = [values[4], 1]
        else:
            carreras[values[2]] += [values[4], 1]

    for carrera, info_carrera in carreras.items():
        carreras[carrera] = info_carrera[0] / info_carrera[1]
    mejor_carrera = max(carreras,  key=carreras.get)


    #PARA RESOLVER EN EL CASO DE QUE EMPATEN MAS DE 1 CARRERA EL MEJOR PUESTO
    mejores_carreras = []
    empate = False
    for carrera in carreras.keys():
        if carreras[mejor_carrera] == carreras[carrera]:
            empate = True
            mejores_carreras.append(carrera)

    if empate:
        print(f"Las mejores carreras son: {mejores_carreras}")
    else:
        print(f"La mejor carrera segun el promedio de sus alumnos es {mejor_carrera}.")

def promedio_materia_seleccionada(alumnos: dict) -> None:
    carreras = []
    for values in alumnos.values():
        if values[2] not in carreras:
            carreras.append(values[2])
    print(carreras)

    carrera = input("Ingrese una carrera para ver el promedio de materias aprobadas de los alumnos: ")
    suma = 0
    contador = 0
    for values in alumnos.values():
        if carrera in values:
            suma += values[3]
            contador += 1
    promedio = suma/contador
    print(f"El promedio de materias aprobadas de la carrera {carrera} es {promedio}")

def ingreso_alumno(alumnos: dict) -> dict:
    padron = input("Ingrese su numero de padron: ")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    carrera = input("Ingrese el nombre de su carrera: ")
    cant_materias_aprobadas = int(input("Ingrese la cantidad de materias aprobadas: "))
    nota_promedio = int(input("Ingrese su nota promedio: "))
    anio_ingreso = int(input("Ingrese su anio de ingreso: "))
    info_alumno = [nombre, apellido, carrera, cant_materias_aprobadas, nota_promedio, anio_ingreso]

    alumnos[padron] = info_alumno

    return alumnos

def main() -> None:
    alumnos = {"1": ["patricio", "baez", "informatica", 37, 7, 2019],
     "2": ["lucas", "dri", "sistemas", 40, 3, 2015],
      "3": ["bautista", "dri", "abogacia", 15, 7, 2020],
       "4": ["gercho", "bourren", "informatica", 5, 9, 2021]}

    volver_menu = True
    while volver_menu:
        print("""
        a)Ingresar un alumno.
        b)Indicar la carrera que tiene los mejores alumnos en base al promedio de todos ellos.
        c)Determinar el promedio de materias aprobadas de los alumnos de una carrera que se le solicita al usuario.
        d)Determinar el apellido más frecuente en la facultad.
        e)Determinar la antigüedad promedio de los alumnos.
        """)
        opcion = input("Ingrese la letra correspondiente: ")
        if opcion == ("a" or "A"):
            alumnos = ingreso_alumno(alumnos)
        elif opcion == "b" or opcion == "B":
            mejor_carrera(alumnos)
        elif opcion == ("c" or "C"):
            promedio_materia_seleccionada(alumnos)
        elif opcion == ("d" or "D"):
            apellido_mas_frecuente(alumnos)
        elif opcion == ("e" or "E"):
            antiguedad_alumnos(alumnos)
        
        if input("Queres volver al menu?(A-SI / B-NO): ") == ("b" or "B"): volver_menu = False

main()