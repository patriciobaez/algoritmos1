"""
3) Arsène Lupin, el dueño de la panadería Arsène Lupin Baguettes, está teniendo graves problemas en el cobro de
ventas con sus clientes. Tanto es así, que no le quedó más que hablar con el departamento de Computación de la
Facultad de Ingeniería de la UBA para pedir por favor que alguno de nuestros programadores le confeccione algún
sistema de administración rentable y que cumpla el régimen de buenas prácticas dictado en la clase de Algoritmos y
Programación I.
Sabiendo que la panadería cuenta con un menú limitado, a saber:
 - Baguette Clásica $250
 - Baguette Rellena $350
 - Baguette Vegana $250
 - Baguette con Muzzarella (a la pizza) $500
 - 1 Merlot $300
 - 1 Vin rosé $300
 - 1 Borgoña blanc $550
Se pide un menú que permita:
a. El ingreso de Pedidos por Cliente. En caso de que el Cliente no exista en los registros, deberá darse de alta
según: Nombre y Apellido y DNI.
b. El ingreso del pago de un pedido por parte de un Cliente.
c. Top 5 de las deudas más importantes ordenadas descendentemente por monto. Se deberá imprimir:
[Nombre y Apellido] - [Monto de Deuda]
d. La impresión de un reporte donde indique en cuantos pedidos se encontró cada artículo. Se deberá imprimir
[Nombre del Artículo] - [Cant. Pedidos solicitados].
e. Indicar el % de pedidos superiores a $1000
Es obligatorio utilizar como mínimo una lista y un diccionario. 
"""

# clientes = {DNI: "NOMBRE Y APELLIDO"}
# pedidos = {numero_pedido: [DNI, [articulo, monto]]}

def ingreso_de_pago(clientes: dict, pedidos: dict) -> tuple:
    importe = input("Ingrese el importe de su pago: ")

def ingreso(clientes: dict, pedidos: dict, articulos: dict, numero_pedido: list) -> tuple:
    
    dni = input("Ingrese su DNI: ")
    #TODO: Otra validación factible para diccionarios podría ser
    #      clientes.get(dni, '0') y validar cuando el valor sea 0
    if dni not in clientes.keys():
        nombre_apellido = input("Ingrese su nombre y apellido: ")
        clientes[dni] = nombre_apellido
    
    print("""
        a- Baguette Clásica $250
        b- Baguette Rellena $350
        c- Baguette Vegana $250
        d- Baguette con Muzzarella (a la pizza) $500
        e- 1 Merlot $300
        f- 1 Vin rosé $300
        g- 1 Borgoña blanc $550
    """)
    articulos_pedidos = []
    salir = False
    while salir == False:
        articulo = input("Ingrese la letra correspondiente al articulo que quiere pedir: ")
        articulos_pedidos.append(articulos[articulo])
        if input("Queres pedir otro articulo?(A-SI / B-NO): ") == ("b" or "B"): salir = True

    datos = [dni, articulos_pedidos]
    #TODO: ¿No sería mejor usar el DNI como llave, y que los pedidos 
    #      sean lista de listas como la variable datos pero sin dni, o bien, directamente
    #      almacenar los valores de cada pedido en una lista
    pedidos[numero_pedido[0]] = datos

    # pedido[dni] = 

    numero_pedido[0] += 1

    return clientes, pedidos

def main() -> None:
    numero_pedido = [1]
    articulos = {
         "a": ["Baguette Clásica", 250],
         "b": ["Baguette Rellena", 350],
         "c": ["Baguette Vegana", 250],
         "d": ["Baguette con Muzzarella (a la pizza)", 500],
         "e": ["1 Merlot", 300],
         "f": ["1 Vin rosé", 300],
         "g": ["1 Borgoña blanc", 550]
        }
    clientes = {}
    pedidos = {}

    volver_menu = True
    while volver_menu:
        print("""
        a. El ingreso de Pedidos por Cliente. En caso de que el Cliente no exista en los registros, deberá darse de alta
        según: Nombre y Apellido y DNI.

        b. El ingreso del pago de un pedido por parte de un Cliente.

        c. Top 5 de las deudas más importantes ordenadas descendentemente por monto. Se deberá imprimir:
        [Nombre y Apellido] - [Monto de Deuda]

        d. La impresión de un reporte donde indique en cuantos pedidos se encontró cada artículo. Se deberá imprimir
        [Nombre del Artículo] - [Cant. Pedidos solicitados].

        e. Indicar el % de pedidos superiores a $1000

        """)
        #TODO: Se puede formatear el ingreso del usuario a minúscula o mayúscula
        #      para evitar hacer comparaciones de más
        opcion = input("Ingrese la letra correspondiente: ")
        if opcion == ("a" or "A"):
            #TODO: Ingreso devuelve una tupla, se puede desempaquetar la misma
            #      indicando las variables separadas por coma, que recibirán
            #      los valores
            clientes = ingreso(clientes, pedidos, articulos, numero_pedido)
            clientes = datos[0]
            pedidos = datos[1]
            print(datos)

        elif opcion == ("b" or "B"):
            datos = ingreso_de_pago(clientes, pedidos)
            clientes = datos[0]
            pedidos = datos[1]
        elif opcion == ("c" or "C"):
            pass
        elif opcion == ("d" or "D"):
            pass
        elif opcion == ("e" or "E"):
            pass
        
        #TODO: Por BPP, el input no debería ir en el condicional, debe guardar el ingreso en una
        #      variable
        #TODO: Si ingreso la 'B', sigo en el menú

        if input("Queres volver al menu?(A-SI / B-NO): ") == ("b" or "B"): volver_menu = False

main()