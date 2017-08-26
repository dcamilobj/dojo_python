class dojo:

    def __init__(self, x, y, s):
        self.menor=x
        self.mayor=y
        self.salto=s
        self.rang = range(menor,mayor,salto)

    def sum(self):
        count=0;
        for i in self.rang:
            count+=i  #count = count +1
        print(count)
        return(count)

print("Ingresar menor")
menor = int(input())

print("Ingresar mayor")
mayor = int(input())

print("Ingresar salto")
salto = int(input())

#rang = range(menor, mayor,salto)
calcular = dojo(menor, mayor, salto)
print(menor,mayor)

calcular.sum();
