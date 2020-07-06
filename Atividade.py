'''Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo: >>> t = [[ 1 , 2 ], [ 3 ], [ 4 , 5 , 6 ]]'''


t = [[ 1 , 2 ], [ 3 ], [ 4 , 5 , 6 ]]

def nested_sum(t):
    total = 0
    for x in range(len(t)):
        total += sum(t[x])
    print(total)

nested_sum(t)