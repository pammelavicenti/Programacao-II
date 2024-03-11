#METADE
#faca um procedimento que leia 10 numeros digitados pelo usuario, armazene a metade de cada um deles numa lista, e depois imprima esta lista.

def metade():
    l = []

    for i in range (10):
        n = float(input("digite um numero: "))
        l.append(n/2)
    for n in l:
        print(n)
metade()
#testando 