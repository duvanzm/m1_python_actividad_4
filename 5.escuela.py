# 5. Escuela — Registrar notas por estudiante

# Instrucciones
# Preguntar cuántos estudiantes
# Para cada uno, pedir 3 notas (0.0 a 5.0)

# Salida
# Calcular promedio individual
# Mostrar “Aprobado” o “Reprobado”

while True:
    try:
        print("")
        num_students = int(input("Cuántos estudiantes: "))
        print("-------------------------------------------")
        list_grades = []
        if num_students > 0 :
            for i in range(num_students):
                print(f"Notas de estudiante {i+1} ingrese notas (0.0 a 5.0)")
                note1 = float(input("Ingrese la nota 1: "))
                note2 = float(input("Ingrese la nota 2: "))
                note3 = float(input("Ingrese la nota 3: " ))
                if 0 <= note1 <= 5 and 0 <= note2 <= 5 and 0 <= note3 <= 5:
                    average = (note1+note2+note3)/3 
                    score = ""
                    if average >= 3 :
                        score = "Aprobado"
                    else:
                        score = "Reprobado"
                    list_grades.append([
                        i+1,
                        note1,
                        note2,
                        note3,
                        round(average, 1),
                        score
                    ])
                else:
                    print("Los datos deven estar entre (0.0 a 5.0)")
                    print("*********Vuelve a intentar************")
                    break
         
            print("-------------------------------------------")
            for i in list_grades:
                print(f"Estudiante {i[0]} promedio {i[4]} ===> {i[5]}") 
                print("-------------------------------------------")   
        else:
            print("Ingrese un numero Positivo")
    except:
        print("***ERROR DATO INVALIDO***")    
        print("   Vuelve a intentarlo")  

