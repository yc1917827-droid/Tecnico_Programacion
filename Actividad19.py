print("-------------------------------------")
print("Bienvenidos al programa S&S")

opcion = 0

while opcion != 3:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Datos")
    print("2. Operaciones")
    print("3. Salir")

    opcion = int(input("Digita tu opción: "))

    # OPCIÓN 1
    if opcion == 1:
        nombre = input("Ingrese su nombre: ")
        edad1 = input("Ingrese su edad: ")
        edad2 = input("Ingrese la edad de su amigo: ")

        print("\n--- DATOS INGRESADOS ---")
        print("Su nombre es:", nombre)
        print("Su edad es:", edad1)
        print("La edad de su amigo es:", edad2)

        input("Presione ENTER para volver al menú...")

    # OPCIÓN 2 
    elif opcion == 2:
        num1 = input("Ingrese un número: ")
        num2 = input("Ingrese otro número: ")

        if num1 >= "0" and num1 <= "9" and num2 >= "0" and num2 <= "9":
            num1 = int(num1)
            num2 = int(num2)

            print("La suma es:", num1 + num2)
            print("La multiplicación es:", num1 * num2)
        else:
            print("Error: solo se permiten números")

        input("Presione ENTER para volver al menú...")

    # OPCIÓN 3
    elif opcion == 3:
        print("Saliendo del programa...S&S\nJojo S<3")

    else:
        print("Opción inválida")

print("Fin del programa...S:)")