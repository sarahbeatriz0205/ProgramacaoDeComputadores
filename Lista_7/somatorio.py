n = int(input())
soma = 0 #acumulador

for i in range(1, n+1):
    soma = soma + (1 / i) # soma = 0 + (1/1) = 1 ------------------> soma = 1 + (1/2) = 1.5...

print("{:.4f}".format(soma))