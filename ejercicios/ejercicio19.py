"""
2)Nos contratan de una empresa textil fabricante de hilado y telas de algodón para la creación de un simple software
que permita la carga de pedidos.
El sistema deberá permitir la carga de un nuevo pedido o la modificación de un pedido ya existente, como así
también la carga de un nuevo stock, o la modificación de uno existente.


Para el stock de sus productos la empresa cuenta con esta información: Número de Artículo, Descripción, color,
cantidad, precio
Para tomar un pedido la empresa necesita esta información: Nro de cuenta, Razón Social, artículos, color, cantidades
pedidas, total valorizado del pedido.

Ejemplo de datos:
Para el stock
271, rebb 100% algodón peinado, Crudo, 1500kg, 825$/Kg
271, rebb 100% algodón peinado, Negro, 150kg, 980$/Kg
271, rebb 100% algodón peinado, Azul Marino, 500kg, 980$/Kg
271, rebb 100% algodón peinado, Blanco, 100kg, 825$/Kg
433, jersey 100% algodón peinado, Rosa, 300kg, 788$/Kg
433, jersey 100% algodón peinado, Blanco, 30kg, 788$/Kg
…
El sistema debe tener:
Un pequeño menú que permita :
a- La carga o modificación de un pedido (Un pedido puede estar compuesto por más de un artículo)
b- La carga o modificación de un stock existente
c- Listar los pedidos de un nro de cuenta o Razón Social dada
d- Mostrar el pedido cuya valorización sea la mayor
e- Listar todos los pedidos cargados.
"""





def main() -> None:

    articulos = {}
    cliente = {}
    pedido = {}

    volver_menu = True
    while volver_menu:
        print("""
        a- La carga o modificación de un pedido (Un pedido puede estar compuesto por más de un artículo).
        b- La carga o modificación de un stock existente.
        c- Listar los pedidos de un nro de cuenta o Razón Social dada.
        d- Mostrar el pedido cuya valorización sea la mayor.
        e- Listar todos los pedidos cargados.
        """)
        opcion = input("Ingrese la letra correspondiente: ")
        if opcion == ("a" or "A"):
            pass
        elif opcion == ("b" or "B"):
            pass
        elif opcion == ("c" or "C"):
            pass
        elif opcion == ("d" or "D"):
            pass
        elif opcion == ("e" or "E"):
            pass
        
        if input("Queres volver al menu?(A-SI / B-NO): ") == ("b" or "B"): volver_menu = False

main()