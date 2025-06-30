inicio = int(input("Início:"))
fim = int(input("Fim:"))
duracao = (fim - inicio)
hora = (duracao//60)
minutos = (duracao % 60)

print("Duração:",hora,":",minutos,sep="")