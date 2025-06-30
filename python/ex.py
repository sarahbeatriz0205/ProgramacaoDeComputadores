def primo_rec(n, x):
    if n <=1:
        return 0
    
    if x == 1:
        return 1
    
    if n % x == 0:
        return 0
    return primo_rec(n, x-1)

def primo(n):
    if primo_rec(n, n-1):
        return f"{n} é primo"
    else:
        return f"{n} não é primo"