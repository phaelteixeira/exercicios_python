'''Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento por palavra. Escreva duas versões desta função, uma usando o método append e outra usando a expressão t = t + [x] . Qual leva mais tempo para ser executada? Por quê?'''


l = "Uma frase para ficar como teste"

def version_1(t):
    n = []
    for i in range(len(t)):
        n.append(t[i])
    return n

def version_2(t):
    n = []
    for i in range(len(t)):
        n = n + [t[i]]
    return n

print(version_1(l))

print(version_2(l))