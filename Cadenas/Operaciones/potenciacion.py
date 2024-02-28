def potenciaCadenas():
    print('HAS ESCOGIDO POTENCIACION DE CADENAS! ')
    cadena = input('Ingrese palabra (cadena): ')
    x = int(input('Ingrese potencia(i): ')) 
    #x = input('Ingrese potencia(i): ')
    #potencia=cadena*int(x)
    potencia = ' '.join([cadena for _ in range(x)])  
    #print('Potenciacion(' + x + '):',potencia)
    
    print('Potenciación(' + '):', potencia)
    input('Enter para continuar...')


  