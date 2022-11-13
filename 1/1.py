n = int(input())
city = []
counts = []

count = 0
for i in range(n):
    temp = input()
    for ch in temp:
        if ch == 'B':
            count += 1
    city.append(temp)
    counts.append(count)
    count = 0

res = 0
for i in range(n):
    if counts[i] >= 2:
        res += counts[i]*(counts[i]-1)//2
    for j in range(n):
        if city[j][i] == 'B':
            count += 1
    if count >= 2:
        res += count*(count-1)//2
    count = 0


print(res)
