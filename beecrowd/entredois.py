import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) #math.sqrt = raiz quadrada
print("{:.4f}".format(distancia))