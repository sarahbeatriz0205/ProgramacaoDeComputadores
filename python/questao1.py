nome = input("Nome:")
horas_trabalho = int(input("Horas trabalhadas:"))
valor_hora = float(input("Valor por hora:"))
salario = (horas_trabalho * valor_hora)

print(nome)
print("{:.2f}".format(salario))
 