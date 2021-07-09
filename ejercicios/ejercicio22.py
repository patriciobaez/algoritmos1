"""
4) Lucho adora las zanahorias. Podría pasar horas contándonos sobre las diferentes variedades de zanahorias, con sus
diferentes sabores, colores, olores, texturas... 
Nos ha contratado para que lo ayudemos a realizar la compra. Luego de investigar, ha reducido su interés a únicamente
dos proveedores de zanahorias: Sus nombres comerciales son “ZANAHORÍN” y “ZANAHORÓN”.
ZANAHORÍN y ZANAHORÓN son los proveedores de máxima calidad, y como la calidad de ambos es indistinguible
(¡Incluso para un experto en zanahorias de la talla de Lucho!), lo importante es comprar al que tenga menor precio de
los dos.
Lucho quiere que lo ayudes con una función llamada zanahorias, que reciba los precios en pesos (por tonelada de
zanahorias) de cada proveedor en UN string, y escriba el nombre del proveedor al cual conviene comprar. Si ambos
venden a igual precio, se debe escribir el texto “DA IGUAL”.
Datos de entrada:
Se reciben en un único string con dos enteros entre 1 y 100000 inclusive, separados por un espacio:
• El primero indica el precio al que vende “ZANAHORÍN”
• El segundo el precio al que vende “ZANAHORÓN”.
Datos de salida:
Se debe escribir una única línea, con la palabra “ZANAHORÓN” o “ZANAHORÍN” (sin las comillas), según quién tenga
mejor precio. Si ambos venden al mismo precio, se debe escribir en una única línea la frase “DA IGUAL” (sin las
comillas). Nota: Toda la salida debe estar en letras mayúsculas, como se ha indicado.
Ejemplo:
 Si la entrada por parámetro fuera: 15223 17250
La salida debería ser: ZANAHORÍN 
"""

precios = "101 909"
def zanahorias(precios):
    lista_de_precios = precios.split()
    if lista_de_precios[0] < lista_de_precios[1]: print("ZANAHORÍN")
    elif lista_de_precios[0] > lista_de_precios[1]: print("ZANAHORÓN")
    else: print("DA IGUAL")

zanahorias(precios)