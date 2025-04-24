def generar_triangulo():
    try:
        filas = int(input("Introduce el número de filas para el triángulo: "))
        if filas <= 0:
            print("Por favor, introduce un número mayor que 0.")
            return


        for i in range(1, filas + 1):
            print("*" * i)
    except ValueError:
        print("Por favor, introduce un número válido.")

# Ejecutar la función para generar el triángulo
generar_triangulo()