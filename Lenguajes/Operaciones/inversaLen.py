def inversaLenguajes():
    print('HAS ESCOGIDO INVERSA DE LENGUAJES! ')
    x = int(input('Ingrese numero de palabras lenguaje: '))
    lenguaje = set()
    inversa= set()

    for i in range(0, x):
        cadena = input('Ingrese palabra del lenguaje: ')
        lenguaje.add(cadena)
        inversa.add(''.join(reversed(cadena)))

    print('Inversa(LR):',inversa)
    input('Enter para continuar...')

    