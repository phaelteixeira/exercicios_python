'''Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, e False se não for o caso.'''

def is_sorted(t):
    aux = 0
    first = t[0]
    existe = 0
    while(aux < len(t)):
        if first <= t[aux]:
            first = t[aux]
        else:
            existe = 1
        aux += 1
    if existe == 1:
        print('False')
    else:
        print('True')

l = [1,2,2]
l2 = ['b','a']

is_sorted(l)
is_sorted(l2)