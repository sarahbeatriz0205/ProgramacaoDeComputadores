def lista_troca_menor_primeiro(lista):
    menor = min(lista)
    indice_menor = lista.index(menor)
    
    
    if indice_menor == 0:
        return 0
    
    lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
    return 1
