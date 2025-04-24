import random

def adivinar_numero():
    numero_aleatorio = random.randint(1, 10)
    intentos = 3

    print("Tienes 3 intentos para adivinar un Numero de 1 a 10.")

    while intentos > 0:
        try:
            numero_ingresado = int(input("Ingresa tu número: "))
            if numero_ingresado < 1 or numero_ingresado > 10:
                print("Por favor, ingresa un número valido entre 1 y 10.")
                continue

            if numero_ingresado == numero_aleatorio:
                print("¡Felicidades! Adivinaste el número.")
                break
            elif numero_ingresado < numero_aleatorio:
                print("El número es mayor.")
            else:
                print("El número es menor.")

            intentos -= 1
            if intentos > 0:
                print(f"Te quedan {intentos} intentos.")
            else:
                print(f"No hay mas intentos. El número era {numero_aleatorio}.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Ejecutar el juego
adivinar_numero()