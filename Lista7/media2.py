#média normal:
limite = int(input())
lista = list(map(int, input().split()))
media = sum(lista) / limite

#contadores:
qtd_maiores = 0
qtd_menores = 0

#criadas para adição de valores posteriormente (só para o print)
lista_menores = []
lista_maiores = []
          
#percorre a lista e puxa a qtd de maiores e/ou menores:          
for valor in lista:
    if valor < media:
        qtd_menores += 1 #qtd_menores = qtd_menores + 1
        lista_menores.append(valor) #adiciona os valores que satisfazem essa condição à uma lista criada anteriormente
    else:
        qtd_maiores += 1
        lista_maiores.append(valor) #adiciona os valores que satisfazem essa condição à uma lista criada anteriormente



print("{:.1f}".format(media))
print(qtd_menores, *lista_menores)
print(qtd_maiores, *lista_maiores)