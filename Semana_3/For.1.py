class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        nombre= "Andres"
        datos =["Andres",18,True]
        numeros = (1,8,6,4,2)
        estudiante = {"Nombre": "Andres", "Edad": 50, "fac": "Unemi"}
        listaNotas = [(30,40),(20,40),(50,40)] 
        listaAlumnos = ({"Nombre":"Leonardo","Final":80},{"Nombre":"Adrian","Final":50},{"Nombre":"Daniela","Final":90})
        
        # j= 0
        # # while j<5:
        # #     print("while",j)
        # #     j= j+1
            
        for i in range(5):
            print("For",i)
        print()
        for i in range(1,5):
            print("For",i,end=" ")
        print()
        for i in range(2,10,2):
            print("For",i,end=" ")
        print()
        for i in range(12,3,-3):
            print("For",i,end=" ")
            
        lon = len(nombre)
        for pos in range(lon):
            if pos%2 == 0:
                print(pos,nombre[pos])
            
        for elem in nombre:
            print(elem,end=" ")
            
bucle = For()
bucle.usoFor()