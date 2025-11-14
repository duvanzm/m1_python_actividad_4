# 6. Taller — Registrar reparaciones y calcular costo

# Instrucciones
# Preguntar cuántos vehículos
# Por cada uno pedir:
# horas de trabajo
# piezas cambiadas

# Reglas
# valor hora = $20.000
# valor pieza = $50.000
# Si horas > 10 o piezas > 4 → “Compleja”
# Mostrar costo por vehículo + complejidad. 

while True:
    try:
        print("")
        num_cars = int(input("Cuantos vehiculos va a ingresar: ")) 
        print("-------------------------------------------")
        list_cars = []

        if num_cars > 0:
            for i in range(num_cars):
                print(f"Vehiculo {i+1}")
                car = i+1
                hour_work = int(input("Ingrese horas de trabajo: "))
                num_parts = int(input("Ingrese numero de piezas cambiadas: "))
                if hour_work > 0 and num_parts > 0 :
                    total_price = (hour_work * 20000) + (num_parts * 50000)
                    difficulty = ""
                    if hour_work > 10 or num_parts > 4 :
                        difficulty = "Compleja"
                    else:
                        difficulty = "Normal"    
                    list_cars.append([
                        car,
                        hour_work,
                        num_parts,
                        total_price,
                        difficulty
                    ])
                else:
                    print("-------------------------------------------")
                    print("Los datos deben ser positivos")
                    print("vuelve a intentar")
                    break
            print("-------------------------------------------")
            for i in list_cars:
                print("-------------------------------------------")
                print(f"Vehiculo {i[0]}")
                print(f"Costo Total: {i[3]}")
                print(f"Dificultad: {i[4]}")

        else:
            print("El numero deve ser positivo")
            print("Vuelve a intentar")
    except:
        print("***ERROR DATO INVALIDO***")    
        print("   Vuelve a intentarlo")  
