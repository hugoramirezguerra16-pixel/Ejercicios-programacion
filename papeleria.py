PRODUCTO1 = input("Nombre del producto 1: ")
precio1 = float(input("Precio por pieza: $"))
cantidad1 = int(input("Cantidad: "))
subtotal1 = precio1 * cantidad1

PRODUCTO2 = input("Nombre del producto 2: ")
precio2 = float(input("Precio por pieza: $"))
cantidad2 = int(input("Cantidad: "))
subtotal2 = precio2 * cantidad2

PRODUCTO3 = input("Nombre del producto 3: ")
precio3 = float(input("Precio por pieza: $"))
cantidad3 = int(input("Cantidad: "))
subtotal3 = precio3 * cantidad3

subtotal_general = subtotal1 + subtotal2 + subtotal3
iva = subtotal_general * 0.16
total = subtotal_general + iva

print("\nCompra Total")
print(f"{PRODUCTO1}: ${subtotal1:.2f}")
print(f"{PRODUCTO2}: ${subtotal2:.2f}")
print(f"{PRODUCTO3}: ${subtotal3:.2f}")
print(f"Subtotal: ${subtotal_general:.2f}")
print(f"IVA (16%): ${iva:.2f}")
print(f"Total: ${total:.2f}")