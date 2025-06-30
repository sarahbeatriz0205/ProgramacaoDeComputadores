a11, a21 = map(int, input().split()) #avaliação 1 das duas etapas
a12, a22 = map(int, input().split()) #av 2 das duas etapas
p1, p2 = map(int, input().split()) #pesos

M1 = 1
M2 = 2
pesos = p1 + p2
m1 = ((a11 * p1) + (a21 * p2)) // pesos #média 1: a divisão tem maior prioridade, então sempre pôr a soma entre parênteses
m2 = ((a12 * p1) + (a22 * p2)) // pesos #média 2

if m1 == m2:
    print(M1)

elif m1 > m2:
    print(M1)

else:
    print(M2)