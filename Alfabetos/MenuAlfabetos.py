<<<<<<< HEAD

from Alfabetos.Operaciones.complemento import complementoAlfabetos
from Alfabetos.Operaciones.difAbsoluta import diferenciaAbsolutaAlfabetos
from Alfabetos.Operaciones.difSimetrica import diferenciaSimetricaAlfabetos
from Alfabetos.Operaciones.interseccion import interseccionAlfabetos
from Alfabetos.Operaciones.pertenencia import pertenciaAlfabetos
from Alfabetos.Operaciones.union import unionAlfabetos




def operacionAlfabetos():
    salirAlfabetos : bool = False
    while(salirAlfabetos==False):
        print('HAS ESCOGIDO OPERACIONES DE ALFABETOS! ELIGE LA OPERACION QUE DESEAS HACER:')
        print('\n')
        print("1. PERTENENCIA")
        print("2. UNION")
        print("3. INTERSECCION")
        print("4. COMPLEMENTO")   
        print("5. DIFERENCIA ABSOLUTA")          
        print("6. DIFERENCIA SIMETRICA")   
        print("7. SALIR DE ALFABETOS")
        

        opcAlfabetos = int(input("INTRODUZCA UN OPCION: "))

        if(opcAlfabetos==1):

            pertenciaAlfabetos()
        if(opcAlfabetos==2):

           unionAlfabetos()
        if(opcAlfabetos==3):

           interseccionAlfabetos()
        if(opcAlfabetos==4):

           complementoAlfabetos()
        if(opcAlfabetos==5):

           diferenciaAbsolutaAlfabetos()
        if(opcAlfabetos==6):

           diferenciaSimetricaAlfabetos()
        if(opcAlfabetos==7):
            salirAlfabetos=True
            print('Gracias por utilizar nuestro sistema!')
=======

from Alfabetos.Operaciones.complemento import complementoAlfabetos
from Alfabetos.Operaciones.difAbsoluta import diferenciaAbsolutaAlfabetos
from Alfabetos.Operaciones.difSimetrica import diferenciaSimetricaAlfabetos
from Alfabetos.Operaciones.interseccion import interseccionAlfabetos
from Alfabetos.Operaciones.pertenencia import pertenciaAlfabetos
from Alfabetos.Operaciones.union import unionAlfabetos




def operacionAlfabetos():
    salirAlfabetos : bool = False
    while(salirAlfabetos==False):
        print('HAS ESCOGIDO OPERACIONES DE ALFABETOS! ELIGE LA OPERACION QUE DESEAS HACER:')
        print('\n')
        print("1. PERTENENCIA")
        print("2. UNION")
        print("3. INTERSECCION")
        print("4. COMPLEMENTO")   
        print("5. DIFERENCIA ABSOLUTA")          
        print("6. DIFERENCIA SIMETRICA")   
        print("7. SALIR DE ALFABETOS")
        

        opcAlfabetos = int(input("INTRODUZCA UN OPCION: "))

        if(opcAlfabetos==1):

            pertenciaAlfabetos()
        if(opcAlfabetos==2):

           unionAlfabetos()
        if(opcAlfabetos==3):

           interseccionAlfabetos()
        if(opcAlfabetos==4):

           complementoAlfabetos()
        if(opcAlfabetos==5):

           diferenciaAbsolutaAlfabetos()
        if(opcAlfabetos==6):

           diferenciaSimetricaAlfabetos()
        if(opcAlfabetos==7):
            salirAlfabetos=True
            print('Gracias por utilizar nuestro sistema!')
>>>>>>> 73e5fa823655244c8a5e2fa012a4e7557255be44
        