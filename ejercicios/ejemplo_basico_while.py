gatos = 1
print(gatos)
seguir = input("Queres agreguar otro gato? :")
while seguir == "si" or "Si" or "SI" or "sI":
    gatos += 1
    print(gatos)
    seguir = input("Queres agreguar otro gato? :")
print("Quedaron", gatos, "gatos.")