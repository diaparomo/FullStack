def calcular_propina():
    try:
        monto_cuenta = float(input("Introduce el monto total de la cuenta: "))
        if monto_cuenta < 0:
            print("El monto de la cuenta no puede ser negativo.")
            return

        porcentaje_propina = float(input("Introduce el porcentaje de propina que deseas dejar (por ejemplo, 10, 15, 20): "))
        if porcentaje_propina < 0:
            print("El porcentaje de propina no puede ser negativo.")
            return

        monto_propina = monto_cuenta * (porcentaje_propina / 100)
        total_pagar = monto_cuenta + monto_propina

        print(f"El monto de la propina es: ${monto_propina:.2f}")
        print(f"El total a pagar (cuenta + propina) es: ${total_pagar:.2f}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

# Ejecutar la función para calcular la propina
calcular_propina()