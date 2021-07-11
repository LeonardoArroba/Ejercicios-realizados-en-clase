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

    def insertar(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
        
    # def insertar2(self,num):
    #     self.ordenarAcs()
    #     auxlista=[]
    #     for pos,ele in enumerate(self.lista):
    #         if num < ele:
    #             break
    #     for i in range(pos):
    #         auxlista.append(self.lista[i])
    #     auxlista.append(num)
    #     for j in range(pos,len(self.lista)):
    #         auxlista.append(self.lista[j])
    #     self.lista=auxlista
            
    # def insertarOrden(self,num):
    #     self.lista.append(num)
    #     self.ordenarAcs()

lista = [1,8,6,4,2,7] 
ord1 = Ordernar(lista)
print(ord1.insertar(5))
print(ord1.lista)
# print("Normal",ord1.lista)
# ord1.ordenarAcs()
# print("Asc",ord1.lista)
# ord1.ordenarDes()
# print("Des",ord1.lista)                                                                                                                                                                                                                                                                                                                           
