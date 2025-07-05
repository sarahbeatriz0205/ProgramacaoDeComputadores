num_jogos = int(input())
portas = []
contador = 0

for i in range(0, num_jogos):
    adicao = portas.append(int(input()))
    if portas[i] != 1:
        contador = contador + 1

print(contador)