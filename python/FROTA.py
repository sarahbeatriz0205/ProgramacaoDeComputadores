valores = input().split()
A, G, rendimento_A, rendimento_G = map(float, valores)

if rendimento_A / A > rendimento_G / G:
    print("A")

else:
    print("G")