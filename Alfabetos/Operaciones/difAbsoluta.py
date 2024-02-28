def diferenciaAbsolutaAlfabetos():
    print('HAS ESCOGIDO DIFERENCIA ABSOLUTA DE ALFABETOS! ')
    c1 = set(input('Ingrese alfabeto 1: '))
    c2 = set(input('Ingrese alfabeto 2: '))
    dif = c1 - c2
    dif1 = c2 - c1
    print('a \ b :', dif)
    print('b \ a :',dif1)
    input('Enter para continuar...')