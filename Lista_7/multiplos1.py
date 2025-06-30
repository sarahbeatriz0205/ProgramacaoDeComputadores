a, b = map(int, input().split())
lista = []
for i in range(1, b):
    produto = a * i

    if produto <= b:
        lista.append(produto)

print(*lista)