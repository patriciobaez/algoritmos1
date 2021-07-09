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



nombre_maximo = ""
padron_maximo = ""
nota_maxima = 0
nota_minima = 10



numero = 1
while numero != 0:
    suma1 = 0
    contador1 = 0
    contador1 = contador1 + 1

    nombre = input("\n\nIngrese nombre y apellido del alumno: ")
    padron = input("\nIngrese el numero del padron del alumno: ")
    nota = int(input("\nIngrese la nota del alumno: "))
    numero = int(input("\nIngrese el numero 0 para terminar el ingreso de alumnos o 1 para continuar: "))

    suma1 += nota
    promedio1 = suma1/contador1

    if nota > nota_maxima:
        nombre_maximo = nombre
        padron_maximo = padron
        nota_maxima = nota
    
    if nota < nota_minima:
        nota_minima = nota
    
print("\n", nombre_maximo, "numero de padron", padron_maximo, "saco la nota mas alta:", nota_maxima)


nombre_maximo = ""
padron_maximo = ""
nota_maxima = 0
nota_minima = 10
numero = 1
while numero != 0:
    suma2 = 0
    contador2 = 0
    contador2 = contador2 + 1

    nombre = input("\n\nIngrese nombre y apellido del alumno: ")
    padron = input("\nIngrese el numero del padron del alumno: ")
    nota = int(input("\nIngrese la nota del alumno: "))
    numero = int(input("\nIngrese el numero 0 para terminar el ingreso de alumnos o 1 para continuar: "))

    suma2 += nota
    promedio2 = suma2/contador2

    if nota > nota_maxima:
        nombre_maximo = nombre
        padron_maximo = padron
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota
    
print("\n", nombre_maximo, "numero de padron", padron_maximo, "saco la nota mas alta:", nota_maxima)


nombre_maximo = ""
padron_maximo = ""
nota_maxima = 0
nota_minima = 10
numero = 1
while numero != 0:
    suma3 = 0
    contador3 = 0
    contador3 = contador3 + 1

    nombre = input("\n\nIngrese nombre y apellido del alumno: ")
    padron = input("\nIngrese el numero del padron del alumno: ")
    nota = int(input("\nIngrese la nota del alumno: "))
    numero = int(input("\nIngrese el numero 0 para terminar el ingreso de alumnos o 1 para continuar: "))

    suma3 += nota
    promedio3 = suma3/contador3

    if nota > nota_maxima:
        nombre_maximo = nombre
        padron_maximo = padron
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota
    
print("\n", nombre_maximo, "numero de padron", padron_maximo, "saco la nota mas alta:", nota_maxima)

print("\n\n\nLa nota minima entre todos los cursos es:", nota_minima)

if promedio1 > promedio2 and promedio3:
    print("\nEl promedio mas alto lo tuvo la catedra 1")
elif promedio2 > promedio1 and promedio3:
    print("\nEl promedio mas alto lo tuvo la catedra 2")
else:
    print("\nEl promedio mas alto lo tuvo la catedra 3")

print("\nEntre las 3 catedras hay", (contador1+contador2+contador3), "alumnos.")