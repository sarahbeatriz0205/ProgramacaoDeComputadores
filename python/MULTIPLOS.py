a = int(input())
b = int(input())

if b % a == 0 or a % b == 0: #executa uma ou outra função, pq eu não disse que A sempre seria maior ou menor que B. é um valor qualquer
    print("Multiplos")
else:
    print("Nao multiplos")