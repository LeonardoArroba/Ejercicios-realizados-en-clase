class Ordernar:
    def __init__(self,lista):
        self.lista = lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
            
    def recorrerEnumerate(self):
        for pos,ele in enumerate(self.lista):
            print(pos,ele)

    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux

lista = [1,8,6,4,2,7] 
ord1 = Ordernar(lista)
print(ord1.lista)
ord1.ordenarAsc()
print(ord1.lista)