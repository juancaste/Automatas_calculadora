def unionAlfabetos():
    print('HAS ESCOGIDO UNION DE ALFABETOS! ')
    c1=set(input('Ingrese alfabeto 1: '))
    c2=set(input('Ingrese alfabeto 2: '))
    union=c1.union(c2)
    union.remove(' ')
    print('A U B :',union)
    input('Enter para continuar...')