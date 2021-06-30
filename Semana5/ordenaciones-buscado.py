class Ordernar:
    def __init__(self,lista):
        self.lista = lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
    
    def buscar(self,buscado):
        enc= False
        for pos,ele in enumerate(self.lista):
            if ele == buscado:
                enc= True
                break
        if enc == True:
            return pos 
        else: return -1

lista = [1,8,6,4,2,7]
ord1 = Ordernar(lista)

buscado= 2
resp = ord1.buscar(buscado)
if resp !=-1:
    print("Numero= {} se encuentra en la posicion: ({}) de la lista: {}".format(buscado,resp,ord1.lista))
else:
    print("Numero= {} no se encuentra en la lista: {}".format(buscado,ord1.lista))
