def diferenciaSimetricaAlfabetos():
    print('HAS ESCOGIDO DIFERENCIA SIMETRICA DE ALFABETOS! ')
    c1 = set(input('Ingrese alfabeto 1: '))
    c2 = set(input('Ingrese alfabeto 2: '))
    difsim = c1 ^ c2
    #difsim1 = c2 ^ c1 
    print('a ^ b :', difsim)
    #print('b ^ a :', difsim1)
    input('Enter para continuar...')