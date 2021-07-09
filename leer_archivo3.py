
"""
Se tiene un archivo de texto(alumnos.txt) con el siguiente formato:
padron, nombre, apellido
Luego se tiene otro archivo de texto(notas.txt) con el siguiente formato:
padrón, materia, nota
A partir de esa información, deseamos saber lo siguiente:
1. La materia con mayor cantidad de aprobados (nota >= 4).
2. El promedio general de cada materia.
3. Los alumnos con un promedio general mayor a 7.
4. El alumno con el mayor promedio.
"""

#diccionario_alumnos = [padron, nombre, apellido]
#diccionario_notas = [padrón, materia, nota]

def armar_diccionarios() -> tuple:
    with open("alumnos.txt", "r") as archivo_alumnos:
        diccionario_alumnos = dict()
        for linea in archivo_alumnos:
            lista_info_alumno = linea.split(", ")
            lista_info_alumno[2] = lista_info_alumno[2].rstrip()
            diccionario_alumnos[lista_info_alumno[0]] = lista_info_alumno

    with open("notas.txt", "r") as archivo_notas:
        diccionario_notas = dict()
        for linea in archivo_notas:
            lista_info_nota = linea.split(", ")
            lista_info_nota[2] = lista_info_nota[2].rstrip()
            diccionario_notas[lista_info_alumno[0]] = lista_info_nota
    
    return diccionario_alumnos, diccionario_notas

def materia_con_mas_aprobados(diccionario_notas: dict) -> None:
    materias = dict()
    
    for valor in diccionario_notas.values():
        if int(valor[2]) >= 4:
            if valor[1] not in materias:
                materias[valor[1]] = 1
            else:
                materias[valor[1]] += 1

    #print(materias)
    
    print(f"La materia con mayor cantidad de aprobados es: {max(materias, key=materias.get)}.")
            
def promedio_general_materia(diccionario_notas: dict) -> None:
    materias = dict()
    
    for valor in diccionario_notas.values():
        
        if valor[1] not in materias:
            materias[valor[1]] = [int(valor[2]), 1]
        else:
            materias[valor[1]][0] += int(valor[2])
            materias[valor[1]][1] += 1
    
    for valor in diccionario_notas.values():
        materias[valor[1]] = materias[valor[1]][0] / materias[valor[1]][1]
    
    print(materias)

def promedio_general_mayor7(diccionario_notas: dict) -> None:
    alumnos = dict()
    
    for valor in diccionario_notas.values():
        
        if valor[0] not in alumnos:
            alumnos[valor[0]] = [int(valor[2]), 1]
        else:
            alumnos[valor[0]][0] += int(valor[2])
            alumnos[valor[0]][1] += 1
    
    for valor in diccionario_notas.values():
        alumnos[valor[0]] = alumnos[valor[0]][0] / alumnos[valor[0]][1]
        if alumnos[valor[0]] <= 7:
            del alumnos[valor[0]]

    print(alumnos)

def alumno_mayor_promedio(diccionario_notas: dict) -> None:
    alumnos = dict()
    
    for valor in diccionario_notas.values():
        
        if valor[0] not in alumnos:
            alumnos[valor[0]] = [int(valor[2]), 1]
        else:
            alumnos[valor[0]][0] += int(valor[2])
            alumnos[valor[0]][1] += 1
    
    for valor in diccionario_notas.values():
        alumnos[valor[0]] = alumnos[valor[0]][0] / alumnos[valor[0]][1]
    
    print(f"El alumno con el mayor promedio es: {max(alumnos, key=alumnos.get)}.")

def main() -> None:
    diccionario_alumnos, diccionario_notas = armar_diccionarios()
    print(diccionario_alumnos)
    print(diccionario_notas)
    materia_con_mas_aprobados(diccionario_notas)
    promedio_general_materia(diccionario_notas)
    promedio_general_mayor7(diccionario_notas)
    alumno_mayor_promedio(diccionario_notas)

main()