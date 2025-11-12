# 1. Supermercado “DataMarket” — Registrar productos válidos y total
# Instrucciones

# Preguntar cuántos productos ingresará el usuario
# Por cada producto solicitar:
# nombre
# precio
# ¿está vencido? (sí/no)
# Objetivo

# Guardar solo los NO vencidos
# Sumar su costo total


while True:
    countProduct = int(input("Cuantos productos desea ingresar: "))
    listProduct = []
    nuevoProducto = {}
    constoTotal = 0
    for i in range(countProduct):
        nombre = input("Ingrese nombre del producto: ")
        precio = int(input("Ingrese precio del producto: "))
        vencido = input("El producto esta vencido (s/n): ")
        Objetivo = input("Ingrese Objetivo del producto: ")
        if vencido == "s":
            nuevoProducto = {"nombre":nombre, "precio":precio, "Objetivo": Objetivo}
            constoTotal += precio
            listProduct.append(nuevoProducto)
        else:
            print("")
    print("PRODUCTOS: ")
    for i in listProduct:
        nuevoProducto = i
        for clave, valor in nuevoProducto:
            print(f"{clave} : {valor}")
    print(f"Costo total de los productos: {constoTotal}")



