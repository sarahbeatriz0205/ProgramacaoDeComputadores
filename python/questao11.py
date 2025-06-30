distancia = int(input())
velocidade = int(input())
tempo = int((distancia / velocidade))
hora = int((tempo))
minutos = (tempo - hora * (60))

print("{:02d}".format(hora),":","{:02d}".format(minutos), sep="")