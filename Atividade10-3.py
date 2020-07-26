'''Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos.'''

t = [1,2,3,4]

def middle(t):
    print(t[1:len(t)-1])

middle(t)