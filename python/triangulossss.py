A, B, C = int(input())

if A + B <= C or A + C <= B or B + C <= A:
    print("n")

else:
    if C * C == B * B + A * A:
        print("r")

        if C * C < A * A + B * B:
            print("a")
        else:
            print("o")