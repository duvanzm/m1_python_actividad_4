# 4. Playlist — Detectar géneros repetidos
# Instrucciones

# Preguntar cuántas canciones ingresará
# Ingresar cada género musical
# Objetivo

# Mostrar géneros repetidos sin duplicarlos en la salida
while True:

    list_songs = []
    print("-----------------------------")
    print("")
    try:
        num_songs = int(input("Cuántas canciones ingresará: "))
        if num_songs > 0:

            for i in range(num_songs):
                genre = input(f"Ingrese el genero de la cancion {i+1}: ")
                list_songs.append(genre)
                
        else:
            print("Ingrese numeros positivos")
        
        for i in list_songs:
            if list_songs.count(i) > 1:
                print("")
                print("----------------------------------")
                print(f"El genero {i} se repite {list_songs.count(i)} veses")
                break
            else:
                print("No hay generos que se repitan")
    except:
        print("***ERROR DATO INVALIDO***")
        print("    VUELVE A INTENTAR")