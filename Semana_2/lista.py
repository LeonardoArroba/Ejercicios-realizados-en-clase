class Sintaxis:
    instancia=0
    
    def __init__(self,dato="LLamando al constructor1"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
        
    def usoVariables(self):
        edad, _peso = 18, 70.5
        nombres = "Leonardo Arroba"
        dirDomiciliaria= "El Triunfo"
        Tipo_sexo = "M"
        civil= True
        
        usuario=() 
        usuario = ('Zancrow','186','zancrow1864@gmail.com')
        
        materias=[]
        materias = ['Programacion Web','PHP','POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        print(materias,aux,materias[1])

        
ejer1 = Sintaxis()
ejer1.usoVariables()