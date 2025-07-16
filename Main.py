import DarkScan
import OsTools

OsTools.clear_console()
print ('Bienvenido a CyberCopiler')
print ('Este es una compilacion de herramientas de hacking')
print ('Creado por Darked2501')

print ('Si quieres ver las herramientas disponibles, escribe "help"')
print ('Si quieres salir, escribe "exit"')
while True:
    command = input('> ')
    OsTools.clear_console()
    if command == 'help':
        print('Herramientas disponibles:')
        print('1. DarkScan - Escaneo de red')
    elif command == 'exit':
        print('Saliendo del programa...')
        break
    elif command == 'DarkScan':
        print('Iniciando DarkScan...')
        DarkScan.DarkScan()
        OsTools.clear_console()
        print('DarkScan ha finalizado.')
    else:
        print('Comando no reconocido, escribe "help" para ver las herramientas disponibles.')
print('Gracias por usar CyberCopiler. ¡Hasta luego!')