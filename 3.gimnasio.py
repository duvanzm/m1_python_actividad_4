# 3. Gimnasio “ProFit” — Registrar asistencia semanal
# Instrucciones

# El usuario ingresa cuántas semanas quiere registrar
# Por cada semana: ingresar cuántos días entrenó
# Reglas de puntos

# ≥ 5 días → +10 puntos
# 3–4 días → +5 puntos
# < 3 días → +2 puntos
# Mostrar total de puntos acumulados.
while True:

    try:
        list_week = []
        print("*******************************")
        print("")
        num_weeks = int(input("ingrese el numero de semanas: "))
        total_points = 0
        if num_weeks > 0:
            for i in range(num_weeks):
                num_days = int(input(f"Ingrese los dias entrenados en la semana {i +1}: "))
                if num_days > 0:
                    if num_days >= 5:
                        points = 10
                    elif 3 <= num_days <= 4:
                        points = 5
                    elif num_days < 3:
                        points = 2
                    else:
                        points = 0
                    total_points += points
                    list_week.append({
                        "week": i +1,
                        "day": int(num_days),
                        "points": int(points)
                    })
                else:
                    print("Ingrese numeros positivos")
                    break
            print("*******************************")
            print("")
            print("Estadisticas: ")
            print("-----------------------------")
            for x in list_week:
                
                print(f"Semana: {x["week"]}")
                print(f"Dias: {x["day"]}")
                print(f"Puntos: {x["points"]}")
                print("-----------------------------")
            print(f"Total de puntos: {total_points}")
            print("")
        else:
            print("Ingrese numeros positivos")
    except:
        print("***ERROR DATO INVALIDO***")
        print("    VUELVE A INTENTAR")
