import os 
import random


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def verificarNumero(nVer, nMax, numeros_ingresados):
    '''Esta función comprueba que el usuario ingrese un número válido.
    Parámetros: nVer= número a verificar, nMax= número máximo dentro del rango.
    Retorna: True si el número a verificar es válido.
    '''
    if not nVer.isnumeric():
        print('ERROR: ha ingresado un carácter incorrecto.')
    elif int(nVer) < 1 or int(nVer) > nMax:
        print('ERROR: ha ingresado un número fuera del rango.')
    elif int(nVer) in numeros_ingresados:
        print('ERROR: ya has ingresado el número', nVer)
    else:
        return True


def pistas(intento, numero_adivinar):
    '''Retorna: pistas para que el usuario pueda adivinar el número.'''
    if intento == 5:
        return f'La suma de todos sus dígitos da como resultado {sum([int(x) for x in str(numero_adivinar)])}'
    elif intento == 4:
        return 'El número es de 2 dígitos.' if len(str(numero_adivinar)) == 2 else 'El número es de 1 dígito.'
    elif intento == 3:
        return f'Su dígito más alto es {max(str(numero_adivinar))}'
    elif intento == 2:
        return 'El número es par.' if numero_adivinar % 2 == 0 else 'El número es impar.'
    else:
        lis_nu = [random.randint(1, 100) for i in range(9)]
        lis_nu.append(numero_adivinar)
        random.shuffle(lis_nu)
        return f'El número está en esta lista: {lis_nu}'


def jugar(rango):
    numero_generado = random.randint(1, rango)
    intentos = 5
    numeros_ingresados = set()

    while intentos > 0:
        print(f'\nADIVINE EL NÚMERO GENERADO ENTRE 1 Y {rango}, TIENE {intentos} INTENTOS.\n')

        print('Pista: ', pistas(intentos, numero_generado))
        
        numero_usuario = input('\nIngrese su predicción: ')
        clearConsole()

        if verificarNumero(numero_usuario, rango, numeros_ingresados) == True:
            if int(numero_usuario) == numero_generado:
                intentos -=1
                print(f'\n¡Felicitaciones! Adivinó el número {numero_generado} correctamente con {5 - intentos} intentos.')
                break
            else:
                print(f'El número no es {numero_usuario}.')
                intentos -=1
                numeros_ingresados.add(int(numero_usuario))

    if intentos == 0: print(f'\n¡Perdiste! El número era {numero_generado}.') 
        

print('''
          +-------------------------------------+
          |          ADIVINA EL NÚMERO          |
          +-------------------------------------+
  
                      INSTRUCCIONES

. La computadora le pedirá que elija la dificultad del juego. 
. Acontinuación generará un número de forma aleatoria y le dará 
una pista para que pueda adivinar el número generado. 
. Cuenta con 5 intentos antes de que se revele el número.
''')
ENTER = input('Presione ENTER para comenzar.')

seguir_jugando = 'S'

while seguir_jugando == 'S':
    clearConsole()
    while True:
        print('''Ingresa el rango del número a adivinar.
        [10] Fácil: 1-10
        [50] Normal: 1-50
        [100] Difícil: 1-100
        ''')
        rango = input()
        if rango == '10' or rango == '50' or rango == '100':
            break
        else:
            clearConsole()
            print('ERROR: has ingresado un número o carácter incorrecto.\n')
    
    clearConsole()
    jugar(int(rango))

    while True:  
        seguir_jugando = input('\n¿Quiere seguir jugando? [S/N] ').upper()
        if seguir_jugando == 'S' or seguir_jugando == 'N':
            break
        else:
            print('\nERROR: ha ingresado un carácter inválido.')