valor = int(input())
print(valor)

valor1 = int(valor / 100)
valor = int(valor % 100)

valor2 = int(valor / 50)
valor = int(valor % 50)

valor3 = int(valor / 20)
valor = int(valor % 20)

valor4 = int(valor / 10)
valor = int(valor % 10)

valor5 = int(valor / 5)
valor = int(valor % 5)

valor6 = int(valor / 2)
valor = int(valor % 2)

valor7 = int(valor / 1)

print(valor1, "nota(s) de R$100,00")
print(valor2, "nota(s) de R$50,00")
print(valor3, "nota(s) de R$20,00")
print(valor4, "nota(s) de R$10,00")
print(valor5, "nota(s) de R$5,00")
print(valor6, "nota(s) de R$2,00")
print(valor7, "nota(s) de R$1,00")