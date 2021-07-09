"""
Hacer un programa que permita el ingreso de los alumnos y las notas correspondiente a 3 cátedras de la materia
 Algoritmos de FIUBA. Para esto sabemos que cada cátedra tiene inscriptos a un número indeterminado a priori de
 alumnos, y que los datos que poseemos de cada alumno son Nombre y Apellido, padrón, nota final
Se pide:
   a- Calcular la nota más alta de cada curso y a qué alumno pertenece (mostrar padrón)
   b- Calcular la nota más baja entre todos los cursos.
   c- Calcular la cátedra cuyo promedio de nota sea el máximo.
   d- Mostar la cantidad total de alumnos de los 3 cursos.
"""


nota_minima_global = 10
contador_alumnos = 0
promedio_maximo = 0
catedra = 0

for i in range(1,4):
    nombre_maximo = ""
    padron_maximo = ""
    nota_maxima = 0
    nota_minima = 10
    numero = 1
    suma = 0
    contador = 0

    while numero != 0:
        contador += 1
        contador_alumnos += 1

        nombre = input("\n\nIngrese nombre y apellido del alumno: ")
        padron = input("\nIngrese el numero del padron del alumno: ")
        nota = int(input("\nIngrese la nota del alumno: "))
        numero = int(input("\nIngrese el numero 0 para terminar el ingreso de alumnos o 1 para continuar: "))

        suma += nota
        promedio = suma/contador

        if nota > nota_maxima:
            nombre_maximo = nombre
            padron_maximo = padron
            nota_maxima = nota
        
        if nota < nota_minima:
            nota_minima = nota

        if nota < nota_minima_global:
            nota_minima_global = nota

        if promedio > promedio_maximo:
            promedio_maximo = promedio
            catedra = i

        print("\n", nombre_maximo, "numero de padron", padron_maximo, "saco la nota mas alta:", nota_maxima, "\n")
     
print(f"La nota mas baja de todas las catedras es {nota_minima_global}.")
print(f"La catedra con mayor promedio de nota es la catedra {catedra}")
print(f"Hay {contador_alumnos} alumnos.")