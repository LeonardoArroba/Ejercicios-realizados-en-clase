class Ordernar:
    
    def __init__(self,lista):
        self.lista = lista
        
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux
                    
    def ordenarDes(self):
        for pos,ele in enumerate(self.lista):
            for sig in range(pos+1,len(self.lista)):
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]= self.lista[sig]
                    self.lista[sig]= aux

    def eliminar(self,num):
        enc= False
        for pos,ele in enumerate(self.lista):
            if num == ele:
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return enc
 

lista = [1,8,6,4,2] 
ord1 = Ordernar(lista)
print(ord1.eliminar(6))
print(ord1.lista)
# print("Normal",ord1.lista)
# ord1.ordenarAsc()
# print("Asc",ord1.lista)
# ord1.ordenarDes()
# print("Des",ord1.lista)