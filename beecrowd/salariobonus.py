nome = input()
salario_fixo = float(input())
vendas_efetuadas = float(input())
comissao = (15 * vendas_efetuadas) / (100 * 1)
total = salario_fixo + comissao
print("TOTAL = R$", "{:.2f}".format(total))