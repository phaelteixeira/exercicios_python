'''Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original.'''

t = [ 1 , 2 , 3]

def cumsum(t):
    acum = 0
    for x in range(len(t)):
        acum += t[x]
        t[x] = acum
    
    print(t)

cumsum(t)