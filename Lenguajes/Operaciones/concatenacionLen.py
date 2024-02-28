<<<<<<< HEAD
def concatenacionLenguajes():
    print('HAS ESCOGIDO CONCATENACION DE LENGUAJES!')

    # Ingresar palabras para el primer lenguaje (L1)
    x = int(input('Ingrese el número de palabras para el primer lenguaje (L1): '))
    lenguaje1 = set()

    for i in range(x):
        palabra = input('Ingrese palabra para el primer lenguaje (L1): ')
        lenguaje1.add(palabra)

    # Ingresar palabras para el segundo lenguaje (L2)
    y = int(input('Ingrese el número de palabras para el segundo lenguaje (L2): '))
    lenguaje2 = set()

    for i in range(y):
        palabra = input('Ingrese palabra para el segundo lenguaje (L2): ')
        lenguaje2.add(palabra)

    # Realizar la concatenación L1 * L2
    concatenacion = set()

    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            concatenacion.add(palabra1 + palabra2)

    print('Concatenación (L1 * L2):', concatenacion)
    input('Presiona Enter para continuar...')

=======
def concatenacionLenguajes():
    print('HAS ESCOGIDO CONCATENACION DE LENGUAJES!')

    # Ingresar palabras para el primer lenguaje (L1)
    x = int(input('Ingrese el número de palabras para el primer lenguaje (L1): '))
    lenguaje1 = set()

    for i in range(x):
        palabra = input('Ingrese palabra para el primer lenguaje (L1): ')
        lenguaje1.add(palabra)

    # Ingresar palabras para el segundo lenguaje (L2)
    y = int(input('Ingrese el número de palabras para el segundo lenguaje (L2): '))
    lenguaje2 = set()

    for i in range(y):
        palabra = input('Ingrese palabra para el segundo lenguaje (L2): ')
        lenguaje2.add(palabra)

    # Realizar la concatenación L1 * L2
    concatenacion = set()

    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            concatenacion.add(palabra1 + palabra2)

    print('Concatenación (L1 * L2):', concatenacion)
    input('Presiona Enter para continuar...')

>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
