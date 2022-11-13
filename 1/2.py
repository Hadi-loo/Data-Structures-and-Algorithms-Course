n = int(input())
seq = input().split()
for i in range(2*n):
    seq[i] = int(seq[i])
seq.sort()
for i in range(n):
    print(seq[i], seq[n + i], end=" ")