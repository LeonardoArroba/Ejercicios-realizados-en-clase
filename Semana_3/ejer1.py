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
            
        for pos,valor in enumerate(datos):
            print(pos,valor)
       
        for clave,valor in estudiante.items():
            print(clave,valor)
        
        for notas in listaNotas:
            for nota in notas:
                print(nota,end=" ")
            
bucle = For()
bucle.usoFor()