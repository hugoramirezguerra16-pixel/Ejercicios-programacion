edad = int(input("Ingrese la edad del visitante: "))

if edad < 0:
	print("La edad no puede ser negativa.")
else:
	estudiante = input("¿Es estudiante? (sí/no): ").strip().lower()

	if edad  <= 12:
		precio = 40
	elif edad <= 69:
		precio = 100
		if estudiante in ("sí", "si"):
			precio *= 0.75
	else:
		precio = 60

	print(f"El precio final de la entrada es: ${precio:g}")

