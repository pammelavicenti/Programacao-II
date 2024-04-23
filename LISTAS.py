#AULA 01 LISTAS 
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
    def maior(l):
        maior = l[0]

        for elem in l:
            if elem > maior:
                maior = elem
        return maior 
    

    #6-POSICAO DO MAXIMO
    '''Dada uma lista de numeros, faça uma função que encontre e retorne o índice do maior deles'''
    def posMaior(l):
        p = 0

        for i in range(len(l)):
            if l[i] > l[p]:
                p = i
        return p 
    

    print("Números pares de 1 a 100 em ordem regressiva:", pares())
    print("Números pares de 1 a 100 em ordem regressiva:", pares2())
    print(f"====="*30)
    
    print("Metade dos números digitados:")
    metade()
    print(f"====="*30)
    
    n = int(input("Digite a quantidade de numeros para leitura: "))
    print("Lista de números lida:", n_numeros(n))
    print(f"====="*30)
    
    l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
    print("Número de ocorrências de '3' na lista:", ocorrencias(3, l))
    print(f"====="*30)

    l = [10, 9, 20, 45, 0]
    print("Maior numero da lista: ", maior(l))
    print(f"====="*30)
    
    l = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 4, 3, 3, 3, 2, 1]
    print("Posição do maior numero:", posMaior(l))
    print(f"====="*30)

    '''07 - INVERTER
    DADA UMA LISTA FAÇA UM PROCEDIMENTO QUE INVERTA A ORDEM DE SEUS ELEMENTOS:
    2'''
    def troca(l, i, j):
        aux = l[i]
        l[i] = l[j]
        l[j] = aux 
    def inverte(l):
        posFinal = len(l)-1

        for i in range (len(l)//2):
            troca(l, i, posFinal-i)

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print (l)
    inverte(l)
    print(f'Lista invertida: {l}')
    print(f"====="*30)
    
    '''08 - FIBONACCI
    DADO UM NUMERO N, RETORNE UMA LISTA COM OS N PRIMEIROS ELEMENTOS DA SEQUENCIA DE FIBONACCI.
    OBS: CADA ELEMENTO DA SEQUENCIA É OBTIDO ATRAVÉS DA SOMA DOS DOIS ELEMENTOS ANTERIORES.
    '''
    def fib(n):
        if n == 1: return [1]
        elif n == 2: return [1, 1]
        else:
            l = [1, 1]

            for i in range(n-2):
                l.append(l[-1]+l[-2])
            return l
    print(f'Sequencia fibonacci: {fib(10)}')
    print(f"====="*30)

    '''09 - ORDENADAS E ABSCISSAS:

    '''
    def calcular_abscissas_e_ordenadas(abscissas, ordenadas):
        a = sum(1 for x in abscissas if x % 2 == 0)  # Conta o número de abscissas que são pares
        b = sum(1 for y in ordenadas if y % 2 != 0)  # Conta o número de ordenadas que são ímpares

        if a >= b:
            soma_abscissas = sum(abscissas)
            print("A soma de todas as abscissas é:", soma_abscissas)
        else:
            produto_ordenadas = 1
            for y in ordenadas:
                produto_ordenadas *= y
            print("O produto de todas as ordenadas é:", produto_ordenadas)

    # Exemplo de uso:
    abscissas = [1, 2, 3, 4, 5]
    ordenadas = [6, 7, 8, 9, 10]

    calcular_abscissas_e_ordenadas(abscissas, ordenadas)




main()

    
