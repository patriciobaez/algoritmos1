"""
Yamila, la cosmetóloga furor en redes, tiene un consultorio donde realiza limpiezas y tratamientos para el cuidado
de la piel.
Debido a la alta demanda de sus pacientes y futuros pacientes, nos pidió que realicemos un programa que la ayude
con la planificación de su negocio. La información del paciente que Yami necesita analizar es la cantidad de consultas
asistidas y que tratamientos fueron realizados.

Asimismo, el catálogo de tratamientos que comercializa es el siguiente:
 - Higiene profunda $1500
 - Tratamiento Acné $1500
 - Tratamiento tensor con aparatología $1800
 - Tratamiento revitalizante $3000

Hacer un programa que:
 a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:
 - DNI
 - Nombre y Apellido
 - Cantidad de consultas asistidas
 - Tratamientos realizados (Tipo y cantidad. Puede ser ninguno.)
 b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.
 c) Emita un reporte que informe el monto total de tratamientos vendidos.
 d) Emita un reporte que informe el total de pacientes nuevos y viejos.
 e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.
A tener en cuenta: Se considera que un paciente es *nuevo* en caso de que el mismo haya asistido únicamente a 1
consulta con el profesional.
"""





def tratamiento_mas_solicitado(clientes: dict):
    higiene_profunda = 0
    tratamiento_acne = 0
    tratamiento_tensor_con_aparatología = 0
    tratamiento_revitalizante = 0

    for keys in clientes.keys():
        higiene_profunda += clientes[keys][2][0]
        tratamiento_acne += clientes[keys][2][1]
        tratamiento_tensor_con_aparatología += clientes[keys][2][2]
        tratamiento_revitalizante += clientes[keys][2][3]

    tratamiento_maximo = max(higiene_profunda, tratamiento_acne, tratamiento_tensor_con_aparatología, tratamiento_revitalizante)

    if tratamiento_maximo == higiene_profunda:
        tratamiento_mas_solicitado = "Higiene profunda"
    elif tratamiento_maximo == tratamiento_acne:
        tratamiento_mas_solicitado = "Tratamiento Acne"
    elif tratamiento_maximo == tratamiento_tensor_con_aparatología:
        tratamiento_mas_solicitado = "Tratamiento tensor"
    elif tratamiento_maximo == tratamiento_revitalizante:
        tratamiento_mas_solicitado = "Tratamiento revitalizante"

    print(f"El tratamiento más solicitado por los pacientes es: {tratamiento_mas_solicitado}")

def ingreso_tratamiento(tratamientos):
    otro_tratamiento = True
    while otro_tratamiento == True:
        print("A-Higiene profunda $1500\nB-Tratamiento Acné $1500")
        print("C-Tratamiento revitalizante $3000\nD-Tratamiento tensor con aparatología $1800")
        tratamiento = input("Seleccione el tratamiento a realizar: ")
        if tratamiento == ("a" or "A"):
            tratamientos[0] += 1
        elif tratamiento == ("b" or "B"):
            tratamientos[1] += 1
        elif tratamiento == ("c" or "C"):
            tratamientos[2] += 1
        elif tratamiento == ("d" or "D"):
            tratamientos[3] += 1

        opcion = input("Quiere realizar otro tratamiento(A-si / B-no): ")
        if opcion == ("a" or "A"):
            otro_tratamiento = True
        else: otro_tratamiento = False


def ingreso_datos(clientes: dict) -> dict:
    dni = int(input("Ingrese su DNI: "))
    if dni not in clientes.keys():
        tratamientos = [0, 0, 0, 0]
        cant_consultas = 1
        nombre_completo = input("Ingrese su nombre completo: ")
        tratamientos = ingreso_tratamiento(tratamientos)
        info_cliente = [dni, nombre_completo, tratamientos, cant_consultas]
        clientes[dni] = info_cliente

    else:
        clientes[dni][3] += 1
        tratamientos = clientes[dni][2]
        tratamientos = ingreso_tratamiento(tratamientos)
    
    return clientes


def main() -> None:
    clientes = {}
    volver_menu = True
    while volver_menu:
        print("""
        a) Permita al usuario realizar el ingreso de un paciente. Para ello se solicita:
            - DNI
            - Nombre y Apellido
            - Cantidad de consultas asistidas
            - Tratamientos realizados (Tipo y cantidad. Puede ser ninguno.)
        b) Emita un reporte que informe el tratamiento más solicitado por los pacientes.
        c) Emita un reporte que informe el monto total de tratamientos vendidos.
        d) Emita un reporte que informe el total de pacientes nuevos y viejos.
        e) Emita un reporte que informe cuál es el tratamiento más solicitado por los pacientes nuevos.
        """)
        opcion = input("Ingrese la letra correspondiente: ")
        if opcion == ("a" or "A"):
            clientes = ingreso_datos(clientes)
        elif opcion == ("b" or "B"):
            tratamiento_mas_solicitado(clientes)
        elif opcion == ("c" or "C"):
            pass
        elif opcion == ("d" or "D"):
            pass
        elif opcion == ("e" or "E"):
            pass
        
        if input("Queres volver al menu?(A-SI / B-NO): ") == ("b" or "B"): volver_menu = False




main()
