def calculadora_basica():
    print("¡Bienvenido a la calculadora básica!")
    print("Opciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    try:
        opcion = int(input("Elige una operación (1-4): "))
        if opcion not in [1, 2, 3, 4]:
            print("Por favor, elige una opción válida.")
            return

        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == 1:
            resultado = num1 + num2
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == 2:
            resultado = num1 - num2
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == 3:
            resultado = num1 * num2
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == 4:
            if num2 == 0:
                print("No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"El resultado de la división es: {resultado}")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

# Ejecutar la calculadora básica
calculadora_basica()
