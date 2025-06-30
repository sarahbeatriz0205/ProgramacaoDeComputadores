A, B, C, D = map(int, input().split())

if (A + B > C) and (A + C > B) and (B + C > A) or (A + B > D) and (A + D > B) and (B + D > A) or (C + B > D) and (D + B > C) and (D + C > B):
    print("S")

else:
    print("N")