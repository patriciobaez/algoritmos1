NUM_1 = int(input("Ingresar un numero: "))
NUM_2 = int(input("Ingresar otro numero: "))
NUM_3 = int(input("Ingresar otro numero: "))
NUM_4 = int(input("Ingresar otro numero: "))
NUM_5 = int(input("Ingresar otro numero: "))

if NUM_1 > (NUM_2 and NUM_3 and NUM_4 and NUM_5):
    print(NUM_1)
elif NUM_2 > (NUM_1 and NUM_3 and NUM_4 and NUM_5):
    print(NUM_2)
elif NUM_3 > (NUM_1 and NUM_2 and NUM_4 and NUM_5):
    print(NUM_3)
elif NUM_4 > (NUM_1 and NUM_2 and NUM_3 and NUM_5):
    print(NUM_4)
elif NUM_5 > (NUM_1 and NUM_2 and NUM_3 and NUM_4):
    print(NUM_5)

if NUM_1 < (NUM_2 and NUM_3 and NUM_4 and NUM_5):
    print(NUM_1)
elif NUM_2 < (NUM_1 and NUM_3 and NUM_4 and NUM_5):
    print(NUM_2)
elif NUM_3 < (NUM_1 and NUM_2 and NUM_4 and NUM_5):
    print(NUM_3)
elif NUM_4 < (NUM_1 and NUM_2 and NUM_3 and NUM_5):
    print(NUM_4)
elif NUM_5 < (NUM_1 and NUM_2 and NUM_3 and NUM_4):
    print(NUM_5)