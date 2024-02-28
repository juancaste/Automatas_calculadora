def  interseccionAlfabetos():
    print('HAS ESCOGIDO INTERSECCION DE ALFABETOS! ')
    c1=set(input('Ingrese alfabeto 1: '))
    c2=set(input('Ingrese alfabeto 2: '))
    interseccion=c1.intersection(c2)
    interseccion.remove(' ')
    print('A ∩ B :',interseccion)
    input('Enter para continuar...')