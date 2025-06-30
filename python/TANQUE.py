consumo_por_litro = int(input())
distancia = int(input())
combustivel = int(input()) # restante antes do abastecimento

combustivel_necessario = distancia / consumo_por_litro # QUANTO PRECISA PRA CHEGAR AO AEROPORTO

if combustivel_necessario > combustivel: # SE O QUE EU PRECISO FOR MAIOR QUE O QUE TENHO, TIRO A DIFERENÇA ENTRE ELES
    compra = combustivel_necessario - combustivel

else: #SENÃO, NADA
    compra = 0

print("{:.1f}".format(compra))