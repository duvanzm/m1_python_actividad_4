# 8. Facturación — Calcular totales con descuento

# Instrucciones:
# Pedir cuántas facturas ingresará el usuario
# Para cada una:
# cliente
# valor
# tipo (normal o premium)

# Descuentos:
# normal → 5%
# premium → 10%
# Calcular total de todas las facturas.

while True:
    try:

        num_check = int(input("Cuantas facturas ingresara: "))
        list_check = []
        all_total = 0
        if num_check > 0:
            for i in range(num_check):
                client = input("Cliente: ")
                value = int(input("Valor: "))
                kind = input("Ingrese (normal o premiun): ")
                discount = 0.0
                total = 0
                if kind == "normal" :
                    discount = 0.95
                elif kind == "premiun" :
                    discount = 0.90
                else:
                    print("Error ")
                    print("Ingrese normal o premiun")
                total = value * discount
                list_check.append([
                    client,
                    value,
                    kind,
                    discount,
                    total
                ])
                
                all_total += total
            print("")
            print("---------------------------------------------------")
            print(f"El precio total de todas las facturas: {all_total}")


        else:
            print("Ingrese numeros positivos")

    except:
        print("***ERROR DATO INVALIDO***")    
        print("   Vuelve a intentarlo")  
