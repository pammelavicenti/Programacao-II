#1-Regressiva: Faca uma funcao que crie e retorne uma lista com todos os numeros pares de 1 a 100, porem na ordem regressiva.
    
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


#2-METADE
#faca um procedimento que leia 10 numeros digitados pelo usuario, armazene a metade de cada um deles numa lista, e depois imprima esta lista.

def metade():
    l = []

    for i in range (10):
        n = float(input("digite um numero: "))
        l.append(n/2)
    for n in l:
        print(n)
metade()

#3-LEITURA
#Dado um numero N, faça uma fanção que leia N números inteiros e retorne uma lista com esses números.

def n_numeros(n):
    i = 0
    l = []

    while i < n:
        x = int(input("Digite um numero: "))
        l.append(x)
        i += 1

    return 1
n = int(input("Digite a quantidade de numeros: "))
print(n_numeros(n))

#4- OCORRENCIAS
#Dada uma lista e um elemento, retorne o numero de ocorrencias do elemento na lista.

def ocorrencias (x, l):
    n = 0 

    for elem in l:
        if elem == x:
            n += 1 
    return n 
l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
print(ocorrencias (3,l))

#5-MAXIMO 
#Dada uma lista de numeros, faça uma função que encontre e retorne o maior deles.



    
