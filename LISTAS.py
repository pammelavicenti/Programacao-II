#1-Regressiva: Faca uma funcao que crie e retorne uma lista com todos os numeros pares de 1 a 100, porem na ordem regressiva.
def main():   
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

        while i >= 2:  # Alteração aqui: iterando até 2 com passo -2
            l.append(i)
            i -= 2  # Alteração aqui: passo -2 para encontrar números pares em ordem regressiva
        return l
    

    #2-METADE
    #faca um procedimento que leia 10 numeros digitados pelo usuario, armazene a metade de cada um deles numa lista, e depois imprima esta lista.

    def metade():
        l = []

        for i in range (10):
            n = float(input("digite um numero: "))
            l.append(n/2)
        for n in l:
            print(n)
    

    #3-LEITURA
    #Dado um numero N, faça uma fanção que leia N números inteiros e retorne uma lista com esses números.

    def n_numeros(n):
        i = 1
        l = []

        for i in range(n):
            x = int(input("Digite um numero: "))
            l.append(x)
        

        return l
    

    #4- OCORRENCIAS
    #Dada uma lista e um elemento, retorne o numero de ocorrencias do elemento na lista.

    def ocorrencias (x, l):
        n = 0 

        for elem in l:
            if elem == x:
                n += 1 
        return n 
    

    #5-MAXIMO 
    #Dada uma lista de numeros, faça uma função que encontre e retorne o maior deles.
    # Chamando as funções
    print("Números pares de 1 a 100 em ordem regressiva:", pares())
    print("Números pares de 1 a 100 em ordem regressiva:", pares2())
    
    print("Metades dos números digitados:")
    metade()
    n = int(input("Digite a quantidade de numeros para leitura: "))
    print("Lista de números lida:", n_numeros(n))
    
    l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
    print("Número de ocorrências de '3' na lista:", ocorrencias(3, l))
    
main()

    
