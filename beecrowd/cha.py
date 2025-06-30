T = int(input())
lista = list(map(int, input().split()))
respostas_T = lista.count(T) #conta a ocorrência de tal elemento, quantas vezes ele aparece em tal lista
print(respostas_T)