class Ordernar:
    def __init__(self,lista):
        self.lista = lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)
            
lista = [1,8,6,4,2,7]
ord1 = Ordernar(lista)
ord1.recorrerElemento()
ord1.recorrerEnumerate()
