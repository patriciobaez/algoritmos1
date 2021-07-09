'''
Se ingresan las 3 temperaturas de los 5 meses del año y se desea saber cual fue el mes de mayor temperatura promedio.
(Si, se supone que todos los meses tienen 30 días para simplificar el ejercicio)
(Para simplificar supongamos 5 meses del año de 3 días cada uno)
'''

DIAS = 3
MESES = 5

promedio_maximo = -200.0
mes_maximo = 0
for mes in range(1,MESES+1):
    print(f"\n\nMes {mes}.")
    suma = 0
    promedio = 0
    
    for dia in range(1,DIAS+1):
        print(f"\nDia {dia}.")
        temperatura = float(input("\nIngresar temperatura: "))
        suma += temperatura
        promedio = suma/dia

    if promedio > promedio_maximo:
        promedio_maximo = promedio
        mes_maximo = mes

print(f"El mes de mayor temperatura fue el mes {mes_maximo} con {promedio_maximo} grados centigrados.")
