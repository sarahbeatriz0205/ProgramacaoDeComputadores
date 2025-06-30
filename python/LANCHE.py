valores = input().split()
código, qtd = map(float, valores)

c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5

if código == c1:
    print("Total: R$","{:.2f}".format(qtd * 4.00))

if código == c2:
    print("Total: R$","{:.2f}".format(qtd * 4.50))

if código == c3:
    print("Total: R$","{:.2f}".format(qtd * 5.00))

if código == c4:
    print("Total: R$","{:.2f}".format(qtd * 2.00))

if código == c5:
    print("Total: R$","{:.2f}".format(qtd * 1.50))