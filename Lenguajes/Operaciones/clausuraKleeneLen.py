<<<<<<< HEAD

def clausuraKleene():
    print('HAS ESCOGIDO CLAUSURA DE KLEENE DE LENGUAJES!')
    lenguaje = set()
    kleene = set()
    x = int(input('Ingrese número de palabras del lenguaje: '))
    y = int(input('Ingrese limite: '))
    for i in range(0, x):
        cadena = input('Ingrese palabra del lenguaje: ')
        lenguaje.add(cadena)
        kleene.add(cadena)
        

    for i in lenguaje:
        for j in lenguaje:
            kleene.add(i + j)
            kleene.add((i + j) * y)

    kleene1 = ['@', *kleene, '...',]
    sorted(kleene1, key=str, reverse=True)
    print('Clausura de Kleene(L*): ', kleene1)
    input('Enter para continuar...')
    

    
=======

def clausuraKleene():
    print('HAS ESCOGIDO CLAUSURA DE KLEENE DE LENGUAJES!')
    lenguaje = set()
    kleene = set()
    x = int(input('Ingrese número de palabras del lenguaje: '))
    y = int(input('Ingrese limite: '))
    for i in range(0, x):
        cadena = input('Ingrese palabra del lenguaje: ')
        lenguaje.add(cadena)
        kleene.add(cadena)
        

    for i in lenguaje:
        for j in lenguaje:
            kleene.add(i + j)
            kleene.add((i + j) * y)

    kleene1 = ['@', *kleene, '...',]
    sorted(kleene1, key=str, reverse=True)
    print('Clausura de Kleene(L*): ', kleene1)
    input('Enter para continuar...')
    

    
>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
