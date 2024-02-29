
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
                            
                            print('HAS ESCOGIDO PERTENENCIA DE ALFABETOS ! \n')
                            
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
                            print("Has seleccionado Union")
                            c1=set(input('Ingrese alfabeto 1: '))
                            c2=set(input('Ingrese alfabeto 2: '))
                            union=c1.union(c2)
                            union.remove()
                            print('A U B :',union)
                            input('Enter para continuar...')
                                                    

                        case '3':
                            print("Has seleccionado la opción INTERSECCIÓN")
                            
                        case '4':
                            print("Has seleccionado la opción Complemento")
                            
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
                            
            
                        case '2':
                            print("HAS ESCOGIDO PERTENENCIA DE CONCATENACIÓN")
            
                        case '3':
                            print("HAS ESCOGIDO PERTENENCIA DE POTENCIACIÓN")
                            
                        case '4':
                            print("HAS ESCOGIDO PERTENENCIA DE INVERSA")                       
                                        
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
                            
            
                        case '2':
                            print("HAS ESCOGIDO PERTENENCIA DE POTENCIA")
    
                        case '3':
                            print("HAS ESCOGIDO PERTENENCIA DE INVERSA")
                            
                        case '4':
                            print("HAS ESCOGIDO PERTENENCIA DE UNIÓN")
                            
                        case '5':
                            print("HAS ESCOGIDO PERTENENCIA DE INTERSECCIÓN")   
                        
                        case '6':
                            print("HAS ESCOGIDO PERTENENCIA DE RESTA")    
                        
                        case '7':
                            print("HAS ESCOGIDO PERTENENCIA DE CLAUSULA DE KLEENE")
                                
                        case '8':
                            print("HAS ESCOGIDO PERTENENCIA DE CLAUSULA POSITIVA")
                                    
                                        
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