n = int(input())

contador = 0

if n <= 1:
    print("Não")
else:
    for i in range(1, n+1):
        if n % i == 0:
            contador += 1
    if contador == 2:
        print("Sim")
    else:
        print("Não") 