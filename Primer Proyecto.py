
def menu():
    while True:
        print("Menú")
        print("1. ALFABETOS")
        print("2. CADENAS")
        print("3. LENGUAJES")
        print("4. SALIR")

        opcion = input("Selecciona una opción: ")

        match opcion:
            case '1':
                while True:    
                    print("Has seleccionado ALFABETOS")
    
                    print("Menú")
                    print("1. PERTENENCIA")
                    print("2. UNIÓN")
                    print("3. INTERSECCIÓN")
                    print("4. COMPLEMENTO")
                    print("5. DIFERENCIA ABSOLUTA")
                    print("6. DIFERENCIA SIMETRICA")
                    print("0. VOLVER AL MENÚ ANTERIOR")
                    print("\n")
                    opcion = input("Selecciona una opción: ")

                    match opcion:
                        case '1':
                            
                            print('HAS ESCOGIDO PERTENENCIA DE ALFABETOS! \n')
                            
                            c1 = set(input("Ingrese el conjunto de alfabetos A (Separados por coma):  "))
                            c2 = set(input("Ingrese el conjunto de alfabetos B (Separados por coma):  "))
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
            
                        case '2':
                            print('HAS ESCOGIDO UNION DE ALFABETOS! ')
                            c1=set(input('Ingrese alfabeto 1: '))
                            c2=set(input('Ingrese alfabeto 2: '))
                            union=c1.union(c2)
                            union.remove('')
                            print('A U B :',union)
                            input('Enter para continuar...')        

                        case '3':
                            print("Has seleccionado la opción INTERSECCIÓN")
                            c1=set(input('Ingrese alfabeto 1: '))
                            c2=set(input('Ingrese alfabeto 2: '))
                            interseccion=c1.intersection(c2)
                            interseccion.remove(' ')
                            print('A ∩ B :',interseccion)
                            input('Enter para continuar...')
                            
                        case '4':
                            print("Has seleccionado la opción Complemento")
                            c1=set(input ('Ingrese alfabeto a: '))
                            c2=set(input('Ingrese alfabeto b: '))
                            complemento=c1-c2
                            print('Complemento de b:',complemento)
                            input('Enter para continuar...')
                            
                        case '5':
                            print("\n")                        
                            print("Has seleccionado la opción DIFERENCIA ABSOLUTA\n\n")
                            
                            dato1 = set(input("Ingrese el conjunto de alfabetos A (Separados por coma):  "))
                            dato2 = set(input("Ingrese el conjunto de alfabetos B (Separados por coma):  "))
                            print("\n")
                            dato1.discard(',')
                            dato2.discard(',')
                            
                            difAbs = dato1 - dato2
                            print("La diferencia absoluta es: A \ B = ", sorted(difAbs))
                            input("\n Pulsa una tecla para continuar")
                            
                            
                        case '6':
                            print("Has seleccionado la opción DIFERENCIA SIMETRICA\n")    
                            c1 = set(input('Ingrese alfabeto 1: '))
                            c2 = set(input('Ingrese alfabeto 2: '))
                            difsim = c1 ^ c2
                            #difsim1 = c2 ^ c1 
                            print('a ^ b :', difsim)
                            #print('b ^ a :', difsim1)
                            input('Enter para continuar...')
                            
                
                        case '0':
                            exit()  # Opción para salir del bucle while
                        case _:
                            print("Opción inválida")
                            
                
                
                
                
                
                
                
                
                
                
                
            case '2':
                
                
                while True:    
                    print("Has seleccionado CADENAS")
    
                    print("Menú")
                    print("1. LONGITUD")
                    print("2. CONCATENACIÓN")
                    print("3. POTENCIACIÓN")
                    print("4. INVERSA")
                    print("0. VOLVER AL MENÚ ANTERIOR")
                    print("\n")
                    opcion = input("Selecciona una opción: ")

                    match opcion:
                        case '1':
                            
                            print('HAS ESCOGIDO PERTENENCIA DE LONGITUD! \n')
                            cadena=input('Ingrese cadena: ')
                            longitud=len(cadena)
                            print('Longitud: ',longitud)
                            input('Enter para continuar...')
            
                        case '2':
                            print("HAS ESCOGIDO PERTENENCIA DE CONCATENACIÓN")
                            cadena=input('Ingrese palabra 1 (cadena): ')
                            cadena2 = input('Ingrese palabra 2 (cadena): ')
                            conca=cadena+cadena2
                            print('Concatenación:',conca)
                            input('Enter para continuar...')
            
                        case '3':
                            print("HAS ESCOGIDO PERTENENCIA DE POTENCIACIÓN")
                            cadena = input('Ingrese palabra (cadena): ')
                            x = int(input('Ingrese potencia(i): ')) 
                            #x = input('Ingrese potencia(i): ')
                            #potencia=cadena*int(x)
                            potencia = ' '.join([cadena for _ in range(x)])  
                            #print('Potenciacion(' + x + '):',potencia)
                            
                            print('Potenciación(' + '):', potencia)
                            input('Enter para continuar...')

                            
                        case '4':
                            print("HAS ESCOGIDO PERTENENCIA DE INVERSA")   
                            cadena = input('Ingrese cadena: ')
                            inversa=''.join(reversed(cadena))
                            print('Inversa←:', inversa)
                            input('Enter para continuar...')                    
                                        
                        case '0':
                            exit()  # Opción para salir del bucle while
                        case _:
                            print("Opción inválida")
    
    
    
    
    
            case '3':
                while True:    
                    print("Has seleccionado LENGUAJES")
    
                    print("Menú")
                    print("1. CONCATENACIÓN")
                    print("2. POTENCIA")
                    print("3. INVERSA")
                    print("4. UNIÓN")
                    print("5. INTERSECCIÓN")
                    print("6. RESTA")
                    print("7. CLAUSULA DE KLEENE")
                    print("8. CLAUSULA POSITIVA")
                    print("0. VOLVER AL MENÚ ANTERIOR")
                    print("\n")
                    opcion = input("Selecciona una opción: ")

                    match opcion:
                        case '1':
                            
                            print('HAS ESCOGIDO PERTENENCIA DE CONCATENACIÓN! \n')
                            
                            # Ingresar palabras para el primer lenguaje (L1)
                            x = int(input('Ingrese el número de palabras para el primer lenguaje (L1): '))
                            lenguaje1 = set()

                            for i in range(x):
                                palabra = input('Ingrese palabra para el primer lenguaje (L1): ')
                                lenguaje1.add(palabra)

                            # Ingresar palabras para el segundo lenguaje (L2)
                            y = int(input('Ingrese el número de palabras para el segundo lenguaje (L2): '))
                            lenguaje2 = set()

                            for i in range(y):
                                palabra = input('Ingrese palabra para el segundo lenguaje (L2): ')
                                lenguaje2.add(palabra)

                            # Realizar la concatenación L1 * L2
                            concatenacion = set()

                            for palabra1 in lenguaje1:
                                for palabra2 in lenguaje2:
                                    concatenacion.add(palabra1 + palabra2)

                            print('Concatenación (L1 * L2):', concatenacion)
                            input('Presiona Enter para continuar...')
                            
                            
            
                        case '2':
                            print("HAS ESCOGIDO PERTENENCIA DE POTENCIA")
                            # Solicitar al usuario que ingrese palabras separadas por comas y sin espacios
                            entrada = input('Ingrese palabras (lenguaje) separadas por comas: ')
                            palabras = entrada.split(',')
                            
                            i = int(input('Ingrese la potencia (i): '))
                            
                            # Verificamos que i sea un número no negativo
                            if i < 0:
                                print("La potencia debe ser un número no negativo.")
                                return
                            
                            # Función recursiva para calcular la potencia i-ésima
                            def calcular_potencia(palabras, i):
                                if i == 0:
                                    return {""}  # La potencia 0 es el lenguaje vacío
                                else:
                                    potencia_anterior = calcular_potencia(palabras, i - 1)
                                    nueva_potencia = set()
                                    for palabra_existente in potencia_anterior:
                                        for palabra in palabras:
                                            nueva_potencia.add(palabra_existente + palabra)
                                    return nueva_potencia
                            
                            potencia = calcular_potencia(palabras, i)
                            i_str = str(i)
                            
                            print('Potencia(' + i_str + '):',potencia)
                            input('Presiona Enter para continuar...')
                            
    
                        case '3':
                            print("HAS ESCOGIDO PERTENENCIA DE INVERSA")
                            x = int(input('Ingrese numero de palabras lenguaje: '))
                            lenguaje = set()
                            inversa= set()

                            for i in range(0, x):
                                cadena = input('Ingrese palabra del lenguaje: ')
                                lenguaje.add(cadena)
                                inversa.add(''.join(reversed(cadena)))

                            print('Inversa(LR):',inversa)
                            input('Enter para continuar...')
                                                    
                        case '4':
                            print("HAS ESCOGIDO PERTENENCIA DE UNIÓN")
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
                            
                        case '5':
                            print("HAS ESCOGIDO PERTENENCIA DE INTERSECCIÓN")   
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
                        
                        case '6':
                            print("HAS ESCOGIDO PERTENENCIA DE RESTA")   
                            # Ingresar palabras para el primer lenguaje
                            x = int(input('Ingrese el número de palabras para el primer lenguaje: '))
                            lenguaje1 = set()

                            for i in range(x):
                                palabra = input('Ingrese palabra para el primer lenguaje: ')
                                lenguaje1.add(palabra)

                            # Ingresar palabras para el segundo lenguaje
                            y = int(input('Ingrese el número de palabras para el segundo lenguaje: '))
                            lenguaje2 = set()

                            for i in range(y):
                                palabra = input('Ingrese palabra para el segundo lenguaje: ')
                                lenguaje2.add(palabra)

                            # Calcular la resta de lenguajes (L1 - L2)
                            resta = lenguaje1.difference(lenguaje2)
                            # Calcular la resta L2 - L1
                            resta1 = lenguaje2.difference(lenguaje1)

                            print('Resultado de la resta (L1 - L2):', resta)
                            print('Resultado de la resta (L2 - L1):', resta1)
                            input('Presiona Enter para continuar...')
 
                        
                        case '7':
                            print("HAS ESCOGIDO PERTENENCIA DE CLAUSULA DE KLEENE")
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
                                
                        case '8':
                            print("HAS ESCOGIDO PERTENENCIA DE CLAUSULA POSITIVA")
                            positiva=set()
                            lenguaje = set()
                            x = int(input('Ingrese número de palabras del lenguaje 1: '))
                            y = int(input('Ingrese limite: '))

                            for i in range(0, x):
                                cadena = input('Ingrese palabra del lenguaje: ')
                                lenguaje.add(cadena)
                                positiva.add(cadena)
                                positiva.add(cadena * y)

                            for i in lenguaje:
                                for j in lenguaje:
                                    positiva.add(i+j)
                                    positiva.add((i + j)*y)

                            positiva1={*positiva, "..."}
                            # print(positiva1)
                            sorted(positiva, key=str)
                            print('Clausura Positiva(L+):',positiva1)
                            input('Enter para continuar...')
                                        
                        case '0':
                            exit()  # Opción para salir del bucle while
                        case _:
                            print("Opción inválida")
                
                
            case '4':   
                exit()  # Opción para salir del bucle while
            case _:
                print("Opción inválida")

if __name__ == "__main__":
    menu()