codigo_peca1, qtd_pecas1, valor_peca1, = map(float, input().split())
codigo_peca2, qtd_pecas2, valor_peca2, = map(float, input().split())
valor_a_pagar = (qtd_pecas1 * valor_peca1) + (qtd_pecas2 * valor_peca2)
print("VALOR A PAGAR: R$", "{:.2f}".format(valor_a_pagar))