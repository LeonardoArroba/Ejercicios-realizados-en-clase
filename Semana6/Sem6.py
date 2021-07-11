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
    
    def primer(self):
        return self.lista[0]
    
    # def primerEliminado(self):
    #     primer = self.lista[0]
    #     auxlista = []
    #     for pos in range(1,len(self.lista)):
    #         auxlista.append(self.lista[pos])
    #     self.lista = auxlista
    #     return primer
    
    def primerEliminado2(self):
        primer = self.lista[0]
        self.lista = self.lista[1:] 
        return primer
    
    def ultimo(self):
        return self.lista[-1]
    
    def ultimoEliminado(self):
        ultimo = self.lista[-1]
        self.lista = self.lista[0:-1] 
        return ultimo
    
    # def ultimoEliminado2(self):
    #     ultimo = self.lista[-1]
    #     auxlista = []
    #     for pos in range(0,len(self.lista)-1):
    #         auxlista.append(self.lista[pos])
    #     self.lista = auxlista
    #     return ultimo
        
lista = [1,8,6,4,2,7] 
ord1 = Ordernar(lista)
# print(ord1.lista)
# print(ord1.primerEliminado2())
# print(ord1.lista)

# print(ord1.lista)
# print(ord1.ultimoEliminado())
# print(ord1.lista)

print("Normal",ord1.lista)
ord1.ordenarAsc()
print("Asc",ord1.lista)
ord1.ordenarDes()
print("Des",ord1.lista)
# print("Primer",ord1.primer())
# print("Primer",ord1.ultimo())
