<<<<<<< HEAD
def clausuraPositiva():
    print('HAS ESCOGIDO CLAUSURA POSITIVA DE LENGUAJES!')
    positiva=set()
    lenguaje = set()
    x = int(input('Ingrese número de palabras del lenguaje 1: '))
    y = int(input('Ingrese limite: '))

    for i in range(0, x):
        cadena = input('Ingrese palabra del lenguaje: ')
        lenguaje.add(cadena)
        positiva.add(cadena)
        positiva.add(cadena * y)

    for i in lenguaje:
        for j in lenguaje:
            positiva.add(i+j)
            positiva.add((i + j)*y)

    positiva1={*positiva, "..."}
    # print(positiva1)
    sorted(positiva, key=str)
    print('Clausura Positiva(L+):',positiva1)
    input('Enter para continuar...')
    
=======
def clausuraPositiva():
    print('HAS ESCOGIDO CLAUSURA POSITIVA DE LENGUAJES!')
    positiva=set()
    lenguaje = set()
    x = int(input('Ingrese número de palabras del lenguaje 1: '))
    y = int(input('Ingrese limite: '))

    for i in range(0, x):
        cadena = input('Ingrese palabra del lenguaje: ')
        lenguaje.add(cadena)
        positiva.add(cadena)
        positiva.add(cadena * y)

    for i in lenguaje:
        for j in lenguaje:
            positiva.add(i+j)
            positiva.add((i + j)*y)

    positiva1={*positiva, "..."}
    # print(positiva1)
    sorted(positiva, key=str)
    print('Clausura Positiva(L+):',positiva1)
    input('Enter para continuar...')
    
>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
