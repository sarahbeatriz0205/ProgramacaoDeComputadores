traseira_A = int(input())
traseira_B = int(input())
traseira_C = int(input())

distancia_A = traseira_B - traseira_A
distancia_C = traseira_C - traseira_B

if distancia_A < distancia_C:
    print("1")
elif distancia_A == distancia_C:
    print("0")
else:
    print("-1")