from Cadenas.Operaciones.longitud import longitudCadenas
from Cadenas.Operaciones.concatenacion import concatenacionCadenas
from Cadenas.Operaciones.potenciacion import potenciaCadenas
from Cadenas.Operaciones.inversa import inversaCadenas

def  operacionCadenas():
    salirCadenas : bool = False
    while(salirCadenas==False):
        print('HAS ESCOGIDO OPERACIONES DE CADENAS! ELIGE LA OPERACION QUE DESEAS HACER:')
        print('1 - LONGITUD')
        print('2 - CONCATENACION')
        print('3 - POTENCIACION')
        print('4 - INVERSA')
        print('5 - SALIR')

        opcCadenas = int(input("INTRODUZCA UN OPCION: "))

        if(opcCadenas==1):
            longitudCadenas()
        if(opcCadenas==2):
            concatenacionCadenas()
        if(opcCadenas==3):
            potenciaCadenas()
        if(opcCadenas==4):
            inversaCadenas()
        if(opcCadenas==5):
            salirCadenas=True
            print('Gracias por utilizar nuestro sistema!')