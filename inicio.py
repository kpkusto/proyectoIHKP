
#PROGRAMA IHKP HECHO POR SANTIAGO DELLAPIAZZA. HECHO EN EL MES DE JUNIO DEL 2026 PARA EL INSTITUTO TECNOLOGICO DE INFORMATICA (I.T.I.)


def menu_inicio():
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("""  
          
                                           /$$$$$$       /$$   /$$         /$$   /$$       /$$$$$$$ 
                                          |_  $$_/      | $$  | $$        | $$  /$$/      | $$__  $$
                                            | $$        | $$  | $$        | $$ /$$/       | $$  \ $$
                                            | $$ /$$$$$$| $$$$$$$$ /$$$$$$| $$$$$/ /$$$$$$| $$$$$$$/
                                            | $$|______/| $$__  $$|______/| $$  $$|______/| $$____/ 
                                            | $$        | $$  | $$        | $$\  $$       | $$      
                                           /$$$$$$      | $$  | $$        | $$ \  $$      | $$      
                                          |______/      |__/  |__/        |__/  \__/      |__/                                                
                                                                                                                                
                                                                                                                                           """)
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                     ------------Bienvenido al sistema IHKP-----------                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |  1.Cargar logs                                |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |  2.Ver estadisticas                           |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |  3.Detectar IPs sospechosas                   |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |  4.Salir                                      |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     -----Desarrollado por Santiago Dellapiazza-------                                            ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")

while True:

    #meter un try + except
    menu_inicio()
    opcion = int(input("          Seleccione una opcion ( 1-4 )   "))
    match opcion:
        case 1:
            print("                 Ingreso a la opcion 1   ")
        case 2:
            print("                 Ingreso a la opcion 2   ")
        case 3:
            print("                 Ingreso a la opcion 3   ")
        case 4:
            print("                  Saliendo del programa...        ")
            break
        case _:
            print("             Opcion invalida. Intente nuevamente.    ")