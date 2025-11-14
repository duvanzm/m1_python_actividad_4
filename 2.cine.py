# 2. Cine — Clasificar películas según duración

# Instrucciones
# Preguntar cuántas películas hay
# Ingresar la duración de cada una

# Clasificación
# < 100 min → “Corta”
# 100–150 min → “Media”
# 150 min → “Larga”

# Guardar y mostrar lista con etiquetas.

while True:

   try:
        list_movies = []
        print("-----------------------------")
        print("")
        num_movies = int(input("Cuantas peliculas hay: "))

        if num_movies <= 0:
            print("Ingrese un numero positivo")
            print("-----------------------------")
        else:
            for i in range(num_movies):
                time_movie = int(input(f"Ingresar la duración de la pelicula {i + 1}: "))
                if time_movie < 100:
                    classification = "corta"
                elif time_movie <= 150:
                    classification = "media"
                else: 
                    classification = "larga"
                list_movies.append({
                "time": time_movie,
                "classification" : classification 
                })
        print("")
        print("Clasificacion: ")
        for s in list_movies:
            print("-----------------------------")
            print(f"{s["time"]} ===> {s["classification"]}")
            
   except:
    print("***ERROR DATO INVALIDO***")
    print("Vuelve a intentarlo")