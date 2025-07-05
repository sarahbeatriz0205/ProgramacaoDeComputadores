n = int(input())
seq = [int(input()) for _ in range(n)]

count = 1  # sempre podemos marcar o primeiro número
last = seq[0]

for i in range(1, n):
    if seq[i] != last:
        count += 1
        last = seq[i]

print(count)
