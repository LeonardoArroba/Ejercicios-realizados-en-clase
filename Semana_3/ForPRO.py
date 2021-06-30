from math import e

class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        nombre = "Andres"
        datos = ["Andres", 18, True]
        numeros = (2,5,6,4,1)
        docente = {'nombre':'Andres','Edad':18,'fac':'Unemi'}
        listaNotas = [(30,40),(20,40),(50,40)] 
        listaAlumnos = [{"nombre":"Leonardo","final":70},{"nombre":"Adrian","final":60},{"nombre":"Daniela","final":90}]
        # j=0          #si se usa while
        # while j<5:
        #     print('while', j)
        #     j=j+1
            
        # for i in range(5):
        #     print('for',i,end=" ")
        # print()
        # for i in range(1,5):
        #     print('for',i,end=" ")
        # print()
        # for i in range(2,10,2):
        #     print('for',i,end=" ")
        # print()
        # for i in range(12,3,-3):
        #     print('for',i,end=" ") 
         
        # lon = len(datos)  
        # for pos in range(lon):
        #     if pos%2 == 0 and pos !=0:
        #         print(pos,datos[pos])
            
        # vocal = ('a','e','i','o','u')
        # for elen in datos:
        #     print(elen,end=" ")
        # for elen in nombre:
        #     print(elen,end=" ")

        # lon = len(datos)  
        # for pos in range(lon):
        #     print(pos,datos[pos])
            
        # for pos, valor in enumerate(datos):    
        #     print(pos,valor)
      
        # for clave,valor in docente.items():
        #     print(clave,valor,end=" ")
            
        # for notas in listaNotas:
        #     for nota in notas:
        #         print(notas,end=" ")
        #     print("Saliendo del for interno")
        
        # print(listaNotas)
        # for notas in listaNotas:
        #     acum=0
        #     for nota in notas:
        #         acum=acum+nota
        #     print("Saliendo del for interno")    
            
        # listaAlumnos = [{"nombre":"Leonardo","final":70},{"nombre":"Adrian","final":60},{"nombre":"Daniela","final":90}]
        # print("/nDiccionario de alumnos")  
        # print(listaAlumnos)
        # acum=0
        
        # for alumnos in listaAlumnos:
        #     print(alumnos,len(alumnos))
        #     for clave,valor in alumnos.items():
        #         print(clave,":",valor,type, end="  ")
        #         if clave == 'final':
        #             acum=acum+valor
                    
        #     print()
        # print("Promedio", acum/len(listaAlumnos))
        
        listaNotas = [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+len(notas)
            acum=acum+acumparcial
            print("Pracial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas)))
        print("TotalGeneral:{} PromGeneral:{}".format(acum,acum/cont))
bucle = For() 
bucle.usoFor()
