def reade_words(t):
    dic = dict()
    for i in range(len(t)):
        val = t[i]
        if val not in dic:
            '''Pra não sair assim pulando varias casas ou numeros, somente adicionar um contador que ele vai fazer a numeracao ir em ordem correta'''
            dic[val] = i
    return dic

l = 'Fazendo apenas um teste'
h = reade_words(l)
print(h)