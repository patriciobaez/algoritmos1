"""
Escriba una función que dada una lista de denominaciones de billetes de la moneda corriente de un país, permita descomponer un
importe otorgado por el usuario en las cantidades correspondientes a cada una de las denominaciones cual si fuera un cajero
automático y suponiendo que siempre elige otorgar billetes del mayor valor posible. La función debe controlar que el importe
sea factible de ser descompuesto y devolver un diccionario con la descomposición.  Construya el programa principal donde utiliza 
dicha función.
  Ej: Lista = [10,20,50,100,200,500,1000]  Valor = 1690  Diccionario = {10:0,20:2,50:1;100:1;200:0;500:1;1000:1}
"""


def ingresar_billetes(denominaciones) -> int:
    ingreso = True
    while ingreso:
        billete = int(input("Ingrese una denominacion de billete: "))
        if billete <= 0:
            ingreso = False
        else:
            denominaciones.append(billete)

    importe = int(input("Ingrese el importe: "))
    while importe < min(denominaciones):
        importe = int(input("El importe debe ser mayor a la menor denominacion: "))
    
    return importe


def main() -> None:
    denominaciones = []
    d ={}
    importe = ingresar_billetes(denominaciones)
    denominaciones.sort(reverse = True)
    for billete in denominaciones:
        d[billete] = importe // billete
        importe = importe % billete
    print(d)

main()