"""
MANEJO DE LISTAS

    Cadenas de caracteres (strings) 


    Para invertir una lista lista podemos escribir
    lis.reverse()

    pero también se invierte escribiendo
    lis = lis[::-1] 

    https://docs.python.org/3/library/stdtypes.html

    Por ejemplo el método .capitalize() cambia la primera letra por una mayúscula.

    - Seguramente, más interesante es el método .count() al que le pasamos un carácter
    o una secuencia de caracteres y nos devuelve cuántas veces la encontró en el
    string.

    - El método .find() nos indica en qué posición comienza una serie de caracteres que
    le indicamos por parámetro. Si no la encuentra devuelve –1.

    Con el método .append() vamos agregando elementos a la lista.

    Tuplas y Listas

        En Python una tupla y una lista son estructuras muy similares. Ambas asemejan lo que
        en Pascal sería un registro y lo que en C o Java sería una estructura. La diferencia entre
        una tupla y una lista es que la primera no puede modificar los datos que tiene y la
        segunda sí. 

        La diferencia al definir una tupla y una lista es que la primera se define con paréntesis y
        la segunda con corchetes. 




    Si quisiéramos tener la lista ordenada, lo podemos hacer de dos maneras
    distintas:

        1. Utilizando la función sorted que no modifica a la lista original, sino que devuelve
        una nueva lista ordenada.
        Usando sorted
        notas_ordenadas = sorted(notas)

        2. Usando el método sort que sí modifica la lista original y no devuelve nada.
        Usando sort
        notas.sort()

        Tanto sorted como sort ordenan, por defecto, de menor a mayor. Para ordenarlo de
        mayor a menor se puede ingresar un nuevo parámetro: reverse = True.
        notas.sort(reverse = True)

     Agregar elementos:
        o Vimos que con append agrega al final.
        o Con insert agrega el valor en la posición que le indiquemos.
        Ejemplo:
        notas.insert(2, 8) # inserta un 8 en la posición 2

     Quitar elementos:
        o Con el método clear quita todos los elementos y deja la lista vacía.
        o Con remove quita un valor de la lista. Por ejemplo remove(3) quitaría una
        nota 3. Si hay más de una solo quita la primera. Si no hay ninguna da
        error, por eso este método debe usarse luego del método count. Si hay
        cantidad positiva, entonces se puede remover, de lo contrario, no.
        o Con pop quita el elemento que esté en la posición indicada. Por ejemplo
        pop(2) quitaría el elemento que está en la posición 2. Si no le pasamos
        ningún parámetro, por defecto quita el último elemento de la lista. 

    Otros métodos
        - copy. Copia la lista en otra.
        - index. Devuelve la posición en la que está cierto elemento. Si hay más de uno
        devuelve la primera. Si no hay ninguno da error, por eso se aconseja usar en
        conjunto con count.
        - reverse. Invierte la lista. 

    notas_1 = [5, 4, 9, 7]
    notas_2 = [2, 2, 4] # el segundo docente es más exigente!

    Si queremos unir las dos listas debemos usar el método extend.
    notas_1.extend(notas_2)
    print(notas_1)

    La salida será:
    [5, 4, 9, 7, 2, 2, 4] 

    ¿Qué hubiera pasado si usábamos append?
    notas_1.append(notas_2)
    print(notas_1)

    Al ver la salida vemos lo siguiente:
    [5, 4, 9, 7, [2, 2, 4]]

    Lo que hizo fue agregar toda la segunda lista como un solo elemento, en lugar de agregar
    3 elementos más, agregó 1 solo. Hay que tener cuidado cuando se usan estos métodos
    que pueden prestar a confusión. 

    Recorriendo una lista 

    for nota in notas:
    print(nota) 

    split

    s = "hola que tal"
    l = s.split() 

    queda: ['hola', 'que', 'tal'] 

    s = "hola,que,tal"
    l = s.split(',') 

    queda: ['hola', 'que', 'tal'] 

    Si queremos volver a armar un string con esta lista podríamos hacer lo siguiente:
    s2 = ""
    for letra in l:
    s2 = s2 + letra

    Armamos un string vacío, recorremos la lista y le vamos agregando con el + cada letra.
    El nuevo string queda con las letras de “camino” ordenadas en forma alfabética:
    acimno

    Hay otra forma de unir una lista en un string, usando el método join (unir). Para hacer
    lo mismo que antes con este método escribimos:
    s2 = "".join(l) 



    Matrices 

    ¿Cómo representamos esa matriz en Python?
    Sería una lista con tres listas, cada una con 5 elementos.

    ventas = [ [10, 15, 8, 12, 24], 
                [2, 5, 3, 4, 6],
                [20, 18, 9, 22, 35] ]

    Es importante notar la diferencia entre estas tres impresiones:
    print(ventas) # imprime toda la matriz
    print(ventas[0]) # imprime la primera fila
    print(ventas[2][3]) # imprime el valor de la fila 3 columna 4

    La salida de cada una es:
    [[10, 15, 8, 12, 24], [2, 5, 3, 4, 6], [20, 18, 9, 22, 35]]
    [10, 15, 8, 12, 24]
    22

    Si queremos obtener el total de ventas del segundo artículo, simplemente hacemos:

    print(sum(ventas[1]))

    En cambio, para saber la cantidad de productos que se vendieron el día jueves:

    total_jueves = 0
    for articulo in ventas:
    total_jueves += articulo[3] 
    print("total vendido el dia jueves: ", total_jueves)
    La salida será:
    total vendido el dia jueves: 38 


    Tablas (vectores de registros) 

    Esto lo podemos representar, como dijimos, con una lista de listas:
    empleados = [ [123, "Pérez Juan", 18000],
    [87, "González Rosa", 22000],
    [145, "Campos Silvia", 20000] ]

    La estructura es similar a la de una matriz con la diferencia de que cada fila representa
    los datos de un empleado.
    A los datos de un registro (una fila) los llamamos “campos”. En este ejemplo tendríamos
    el campo “legajo” que es la primera posición, el campo “nombre”, la segunda, y el campo
    “sueldo”, la tercera. 
    ¿Cómo ordenar según los distintos campos?
    Si la lista la ordenamos usando sorted o sort la ordenará por defecto sobre el primer
    campo, en este caso por legajo.

    empleados.sort()
    for empleado in empleados:
    print(empleado)
    
    La salida quedará:
    [87, 'González Rosa', 22000]
    [123, 'Pérez Juan', 18000]
    [145, 'Campos Silvia', 20000]

    Para ordenar por otros campos necesitamos usar funciones lambda. 


    Funciones lambda 

    ¿Cómo utilizar estas funciones lambda para ordenar listas? 
    En el ejemplo de la lista de empleados, si quisiéramos ordenarla por algún otro campo,
    por ejemplo, por orden apellido, deberíamos indicarle que ordene por el segundo
    campo, es decir por el campo que está en la columna 1.

    empleados.sort(key = lambda x: x[1])

    Con el método sort le indicamos que ordene, pero en key le decimos que lo haga por la
    columna 1. La x representaría uno de los registros, podríamos haber utilizado cualquier
    nombre.

    La impresión quedará:

    [145, 'Campos Silvia', 20000]
    [87, 'González Rosa', 22000]
    [123, 'Perez Juan', 18000]

    Y si quisiéramos ordenarlo por sueldo, de mayor a menor:

    empleados.sort(key = lambda reg: reg[2], reverse = True)
    for empleado in empleados:
    print(empleado)

    La salida será:

    [87, 'González Rosa', 22000]
    [145, 'Campos Silvia', 20000]
    [123, 'Perez Juan', 18000] 




Diccionarios

    La estructura anterior podríamos guardarla en un diccionario. Un diccionario será como
    una lista de registros, con la diferencia de que uno de los campos actuará como clave.
    ¿Qué es una clave?
    Una clave es un campo o más que determinan de forma unívoca a un registro. Por
    ejemplo, en los datos de un empleado la clave sería el legajo, ya que los nombres se
    pueden repetir y los sueldos también.
    Si los mismos datos los pusiéramos en un diccionario, el campo legajo sería la clave y el
    nombre y el sueldo serían los campos que están asociados a dicha clave.
    Pero empecemos con un ejemplo más sencillo: legajo – nombre (sin el sueldo). 

    empleados = { 123 : "Perez Juan",
    87 : "González Rosa",
    145 : "Campos Silvia" } 

    Un diccionario se define con llaves en lugar de corchetes como una lista. Se coloca el
    valor de la clave, dos puntos, y el valor asociado a dicha clave. 
    Si quisiéramos ir llenando el diccionario a medida que se ingresan los datos por teclado,
    podríamos hacer una función cargar de esta forma.



    Iterar diccionarios:
        .
        .
        .
        .

    Hacer list(d.keys()) en un diccionario devuelve una lista de todas las claves usadas en el diccionario, en un orden
    arbitrario (si las querés ordenadas, usá en cambio sorted(d.keys()).
    6 Para controlar si una clave está en el diccionario,
    usá el in.

    El constructor dict() crea un diccionario directamente desde secuencias de pares clave-valor:
    >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    {'sape': 4139, 'jack': 4098, 'guido': 4127}

    Además, las comprensiones de diccionarios se pueden usar para crear diccionarios desde expresiones arbitrarias de clave y
    valor:
    >>> {x: x ** 2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}

    Cuando las claves son cadenas simples, a veces resulta más fácil especificar los pares usando argumentos por palabra
    clave:
    >>> dict(sape=4139, guido=4127, jack=4098)
    {'sape': 4139, 'jack': 4098, 'guido': 4127}


    .update() metohd(returns None):
        The update() method updates the dictionary with the elements from the another dictionary object or from an
        iterable of key/value pairs.
        update() method adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the
        dictionary, it updates the key with the new value.

        Example:
            d = {1: "one", 2: "three"}
            d1 = {2: "two"}

            # updates the value of key 2
            d.update(d1)
            print(d)

            d1 = {3: "three"}

            # adds element with key 3
            d.update(d1)
            print(d)

            >>>{1: 'one', 2: 'two'}
            >>>{1: 'one', 2: 'two', 3: 'three'}

        Example 2(when tuple is passed as parameter):
            d = {'x': 2}

            d.update(y = 3, z = 0)
            print(d)

            >>>{'x': 2, 'y': 3, 'z': 0}

    Para eliminar elementos del diccionario usar del o .pop()










MANEJO DE ARCHIVOS

archivo.read(5)             lee los primeros 5 caracteres

archivo.read()              lee el resto del archivo

archivo.read()              devuelve ''. porque no queda nada del archivo

archivo.seek(0)             vuelve al inicio del archivo

archivo.readlines()         

archivo.seek(0, 2)         va al final del archivo

archivo.write("texto ejemplo")         escribe algo donde este el cursor

archivo.write("\ntexto ejemplo")         el \n hace 


for linea in archivo:
    print(linea, end='')              devuelve todas las lineas del 
                                      archivo una abajo de la otra


archivo.close()             cierra el archivo




"""
