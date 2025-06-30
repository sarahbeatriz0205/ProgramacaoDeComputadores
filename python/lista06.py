def soma(a, b):
    resultado = a + b
    return resultado

n1, n2 = map(int, input().split())
n3 = soma(n1, n2)
print(n3)