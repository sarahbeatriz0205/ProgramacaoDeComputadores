limite = int(input())
lista = list(map(int, input().split()))
media = sum(lista) / limite
    
qtd_maiores = 0
qtd_menores = 0
          
for valor in lista:
    if valor < media:
        qtd_menores += 1 #qtd_menores = qtd_menores + 1
    else:
        qtd_maiores += 1
                
print("{:.1f}".format(media))
print(qtd_menores)
print(qtd_maiores)