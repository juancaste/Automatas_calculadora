def interseccionLenguajes():
    print('HAS ESCOGIDO INTERSECCION DE LENGUAJES!')
    x=int(input('Ingrese numero de palabras lenguaje 1: '))
    y=int(input('Ingrese numero de palabras lenguaje 2: '))
    lenguaje=set()
    lenguaje2 = set()

    for i in range(0,x):
        cadena=input('Ingrese palabra lenguaje 1: ')
        lenguaje.add(cadena)

    for i in range(0, y):
        cadena1 = input('Ingrese palabra lenguaje 2: ')
        lenguaje2.add(cadena1)

    interseccion=lenguaje.intersection(lenguaje2)
            
    print('Interseccion(L1 ∩ L2): ',interseccion)
    input('Enter para continuar...')