<<<<<<< HEAD
from Lenguajes.Operaciones.concatenacionLen import concatenacionLenguajes
from Lenguajes.Operaciones.inversaLen import inversaLenguajes
from Lenguajes.Operaciones.potenciaLen import potenciacionLenguajes
from Lenguajes.Operaciones.restaLen import restaLenguajes
from Lenguajes.Operaciones.unionLen import unionLenguajes
from Lenguajes.Operaciones.interseccionLen import interseccionLenguajes
from Lenguajes.Operaciones.clausuraKleeneLen import clausuraKleene
from Lenguajes.Operaciones.clausuraPositivaLen import clausuraPositiva

def  operacionLenguajes():


    salirLenguajes : bool = False
    while(salirLenguajes==False):
        print('HAS ESCOGIDO OPERACIONES DE LENGUAJES! ELIGE LA OPERACION QUE DESEAS HACER:')
        print('1 - UNION')
        print('2 - CONCATENACION')
        print('3 - POTENCIACION')
        print('4 - INVERSA')
        print('5 - INTERSECCION')
        print('6 - RESTA')
        print('7 - CLAUSURA DE KLEENE')
        print('8 - CLAUSURA POSITIVA')
        print('9 - SALIR')

        opcLenguajes = int(input("INTRODUZCA UN OPCION: "))

        if(opcLenguajes==1):
            unionLenguajes()
        if(opcLenguajes==2):
            concatenacionLenguajes()
        if(opcLenguajes==3):
           potenciacionLenguajes()
        if(opcLenguajes==4):
           inversaLenguajes()
        if(opcLenguajes==5):
           interseccionLenguajes()
        if(opcLenguajes==6):
           restaLenguajes()
        if(opcLenguajes==7):
           clausuraKleene() 
        if(opcLenguajes==8):
           clausuraPositiva() 
        if(opcLenguajes==9):
            salirLenguajes = True
=======
from Lenguajes.Operaciones.concatenacionLen import concatenacionLenguajes
from Lenguajes.Operaciones.inversaLen import inversaLenguajes
from Lenguajes.Operaciones.potenciaLen import potenciacionLenguajes
from Lenguajes.Operaciones.restaLen import restaLenguajes
from Lenguajes.Operaciones.unionLen import unionLenguajes
from Lenguajes.Operaciones.interseccionLen import interseccionLenguajes
from Lenguajes.Operaciones.clausuraKleeneLen import clausuraKleene
from Lenguajes.Operaciones.clausuraPositivaLen import clausuraPositiva

def  operacionLenguajes():


    salirLenguajes : bool = False
    while(salirLenguajes==False):
        print('HAS ESCOGIDO OPERACIONES DE LENGUAJES! ELIGE LA OPERACION QUE DESEAS HACER:')
        print('1 - UNION')
        print('2 - CONCATENACION')
        print('3 - POTENCIACION')
        print('4 - INVERSA')
        print('5 - INTERSECCION')
        print('6 - RESTA')
        print('7 - CLAUSURA DE KLEENE')
        print('8 - CLAUSURA POSITIVA')
        print('9 - SALIR')

        opcLenguajes = int(input("INTRODUZCA UN OPCION: "))

        if(opcLenguajes==1):
            unionLenguajes()
        if(opcLenguajes==2):
            concatenacionLenguajes()
        if(opcLenguajes==3):
           potenciacionLenguajes()
        if(opcLenguajes==4):
           inversaLenguajes()
        if(opcLenguajes==5):
           interseccionLenguajes()
        if(opcLenguajes==6):
           restaLenguajes()
        if(opcLenguajes==7):
           clausuraKleene() 
        if(opcLenguajes==8):
           clausuraPositiva() 
        if(opcLenguajes==9):
            salirLenguajes = True
>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
            print('Gracias por utilizar nuestro sistema!')