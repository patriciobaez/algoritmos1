"""
Ejercicio) “@RumboCircular” es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular
 además de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos
  para la comunidad general.

Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijos) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500

El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la
 creación de un pequeño sistema que permita organizar la asistencia de los participantes.

Los requerimientos que nos solicitan son los siguientes:
a- ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos.
 Nombre, cantidad de días, costo, cantidad de vacantes, fechas de dictado.
b- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
c- Mostrar el o los cursos cuya cantidad de vacantes se la máxima.
d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
"""

#cursos = {num_curso: ["Nombre", cant_dias, costo, cant_vacantes, ["fechas_dictado"]]}

def fechas_dictado_3(cursos: dict) -> None:
  for value in cursos.values():
    if len(value[4]) >= 3:
      print(value[0])

def max_cant_vacantes(cursos: dict) -> None:
    cursos_vacantes = {}
    for key, values in cursos.items():
        if key not in cursos_vacantes.keys():
            cursos_vacantes[key] = values[3]

    curso_mas_vacantes = max(cursos_vacantes,  key=cursos_vacantes.get)

    #PARA RESOLVER EN EL CASO DE QUE EMPATEN MAS DE 1 CARRERA EL MEJOR PUESTO
    cursos_mas_vacantes = []
    empate = False
    for curso in cursos_vacantes.keys():
        if cursos_vacantes[curso_mas_vacantes] == cursos_vacantes[curso]:
            empate = True
            cursos_mas_vacantes.append(cursos[curso][0])

    if empate:
        print(f"Los cursos cuya cantidad de vacantes es la máxima son: {cursos_mas_vacantes}")
    else:
        print(f"El curso cuya cantidad de vacantes es la máxima es: {curso_mas_vacantes}.")

def costo_mayor_1150(cursos:dict) -> None:
  for valor in cursos.values():
    if valor[2] > 1150:
      print(valor[0])

def mod(cursos: dict) -> dict:
  for key, value in cursos.items():
    print(f"Numero de curso: {key}: {value[0]}")
  curso_modificar = int(input("Ingrese el numero del curso que quiere modificar: "))

  nombre = input("Ingrese el nombre del curso: ")
  cant_dias = int(input("Ingrese la cantidad de dias del curso: "))
  costo = int(input("Ingrese el costo del curso: "))
  cant_vacantes = int(input("Ingrese la cantidad de vacantes: "))
  fechas_dictado = []
  salir = False
  while salir == False:
    fecha_dictado = input("Ingrese la fecha de dictado de la siguiente forma(dia/mes/año)(sin los parentesis): ")
    fechas_dictado.append(fecha_dictado)
    opcion = input("Quiere agregar otra fecha de dictado. (A-Si/B-No): ")
    if opcion == "B" or opcion == "b": salir = True

  alta_info = [nombre, cant_dias, costo, cant_vacantes, fechas_dictado]
  cursos[curso_modificar] = alta_info
  return cursos

def baja(cursos: dict) -> dict:
  for key, value in cursos.items():
    print(f"Numero de curso: {key}: {value[0]}")
  curso_eliminar = int(input("Ingrese el numero del curso que quiere eliminar: "))
  del cursos[curso_eliminar]

def alta() -> list:
  nombre = input("Ingrese el nombre del curso: ")
  cant_dias = int(input("Ingrese la cantidad de dias del curso: "))
  costo = int(input("Ingrese el costo del curso: "))
  cant_vacantes = int(input("Ingrese la cantidad de vacantes: "))
  fechas_dictado = []
  salir = False
  while salir == False:
    fecha_dictado = input("Ingrese la fecha de dictado de la siguiente forma(dia/mes/año)(sin los parentesis): ")
    fechas_dictado.append(fecha_dictado)
    opcion = input("Quiere agregar otra fecha de dictado. (A-Si/B-No): ")
    if opcion == "B" or opcion == "b": salir = True

  alta_info = [nombre, cant_dias, costo, cant_vacantes, fechas_dictado]
  return alta_info

def abm_cursos(cursos: dict,num_curso: list) -> dict:
  volver_menu = True
  while volver_menu:
    print("A-Agregar un curso.\nB-Eliminar un curso.\nC-Modificar un curso.")
    opcion = input("Ingrese la letra correspondiente: ")
    if opcion == "a" or opcion == "A":
      alta_info = alta()
      cursos[num_curso[0]] = alta_info
      num_curso[0] += 1
    elif opcion == "b" or opcion == "B":
      cursos = baja(cursos)
    elif opcion == "c" or opcion == "C":
      cursos = mod(cursos)

    opcion_volver_menu = input("Queres volver al menu de Alta, Baja y Modificion?(A-SI / B-NO): ")
    if opcion_volver_menu == "b" or opcion_volver_menu == "B":
      volver_menu = False


  return cursos

def main() -> None:
  num_curso = [4]
  cursos = {
  1: ["Aprendé a hacer tu propio compost", 1, 950, 1, ["10/07/2021", "05/07/2021", "30/06/2021"]],
  2: ["Los niños y el medioambiente", 2, 990, 1, ["30/06/2021"]],
  3: ["Tu huerta orgánica", 4, 2500, 0, ["05/07/2021", "30/06/2021"]]
  }

  volver_menu = True
  while volver_menu:
      print("""
      a- ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos.
      Nombre, cantidad de días, costo, cantidad de vacantes, fechas de dictado.
      b- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
      c- Mostrar el o los cursos cuya cantidad de vacantes se la máxima.
      d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
      e- Mostrar todos los cursos.
      """)
      opcion = input("Ingrese la letra correspondiente: ")
      if opcion == "a" or opcion == "A":
          cursos = abm_cursos(cursos, num_curso)
      elif opcion == "b" or opcion == "B":
          costo_mayor_1150(cursos)
      elif opcion == "c" or opcion == "C":
          max_cant_vacantes(cursos)
      elif opcion == "d" or opcion == "D":
          fechas_dictado_3(cursos)
      elif opcion == "e" or opcion == "E":
        for key, value in cursos.items():
          print(f"{key}: {value}")

      opcion_volver_menu = input("Queres volver al menu principal?(A-SI / B-NO): ")
      if opcion_volver_menu == "b" or opcion_volver_menu == "B":
          volver_menu = False

main()

