x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia_sem_raiz = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
# raiz_da_distancia = distancia_sem_raiz * distancia_sem_raiz
print("{:.4f}".format(distancia_sem_raiz))