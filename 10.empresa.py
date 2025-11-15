# 10. Empresa — Evaluación según ventas ingresadas

# Instrucciones
# Preguntar cuántos empleados
# Por cada uno:
# nombre
# ventas del mes (ingresar 3 números)

# Regla
# promedio ≥ 6 → “Excelente”
# 3–5.9 → “Bien”
# < 3 → “Bajo rendimiento”
# Mostrar nombre + calificación.

while True:
     try:
        print("")
        print("----------------------------")
        num_staffs= int(input("Ingresar numero de empleados: "))
        list_staffs = []
      
        if num_staffs > 0:
            for i in range(num_staffs):
                name = input("Ingrese el nombre: ")
                sale1 = int(input("Numero de ventas 1: "))
                sale2 = int(input("Numero de ventas 2: "))
                sale3 = int(input("Numero de ventas 3: "))
                if sale1 > 0 and sale2 > 0 and sale3 > 0:
                    mean_sales = (sale1 + sale2 + sale3)/3
                    classification = ""
                    if  mean_sales >= 6:
                        classification = "Excelente"
                    elif  3 <= mean_sales <= 5.9 :
                        classification = "Bien"
                    else:
                        classification = "Bajo rendimiento"
                    list_staffs.append({
                        "name": name,
                        "sales":[sale1,sale2,sale3],
                        "mean_sales": mean_sales,
                        "classification": classification
                        })
                else:
                   print("")
                   print("----------------------------") 
                   print("Ingrese numeros positivos")
                   break  
            for i in list_staffs:
                 print("")
                 print("Estadisticas: ")
                 print("----------------------------") 
                 print(f"{i["name"]} ====> {i["classification"]}")
                 print("----------------------------") 
        else:
            print("")
            print("----------------------------")         
            print("Ingrese numeros positivos")
            print("   Vuelve a intentarlo")
            print("----------------------------")     
           
     except:
         print("***********************")
         print("***ERROR DATO INVALIDO***")    
         print("   Vuelve a intentarlo")  
         print("***********************")
