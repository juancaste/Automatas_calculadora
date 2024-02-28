<<<<<<< HEAD
def pertenciaAlfabetos():
    print('HAS ESCOGIDO PERTENENCIA DE ALFABETOS! ')
    c1 = set(input('Ingrese alfabeto 1: '))
    c2 = set(input('Ingrese alfabeto 2: '))
    pertenencia = c2.issubset(c1)
    pertenencia1 = c1.issubset(c2)
    if (pertenencia == True):
        sorted(c1,key=str)
        sorted(c2, key=str)
        print('a = ', c1)
        print('b = ', c2)
        print('b ∈ a')
        input('Enter para continuar...')

    elif (pertenencia1 == True):
        print('a: ', c1)
        print('b: ', c2)
        print('a ∈ b')
        input('Enter para continuar...')

    else:
        print('a ∉ b y b ∉ a')
        input('Enter para continuar...')
        
        
        
=======
def pertenciaAlfabetos():
    print('HAS ESCOGIDO PERTENENCIA DE ALFABETOS! ')
    c1 = set(input('Ingrese alfabeto 1: '))
    c2 = set(input('Ingrese alfabeto 2: '))
    pertenencia = c2.issubset(c1)
    pertenencia1 = c1.issubset(c2)
    if (pertenencia == True):
        sorted(c1,key=str)
        sorted(c2, key=str)
        print('a = ', c1)
        print('b = ', c2)
        print('b ∈ a')
        input('Enter para continuar...')

    elif (pertenencia1 == True):
        print('a: ', c1)
        print('b: ', c2)
        print('a ∈ b')
        input('Enter para continuar...')

    else:
        print('a ∉ b y b ∉ a')
        input('Enter para continuar...')
        
        
        
>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
    