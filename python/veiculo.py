# FEITO PELO CHAT GPT:
# Leitura do valor final de venda do automóvel
valor_venda = float(input("Digite o valor final de venda do automóvel: R$ "))

# Percentuais dos impostos (todos sobre o valor de custo)
ICMS = 0.18
IPI = 0.13
PIS = 0.014
COFINS = 0.076

# Soma das alíquotas para cálculo reverso do valor de custo
total_impostos = 1 + ICMS + IPI + PIS + COFINS

# Cálculo do valor sem impostos (valor de custo)
valor_custo = valor_venda / total_impostos

# Cálculo dos valores de cada imposto
valor_icms = valor_custo * ICMS
valor_ipi = valor_custo * IPI
valor_pis = valor_custo * PIS
valor_cofins = valor_custo * COFINS

# Exibição dos resultados com 2 casas decimais
print("\n--- Detalhamento dos custos ---")
print(f"Valor de custo sem impostos: R$ {valor_custo:.2f}")
print(f"ICMS (18%): R$ {valor_icms:.2f}")
print(f"IPI (13%): R$ {valor_ipi:.2f}")
print(f"PIS (1,4%): R$ {valor_pis:.2f}")
print(f"Cofins (7,6%): R$ {valor_cofins:.2f}")