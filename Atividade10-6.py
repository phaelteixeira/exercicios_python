'''Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. Escreva uma função chamada is_anagram que tome duas strings e retorne True se forem anagramas.'''


def is_anagram(a,b):
    len_word1 = len(a)
    len_word2 = len(b)
    acum = 0
    
    if len_word1 == len_word2: 
            for i in range(len_word1):
                acum = acum + a.count(b[i])
            if acum == len_word1 and acum == len_word2:
                print("True")
            else:
                print("False")    
    else:
        print("False")

is_anagram("Holle","Elloh")