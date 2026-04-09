print("\nCAJA DE KIOSCO")

total = 0
ahorro = 0


nombre = input("Ingresar nombre del cliente: ")
while True:
    cantidad = input("\nIngresar cantidad de productos a comprar: ")
    if not cantidad.isdigit() or int(cantidad) <= 0  or cantidad == "0":
        print("\n***Debe ingresar un numero mayor a cero '0'")
    else:
        break

cantidad = int(cantidad)

while not str(cantidad).isdigit() or cantidad <= 0:
    print("\n*** La cantidad debe ser digitos mayores a cero '0'")
    cantidad = input("\nIngresar cantidad de productos a comprar: ")

for producto in range (int(cantidad)):
    print(f"\nProducto {producto + 1 }")
    while True:
        precio = input("- Precio: ")
        if precio.isdigit():
            precio = float(precio)
            total += precio
            break
        else:
            print("\n*** Debe ingesar un numero")
    while True:
        descuento = input("- Descuento (S/N): ").lower()
        if descuento == "s":
            ahorro += (precio * 0.10)
            print("\n- Se aplico el descuento")
            break
        elif descuento == "n":
            print("\n- No se aplico el descuento")
            break
        else:
            print("\n*** Debe ingesar 's' o 'n'")

prom = (total - ahorro) / cantidad
print(f"Total sin descuentos: $ {total}")
print(f"Total con descuentos: $ {total - ahorro}")
print(f"Ahorro: $ {ahorro}")
print(f"Promedio por producto: $ {prom:.2f}")
print("\nFin del programa.")
