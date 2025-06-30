def dias_da_semana(dias, qtd_dias):
    lista_dias = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

    dia_atual = lista_dias.index(dias)
    evento = (dia_atual + qtd_dias) % 7

    return lista_dias[evento]