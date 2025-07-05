segundos, massa = map(int, input().split())
contador_while = 0

#enquanto massa for maior que 0.5, faça isso:
while (massa > 0.5):
    massa = massa / 2
    contador_while += 1 #número de vezes que o while foi executado
tempo_total = contador_while * segundos #tempo total

dias = tempo_total // 86400
horas = tempo_total // 3600
if horas >= 24:
    horas = horas % 24
minutos = tempo_total // 60
if minutos >= 60:
    minutos = minutos % 60
segundo = tempo_total % 60
print(dias, "dias","{:02d}:{:02d}:{:02d}".format(horas, minutos, segundo))