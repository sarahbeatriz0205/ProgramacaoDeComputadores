n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())

if (d2//v2) < (d1//v1): #se o tempo 2 for menor, significa que ele é mais rápido, logo, sendo o vencedor
    print(n2)

else:
    print(n1)