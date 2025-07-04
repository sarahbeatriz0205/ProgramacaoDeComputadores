num_caixas = int(input()) #número de caixas
conteudo_caixas = []
saldo = 100 #início do saldo = 100sbecs
saldo_atual = 100

for i in range(0, num_caixas): #intervalo entre 0 e num_caixas - 1
    conteudo_caixas.append(int(input())) #adiciona a qtd de valores estabalecidos pelo intervalo (num_caixas, na teoria)
    saldo_atual = saldo_atual + conteudo_caixas[i]

    if saldo_atual >= saldo: #se isso não for verdade, ele não conta
        saldo = saldo_atual

print(saldo)