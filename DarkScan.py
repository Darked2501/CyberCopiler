import subprocess
import OsTools
def DarkScan():
    print('DarkScan Menu')
    print('1. Scan Network')
    while True:
        command = input('> ')
        if command == 'exit':
            print('Saliendo del programa...')
        elif command == '1':
            print('Name of the network to scan(press N to do it locally):')
            network_name = input('> ')
            if network_name.lower() == 'n':
                print('Scanning local network...')
                activos = ScanNetwork("192.168.1.0/24")
                print("Active Hosts:")
                for ip in activos:
                    OsTools.green(ip)
            elif network_name:
                print(f'Scanning network: {network_name}...')
                # Aquí iría el código para escanear la red especificada
                ScanNetwork(network_name)
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

