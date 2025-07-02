num_caixas = int(input()) #número de caixas
conteudo_caixas = []
saldo_inicial = 100 #início do saldo = 100sbecs

for i in range(0, num_caixas): #intervalo entre 0 e num_caixas - 1
    lista = conteudo_caixas.append(int(input())) #aidiciona a qtd de valores estabalecidos pelo intervalo (num_caixas, na teoria)
    if conteudo_caixas[i] >= 0: #se o índice que corresponde ao "i" for maior ou igual à 0
        saldo_inicial = saldo_inicial + conteudo_caixas[i] 

print(saldo_inicial)