def dia(dia, mes, ano):
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


    if mes < 1 or mes > 12:
        return "Data Invalida"
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return "Data Invalida"

    dia_formatado = "{:02d}".format(dia)

    return f"{dia_formatado} de {meses[mes - 1]} de {ano}" #f = diz ao programa que esse é um trecho formatado, tendo o poder de formatar também
#por que [mes - 1]? porque ele {meses} irá me retornar o mês inserido e vai utilizar o [mes - 1] para encontrar dentro da lista
#ex: mes = 04 / 04 - 1 = 3: 3 é o índice do elemento na lista
