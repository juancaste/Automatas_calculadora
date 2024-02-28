
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
                        print("Has seleccionado Pertenencia")
            # Agrega aquí la lógica para la opción de Pertenencia
                    case '2':
                        print("Has seleccionado Union")
            # Agrega aquí la lógica para la opción de Union
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
                print("Has seleccionado Union")
    # Agrega aquí la lógica para la opción de Union
            case '3':
                exit()  # Opción para salir del bucle while
            case _:
                print("Opción inválida")

if __name__ == "__main__":
    menu()