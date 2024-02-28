def potenciacionLenguajes():
    print('HAS ESCOGIDO POTENCIA DE LENGUAJES!')
    
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

