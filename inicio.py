def menu_inicio():
    print("                                                          ")
    print("                                                          ")
    print("         ------------Bienvenido al sistema IHKP-----------")
    print("         |                                               |")
    print("         |  1.Ingrese a la opcion 1                      |")
    print("         |                                               |")
    print("         |  2.Ingrese a la opcion 2                      |")
    print("         |                                               |")
    print("         |  3.Ingrese a la opcion 3                      |")
    print("         |                                               |")
    print("         |  4.Salir                                      |")
    print("         |                                               |")
    print("         -----Desarrollado por Santiago Dellapiazza-------")
    print("                                                          ")
    print("                                                          ")

while True:
    menu_inicio()
    opcion = int(input("          Seleccione una opcion ( 1-4 )   "))
    match opcion:
        case 1:
            print("Ingreso a la opcion 1")
        case 2:
            print("Ingreso a la opcion 2")
        case 3:
            print("Ingreso a la opcion 3")
        case 4:
            print("             Saliendo del programa...")
            break
        case _:
            print(" Opcion invalida. Intente nuevamente.")

print("hola")