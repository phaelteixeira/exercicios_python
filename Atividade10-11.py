def reverse_pair(word1,word2):
    if len(word1) == len(word2):
        contador = 0
        y = len(word2) - 1
        for x in range(len(word1)):
            if word1[x] == word2[y - x]:
                contador += 1
        if len(word1) == contador and len(word2) == contador:
            print('Reverse pair')
        else:
            print('Not Reverse')
    else:
        print('Not Reverse')

reverse_pair('MELAO','OALEM')