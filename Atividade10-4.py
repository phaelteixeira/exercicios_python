'''Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne None.'''

t = [1,2,3,4]

def chop(t):
    del t[0]
    del t[len(t)-1]
    print(t)

chop(t)