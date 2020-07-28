l = ['Abacaxi','Maça','Kiwi','Melancia','Melao','Jaca','Jambo']

def in_bisect(t,palavra):
    total = len(t)
    metade = int(total / 2)
    if palavra in t[0:metade-1]: 
        print('Na primeira metade')
    elif palavra in t[metade:]:
        print('Na segunda metade')
    else:
        print('Palavra nao encontrada')

in_bisect(l,'Pitanga')
