valores = input().split()
x, y = map(float, valores)

if x == 0:
    if y == 0:
        print("Origem")
    
    else:
        print("Eixo Y")
        
else: 
    if y == 0:
        print("Eixo X")

    if y > 0:
        if x > 0:
            print("Q1")

        else:
            print("Q2")

    else:
        if x < 0:
            print("Q3")
    
        else:
            print("Q4")