consumo = int(input())
conta = 7

if consumo <= 10:
    conta = 7

elif consumo <=30:
   conta += ((consumo - 10)) * 1

elif consumo <=100:
    conta+= 20 * 1
    conta += ((consumo - 30)) * 2

elif consumo >=101:
    conta += 20 * 1
    conta += 70 * 2
    conta += ((consumo - 100)) * 5

print(conta)