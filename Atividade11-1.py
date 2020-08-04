def reade_words(t):
    dic = dict()
    for i in t:
        val = t[i]
        if val not in dic:
            dic[val] = i
    return dic

l = 'Fazendo apenas um teste'
reade_words(l)