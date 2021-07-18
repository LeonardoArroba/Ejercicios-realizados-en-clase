# class Calculadora:
#     def suma(self,num1,num2):
#         return num1+num2
    
class Ejercicio:
    def __init__(self):
        pass
    
    def perfecto2(self,numero):
        acu=0
        for i in range(1,numero):
            if numero % i == 0:
                acu= acu+i
        return acu
    
    def divisores(self,num):
        cont=1
        divisores=[]
        while cont < num:
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
                cont = cont + 1
            print(divisores)
    
class Programacion(Ejercicio):
    def __init__(self):
        pass
    
    def divisores(self,num):
        cont=1
        divisores=[]
        for cont in range(1,num):
            rec = num % cont
            if rec == 0:
                divisores.append(cont)
        return divisores
            
# prog1 = Programacion()
# num=6
# acumDivisor = prog1.perfecto2(num)
# if acumDivisor == num:
#     print(num,"es perfecto")
# else:
#     print(num,"no es perfecto")
# numeros = [3,6,25,28]
# perfectos=[]
# for numero in numeros:
#     if prog1.perfecto2(numero) == numero:
#         perfectos.append(numero)
# print(perfectos)

prog1 = Programacion()
div = prog1.divisores(6)
lista = [1,2]
lista2 = lista+div
print(lista2)
# print(prog1.suma(5,7))
