def complementoAlfabetos():
    print('HAS ESCOGIDO COMPLEMENTOS DE ALFABETOS! ')
    c1=set(input ('Ingrese alfabeto a: '))
    c2=set(input('Ingrese alfabeto b: '))
    complemento=c1-c2
    print('Complemento de b:',complemento)
    input('Enter para continuar...')