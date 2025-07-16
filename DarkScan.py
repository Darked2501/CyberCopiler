import subprocess
import OsTools
import socket
def DarkScan():
    print('DarkScan Menu')
    print('1. Scan Network')
    while True:
        command = input('> ')
        if command == 'exit':
            print('Saliendo del programa...')
        elif command == '1':
            print('Scanning local network...')
            activos = ScanNetwork("192.168.1.0/24")
            print("Active Hosts:")
            for ip in activos:
                OsTools.green(ip)
                hostname = obtener_hostname(ip)
                print(f"{ip} → {hostname if hostname else 'Sin nombre'}")

        else:
            print('Comando no reconocido, escribe "help" para ver las herramientas disponibles.')


def ScanNetwork(network_name):
    try:
        resultado = subprocess.run(
            ["fping", "-a", "-g", network_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        hosts = resultado.stdout.strip().split('\n')
        return hosts
    except FileNotFoundError:
        print("❌ fping no está instalado.")
        return []

def obtener_hostname(ip):
    try:
        nombre, _, _ = socket.gethostbyaddr(ip)
        return nombre
    except socket.herror:
        return None