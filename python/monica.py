M = int(input())
A = int(input())
B = int(input())
C = M - (A + B) #DESCOBRE O VALOR QUE FALTA

#CONSIDERAR TODAS AS POSSIBILIDADES
if A > C and A > B:
    print(A)

elif B > A and B > C:
    print(B)

else:
    print(C)