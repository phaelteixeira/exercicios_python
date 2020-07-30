def interlock(word1,word2):
    if len(word1) == len(word2):
        new_word = ''
        for i in range(len(word1)):
            new_word = new_word + word1[i] + word2[i]
        print(new_word) 
    else:
        print("Can't not puzzle this word")

interlock('shoe','cold')