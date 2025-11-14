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
    # try:
        print("")
        num_staffs= int(input("Ingresar numero empleados: "))
        list_staffs = []
      
        if num_staffs > 0:
            for i in range(num_staffs):
              list_staffs.append({
                   "name": input("Ingrese el nombre: "),
                   "sale": 
              })
            
            
        else:
            print("Ingrese numeros positivos")
                
           
    # except:
    #     print("***********************")
    #     print("***ERROR DATO INVALIDO***")    
    #     print("   Vuelve a intentarlo")  
    #     print("***********************")
