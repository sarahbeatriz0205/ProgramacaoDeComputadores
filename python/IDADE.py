#mediana manual:

a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a <= c) or (a <= b) and (a >= c): #considerar as igualdades
    camila = a

elif (b >= a) and (b <= c) or (b <= a) and (b >= c):
    camila = b

else:
    camila = c

print(camila)