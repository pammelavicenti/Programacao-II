#Regressiva: Faca uma funcao que crie e retorne uma lista com todos os numeros pares de 1 a 100, porem na ordem regressiva.
    
def pares():
    i = 100
    l = []

    while i >= 1:
        if i%2 == 0:
            l.append(i)
        i = i-1
    return l
def pares2():
    i = 100
    l = []

    while i >= 2:
        l.append(i)
        i = i-2
    return l 
print(pares())
print(pares2())


    
