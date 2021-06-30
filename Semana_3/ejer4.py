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
        
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,":",valor,end=" ")
            print()
bucle = For()
bucle.usoFor()