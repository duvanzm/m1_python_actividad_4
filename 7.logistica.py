# 7. Logística — Contar tipos de paquetes

# Instrucciones
# Ingresar cantidad de paquetes
# Por cada uno escoger tipo:
# normal
# express
# urgente

# Objetivo
# Contar cuántos hay de cada tipo

while True:
    try:
        num_packs = int(input("Ingresar cantidad de paquetes: ")) 
        list_packs = []
        if num_packs > 0 :
        
            for i in range(num_packs):
                print("Opciones:")
                print("1. normal")
                print("2. express")
                print("3. urgente")
                print(f"Escojer un tipo para el paquete {i+1}")
                option = int(input("Ingrese una opcion (1, 2, 3): "))
                if option == 1:
                    list_packs.append("normal")
                elif option == 2 :
                    list_packs.append("express")
                elif option == 3 :
                    list_packs.append("urgente")
                else:
                    print("Dato invalido")
                    print("Vuelve a intentar")
            for i in list_packs:
                if i == i[1] :
                    print("")
                    print("REPETICIONES: ")
                    print("----------------------------------")
                    print(f"El paquete tipo: {i}")
                    print(f"Se repite  {list_packs.count(i)} veses")
                    print("----------------------------------")
                else:
                    print("No hay generos que se repitan")
        else:
            print("El numero deve ser positivo")
            print("Vuelve a intentar")
    except:
        print("***ERROR DATO INVALIDO***")    
        print("   Vuelve a intentarlo")  
