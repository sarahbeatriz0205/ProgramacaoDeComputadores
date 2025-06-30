valorproduto = int(input("Preço:"))
itensqtd = int(input("Qtd:"))
valor_a_pagar = (valorproduto * itensqtd)
seu_dinheiro = int(input("Seu dinheiro:"))
troco = (seu_dinheiro - valorproduto * (itensqtd))

print("A pagar:", valor_a_pagar)
print("Troco:", troco)