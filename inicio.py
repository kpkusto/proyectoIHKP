# PROGRAMA IHKP HECHO POR SANTIAGO DELLAPIAZZA. JUNIO 2026 - INSTITUTO TECNOLÓGICO DE INFORMÁTICA (I.T.I.)
import socket
import analizador
import requests

def limpiar_consola():
    print("\n" * 50)

def obtener_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return socket.gethostbyname(socket.gethostname())

def menu_inicio():
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")
    print("                                     ------------Bienvenido al sistema IHKP-----------                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |  1.Mostrar todos los logs                     |                                            ")
    print("                                     |  2.Buscar por tipo                            |                                            ")
    print("                                     |  3.Buscar por IP                              |                                            ")
    print("                                     |  4.Detectar IPs sospechosas                   |                                            ")
    print("                                     |  5.Salir                                      |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     |                                               |                                            ")
    print("                                     -----Desarrollado por Santiago Dellapiazza-------                                            ")
    print("                                                                                                                                  ")
    print("                                                                                                                                  ")

def main():
    ip = obtener_ip()
    print(f"\n  Sistema iniciado. IP Detectada: {ip}\n")
    analizador.registrar_log("INFO", ip, "  Sistema iniciado    ")

    while True:
        try:
            menu_inicio()
            
            opcion = int(input("\n--------> Seleccione una opción (1-5): "))
            
            match opcion:
                case 1:
                    limpiar_consola()
                    print("                                            ")
                    print("======= 1) Mostrar todos los logs ========\n")
                    print("                                            ")
                    logs = analizador.leer_logs()
                    analizador.mostrar_logs(logs)
                    analizador.registrar_log("INFO", ip, "-------> 1) Mostrar todos los logs")

                case 2:
                    limpiar_consola()
                    print("                                     ")
                    print("======= 2) Buscar por tipo ========\n")
                    print("                                     ")
                    tipo = input("---------> Ingrese el tipo (INFO / WARNING / ERROR): ").strip().upper()
                    logs = analizador.leer_logs()
                    resultado = analizador.buscar_por_tipo(logs, tipo)
                    analizador.registrar_log("INFO", ip, f"----------> 2) Buscar por tipo {tipo}")
                    if not resultado:
                        print(f"\n---------> No se encontraron logs de tipo {tipo}.")
                    else:
                        print(f"\n---------> Logs de tipo {tipo}: {len(resultado)} encontrados")
                        analizador.mostrar_logs(resultado)

                case 3:
                    limpiar_consola()
                    print("                                   ")
                    print("======= 3) Buscar por IP ========\n")
                    print("                                   ")
                    ip_buscar = input("-------->Ingrese la IP a buscar: ").strip()
                    logs = analizador.leer_logs()
                    resultado = analizador.buscar_por_ip(logs, ip_buscar)
                    analizador.registrar_log("INFO", ip, f" -------> 3) Buscar por IP {ip_buscar}")
                    if not resultado:
                        print(f"\n-------> No se encontraron logs para la IP {ip_buscar}.")
                    else:
                        print(f"\n-------->Logs de IP {ip_buscar}: {len(resultado)} encontrados")
                        analizador.mostrar_logs(resultado)

                case 4:
                    limpiar_consola()
                    print("                                               ")
                    print("======== 4) Detectar IPs sospechosas ========\n")
                    print("                                               ")
                    logs = analizador.leer_logs()
                    sospechosas = analizador.detectar_ips_sospechosas(logs)
                    analizador.registrar_log("INFO", ip, "--------> 4) Detectar IPs sospechosas")
                    if not sospechosas:
                        print("\n---------> No se detectaron IPs sospechosas.")
                    else:
                        print(f"\n{'IP':<20} {'<--------EVENTOS SOSPECHOSOS'}")
                        print("-" * 40)
                        for ip_s, cantidad in sospechosas.items():
                            print(f"{ip_s:<20} {cantidad}")

                case 5:
                    limpiar_consola()
                    print("======= 5) Salir del sistema ========\n")
                    analizador.registrar_log("INFO", ip, "  5)Salir")
                    analizador.registrar_log("INFO", ip, "  Sistema cerrado ")
                    print("\n ---------> Cerrando el sistema. Hasta luego.")
                    break

                case _:
                    limpiar_consola()
                    print("========= Opción inválida ==========\n")
                    print(" ------> Opción inválida. Ingrese un número entre 1 y 5.")
                    analizador.registrar_log("WARNING", ip, "Opción inválida seleccionada")

        except ValueError:
            limpiar_consola()
            print("========== Error de entrada =========\n")
            print("------> Error: debe ingresar un número.")
            analizador.registrar_log("ERROR", ip, "Entrada inválida (no numérica)")

        except KeyboardInterrupt:
            limpiar_consola()
            print("==========: Interrupción del usuario ==========\n")
            analizador.registrar_log("WARNING", ip, "Programa interrumpido por el usuario")
            print("\n--------> Programa interrumpido por el usuario.")
            break

        except Exception as e:
            limpiar_consola()
            print("=========== Error inesperado ==========\n")
            analizador.registrar_log("ERROR", ip, f"Error inesperado: {e}")
            print(f"--------> Error inesperado: {e}")

    input("Presione Enter para cerrar...")

main()
