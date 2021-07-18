class Ejercicio:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))
    
    def perfecto(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu= acu+i
        if numero == acu:
            print("{} es perfecto".format(numero))
        else:
            print("{} no es perfecto".format(numero))
            
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu= acu+i
        return acu
                
ejer1= Ejercicio()
num = int(input("Ingrese un numero:"))
print("Llamada 1")
ejer1.parImpar(num)
ejer1.perfecto(num)
print()
# lista= [1,8,6,4,2,7,10]
# print("Llamada 2")
# for num in lista:
#     ejer1.parImpar(num)
# print()
# print("Llamada 3")
# ejer1.parImpar(23)

