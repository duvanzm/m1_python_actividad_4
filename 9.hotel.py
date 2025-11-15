# 9. Hotel — Registrar habitaciones ocupadas

# Instrucciones
# Pedir cantidad de habitaciones
# Por cada una:
# número de habitación
# ocupada? (sí/no)

# Salida
# Lista de habitaciones libres
# Conteo de ocupadas vs libres

while True:
    try:
        print("")
        num_rooms = int(input("Ingresar cantidad de habitaciones: "))
        list_rooms = []
        num_free = 0
        num_busy = 0
        if num_rooms > 0:
            for i in range(num_rooms):
                print(f"Dato: {i+1} ")
                num_room = input("Numero de habitacion: ")
                busy = input("Esta ocupada s/n: ")
                if busy == "s" or busy == "n":
                    list_rooms.append([
                    num_room,
                    busy
                    ])
                else:
                    print("***********************")
                    print("Error Dato invalido")
                    print("Vuelve a intentar")
                    print("***********************")
                    break
            print("")
            print("-----------------------------")
            print("Habitaciones Libres: ")
            print("----------------------------")
            for i in list_rooms:
                if i[1] == "s":
                    num_free = num_free +1
                else:
                    num_busy = num_busy +1
                if i[1] == "s":
                    print("--------------------")
                    print(f"habitacion: {i[0]} ===> libre")
                    print("--------------------")
            print("ocupadas vs libres: ")
            print(f"        {num_busy} vs {num_free}")

        else:
            print("Ingrese numeros positivos")
    except:
        print("***********************")
        print("***ERROR DATO INVALIDO***")    
        print("   Vuelve a intentarlo")  
        print("***********************")