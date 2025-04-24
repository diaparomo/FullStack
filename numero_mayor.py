primero = input("Ingresa Primer Numero:\t")
#print("Tu Primer Numero es: "+primero)

segundo = input("Ingresa Segundo Numero:\t")
#print("Tu Segundo Numero es: "+segundo)


tercero = input("Ingresa Tercer Numero:\t")
#print("Tu Tercer Numero es: "+tercero)

if primero > segundo and primero > tercero:
    print("El numero "+primero+" es el numero mayor")
elif segundo > primero and segundo > tercero:
    print("El numero "+segundo+" es el numero mayor")
elif tercero > primero and tercero > segundo:
    print("El numero "+tercero+" es el numero mayor")
elif primero == segundo and primero== tercero:
    print("Los numeros son Iguales")
