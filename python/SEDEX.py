diametro = int(input())
caixa = input().split()
A, L, P = map(int, caixa)

if diametro > L or diametro > A or diametro > P:
    print("N")

else:
    print("S")