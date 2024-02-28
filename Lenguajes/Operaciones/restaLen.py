def restaLenguajes():
    print('HAS ESCOGIDO RESTA DE LENGUAJES!')

    # Ingresar palabras para el primer lenguaje
    x = int(input('Ingrese el número de palabras para el primer lenguaje: '))
    lenguaje1 = set()

    for i in range(x):
        palabra = input('Ingrese palabra para el primer lenguaje: ')
        lenguaje1.add(palabra)

    # Ingresar palabras para el segundo lenguaje
    y = int(input('Ingrese el número de palabras para el segundo lenguaje: '))
    lenguaje2 = set()

    for i in range(y):
        palabra = input('Ingrese palabra para el segundo lenguaje: ')
        lenguaje2.add(palabra)

    # Calcular la resta de lenguajes (L1 - L2)
    resta = lenguaje1.difference(lenguaje2)
     # Calcular la resta L2 - L1
    resta1 = lenguaje2.difference(lenguaje1)

    print('Resultado de la resta (L1 - L2):', resta)
    print('Resultado de la resta (L2 - L1):', resta1)
    input('Presiona Enter para continuar...')

