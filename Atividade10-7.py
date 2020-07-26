'''Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.'''

def has_duplicates(t):
    existe = 0
    for i in range(len(t)):
        for x in range(len(t)):
            if t[i] == t[x] and x != i:
                existe = 1
    if existe == 1:
        print("True")
    else:
        print("False")

l = [1,2,3,4]
l2 = [1,2,2,5]

has_duplicates(l)
has_duplicates(l2)