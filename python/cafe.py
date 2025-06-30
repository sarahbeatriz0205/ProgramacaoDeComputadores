pessoas_andar1 = int(input())
pessoas_andar2 = int(input())
pessoas_andar3 = int(input())
tempo1 = pessoas_andar1 * 2
tempo2 = pessoas_andar2 * 2
tempo3 = 

if tempo1 <= tempo2 and tempo1 <= tempo3:
    menor_tempo = tempo1

elif tempo2 <= tempo1 and tempo2 <= tempo3:
    menor_tempo = tempo2

else:
    menor_tempo = tempo3

print(menor_tempo)