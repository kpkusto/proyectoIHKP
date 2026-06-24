
import os
import datetime

ARCHIVO_LOGS = os.path.join(os.path.dirname(__file__), "logs.txt")

def registrar_log(tipo, ip, descripcion):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d")
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    linea = f"{fecha},{hora},{tipo},{ip},{descripcion}\n"
    with open(ARCHIVO_LOGS, "a") as archivo:
        archivo.write(linea)
        archivo.flush()  # asegura escritura inmediata

def leer_logs():
    logs = []
    if not os.path.exists(ARCHIVO_LOGS):
        return logs
    with open(ARCHIVO_LOGS, "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 5:
                log = {
                    "fecha": partes[0],
                    "hora": partes[1],
                    "tipo": partes[2],
                    "ip": partes[3],
                    "descripcion": partes[4]
                }
                logs.append(log)
    return logs

def mostrar_logs(logs):
    if not logs:
        print("No hay logs para mostrar.")
        return
    print(f"\n{'FECHA':<12} {'HORA':<10} {'TIPO':<8} {'IP':<15} {'DESCRIPCIÓN'}")
    print("-" * 60)
    for log in logs:
        print(f"{log['fecha']:<12} {log['hora']:<10} {log['tipo']:<8} {log['ip']:<15} {log['descripcion']}")

def buscar_por_tipo(logs, tipo):
    return [log for log in logs if log["tipo"] == tipo]

def buscar_por_ip(logs, ip):
    return [log for log in logs if log["ip"] == ip]

def detectar_ips_sospechosas(logs, umbral=2):
    conteo = {}
    for log in logs:
        if log["tipo"] == "ERROR":
            conteo[log["ip"]] = conteo.get(log["ip"], 0) + 1
    return {ip: cant for ip, cant in conteo.items() if cant >= umbral}

