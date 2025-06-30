valores = input().split()
X, Y = map(int, valores)

if Y >= 0 and Y <= 468:
    if X >=0 and X <= 432:
        print("dentro")

    else:
        print("fora")

else:
    print("fora")