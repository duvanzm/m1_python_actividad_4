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
    try :
        print("******************************************************")
        countProduct = int(input("Cuantos productos desea ingresar: "))
        listProduct = []
        constoTotal = 0
        for i in range(countProduct):
            print("**************************************************")
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))
            vencido = input("El producto esta vencido (si/no): ")
            Objetivo = input("Ingrese Objetivo del producto: ")
            print("**************************************************")
            if vencido.lower() == "no":
                nuevoProducto = {"nombre":nombre, "precio":precio, "Objetivo": Objetivo}
                constoTotal += precio
                listProduct.append(nuevoProducto)

        print("")
        print(f"Costo total de los productos: {constoTotal}")
    except:
        print("****Error dato invalido****")
        print("****Volver a intentar****")


