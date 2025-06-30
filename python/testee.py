nivel_1 = int(input())
nivel_2 = int(input())
nivel_3 = int(input())
nivel_4 = int(input())

maior = nivel_1
menor = nivel_1

if nivel_2 >= maior:
    maior = nivel_2
if nivel_3 >= maior:
    maior = nivel_3
if nivel_4 >= maior:
    maior = nivel_4

if maior == nivel_1:
    menor = nivel_2
    soma1 = nivel_3 + nivel_4
    soma2 = nivel_1 + nivel_2
    if nivel_3 < menor:
        menor = nivel_3
        soma1 = nivel_2 + nivel_4
        soma2 = nivel_1 + nivel_3
        if nivel_4 < menor:
            menor = nivel_4
            soma1 = nivel_2 + nivel_3
            soma2 = nivel_1 + nivel_4

if maior == nivel_2:
    menor = nivel_3
    soma1 = nivel_4 + nivel_1
    soma2 = nivel_2 + nivel_3
    if nivel_4 < menor:
        menor = nivel_4
        soma1 = nivel_1 + nivel_3
        soma2 = nivel_2 + nivel_4
        if nivel_1 < menor:
            menor = nivel_1
            soma1 = nivel_4 + nivel_3
            soma2 = nivel_1 + nivel_2

if maior == nivel_3:
    menor = nivel_4
    soma1 = nivel_2 + nivel_1
    soma2 = nivel_3 + nivel_4
    if nivel_2 < menor:
        menor = nivel_2
        soma1 = nivel_1 + nivel_4
        soma2 = nivel_3 + nivel_2
        if nivel_1 < menor:
            menor = nivel_1
            soma1 = nivel_4 + nivel_2
            soma2 = nivel_3 + nivel_1

if maior == nivel_4:
    menor = nivel_3
    soma1 = nivel_2 + nivel_1
    soma2 = nivel_4 + nivel_3
    if nivel_2 < menor:
        menor = nivel_2
        soma1 = nivel_1 + nivel_3
        soma2 = nivel_4 + nivel_2
        if nivel_1 < menor:
            menor = nivel_1
            soma1 = nivel_2 + nivel_3
            soma2 = nivel_4 + nivel_1

if soma1 < soma2:
    print(soma2 - soma1)
else:
    print(soma1 - soma2)