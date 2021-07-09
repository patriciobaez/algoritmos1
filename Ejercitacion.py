'''
“@RumboCircular” es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- ABM (Alta – Baja – Modificación) de cursos. Se podrá cargar la siguiente infomación de los cursos. Nombre, cantidad de días, costo, cantidad de vacantes, fechas de dictado.
b- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
c- Mostrar el o los cursos cuya cantidad de vacantes se la máxima.
d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
'''

# cursos = {codigo_curso : {"Nombre": , "Dias" : , "Costo" : , "Vacantes" : , "Fechas" : [], "Codigo" : }}

def imprimir_curso(curso : dict) -> None:
    print("\n\n")
    for k,v in curso.items():
        print(f"\t {k} : {v}")
        if k == "Codigo":
            print()

def listar_fechas_dictado_mayor_a(valor : int, cursos : dict) -> None:
    lista = list()
    for curso in cursos.values():
        if len(curso["Fechas"]) >= valor: lista.append(curso)
    
    print(f"\n\nCursos con fechas de dictado mayor a {valor}")
    print("______________________________________________")
    for curso in lista:
        imprimir_curso(curso)

def listar_vacantes_max(cursos : dict) -> None:
    maximo = 0
    for curso in cursos.values():
        vacantes = curso["Vacantes"]
        if int(vacantes) > maximo: maximo = int(vacantes)

    lista_max = list()
    for curso in cursos.values():
        if int(curso["Vacantes"]) == maximo: lista_max.append(curso)

    print("\n\nCursos con la mayor cantidad de vacantes")
    print("________________________________________")
    for curso in lista_max:
        imprimir_curso(curso)

def listar_mayor_a_valor(valor : int, cursos : dict) -> None:
    cantidad = 0
    for curso in cursos.values():
        if int(curso["Costo"]) > valor:
            cantidad += 1
            imprimir_curso(curso)
    print("=============================================================")
    print(f"\nCantidad de cursos con costo mayor a {valor}: {cantidad}")
    print("=============================================================\n\n")

def modificar_curso(cursos : dict) -> None:
    for curso in cursos.values():
        imprimir_curso(curso)
    print("\n\n")
    if len(cursos.keys()) == 0:
        print("No hay cursos para eliminar")
    else:
        opcion = input("¿Qué curso desea modificar? : ")
        if cursos.get(opcion, 0) == 0: print("No existe el curso")
        else:
            campo = input("¿Qué campo desea modificar? : ")
            if cursos[opcion].get(campo, 0) == 0: print("No existe el campo")
            else: cursos[opcion][campo] = input("Ingrese nuevo valor: ")

def eliminar_curso(cursos : dict) -> None:
    for curso in cursos.values():
        imprimir_curso(curso)
    print("\n\n")
    if len(cursos.keys()) == 0:
        print("No hay cursos para eliminar")
    else:
        opcion = input("¿Qué curso desea eliminar? : ")
        if cursos.get(opcion, 0) == 0: print("No existe el curso")
        else: del cursos[opcion]

def cargar_curso(cursos : dict) -> None:
    print("\n\nDatos de curso")
    cod_curso = input("Código(id): ")
    cursos[cod_curso] = dict()
    cursos["Codigo"] = cod_curso
    cursos[cod_curso]["Nombre"] = input("Nombre del curso: ")
    cursos[cod_curso]["Dias"] = input("Días de curso: ")
    cursos[cod_curso]["Costo"] = input("Costo: ")
    cursos[cod_curso]["Vacantes"] = input("Vacantes: ")
    i = 0
    fechas = list()
    while i < cursos[cod_curso]["Dias"]:
        i += 1
        fecha = input(f"Ingrese fecha {i} (formato dd/mm): ")
        fechas.append(fecha)
    cursos[cod_curso]["Fechas"] = fechas


def opciones_curso(cursos : dict) -> None:
    print('''
    1-Alta
    2-Baja
    3-Modificacion
    ''')
    opcion = input("Opción: ")
    if opcion == "1": cargar_curso(cursos)
    elif opcion == "2": eliminar_curso(cursos)
    elif opcion == "3": modificar_curso(cursos)

def main():
    cursos = dict()
    continuar = True
    while continuar:
        print('''
        a- ABM (Alta - Baja - Modificación) de cursos.
        b- Listar cursos cuyo costo sea superior a 1150 pesos.
        c- Mostrar el o los cursos cuya cantidad de vacantes sea la máxima.
        d- Mostrar todos los cursos que tengan al menos 3 fechas de dictado.
        e- Salir
        ''')
        opcion = input("Opción: ")
        if opcion == "a": opciones_curso(cursos)
        elif opcion == "b": listar_mayor_a_valor(1150, cursos)
        elif opcion == "c": listar_vacantes_max(cursos)
        elif opcion == "d": listar_fechas_dictado_mayor_a(3, cursos)
        elif opcion == "e": continuar = False

main()