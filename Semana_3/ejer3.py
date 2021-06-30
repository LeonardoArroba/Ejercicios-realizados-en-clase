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
        
        print(listaNotas)
        for notas in listaNotas:
            acum = 0
            for nota in notas:
                acum = acum + nota
            print(acum/len(notas),end=" ")
            
bucle = For()
bucle.usoFor()