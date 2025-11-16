# 4. Playlist — Detectar géneros repetidos

# Instrucciones
# Preguntar cuántas canciones ingresará
# Ingresar cada género musical

# Objetivo
# Encontrar géneros repetidos sin duplicarlos en la salida
while True:
    # try:
        list_genres = []
        print("-----------------------------")
        print("")
        
        num_genres = int(input("Cuántos generos ingresará: "))
        if num_genres > 0:
              for i in range(num_genres):
                genres = input(f"Ingrese el genero {i}: ")
                if genres not in list_genres:
                     list_genres.append(genres)
                     
              for i in list_genres:
                 print(i)      
        else:
            print("No es numero positivo")
                
       

            
    # except:
    #     print("***ERROR DATO INVALIDO***")
    #     print("    VUELVE A INTENTAR")