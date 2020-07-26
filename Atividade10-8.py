'''Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem aniversário no mesmo dia? Você pode estimar esta probabilidade gerando amostras aleatórias de 23 dias de aniversário e verificando as correspondências. Dica: você pode gerar aniversários aleatórios com a função randint no módulo random.'''

import random

def generate_number():
    return random.randrange(1,100)
    


def birthday_paradox(t):
    p = (1/365)**t
    for i in range((366-t),366):
        p *= i
    print(1-p)

n = generate_number()
birthday_paradox(n)
