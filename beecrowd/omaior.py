a, b, c = map(int, input().split())
maiorAB = (a+b+abs(a-b))//2 #MAIOR ENTRE DOIS NÚMEROS
maiorABC = (maiorAB+c+abs(maiorAB-c))//2 #MAIOR ENTRE TRÊS NÚMEROS
print(maiorABC, "eh o maior")