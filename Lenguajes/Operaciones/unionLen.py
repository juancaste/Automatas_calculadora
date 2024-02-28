def unionLenguajes():
    print('HAS ESCOGIDO UNION DE LENGUAJES!')
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

    union=lenguaje.union(lenguaje2)
    print('Unión(L1 ∪ L2): ',union)
    input('Enter para continuar...')