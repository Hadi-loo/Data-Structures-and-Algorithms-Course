import sys
sys.setrecursionlimit(10**5)

def island_size(park, i, j, n, m):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    new_members = 1
    for k in range(4):
        new_i = i + di[k]
        new_j = j + dj[k]
        if (new_i >= 0) and (new_j >= 0) and (new_i < n) and (new_j < m):
            if park[new_i][new_j][0]:
                if not park[new_i][new_j][1]:
                    park[new_i][new_j][1] = True
                    new_members += island_size(park, new_i, new_j, n, m)
    return new_members

a = input().split()
n = int(a[0])
m = int(a[1])
k = int(a[2])
park = []
res = []
sum = 0
for i in range(n):
    row = input()
    line = []
    for j in range(m):
        line.append([int(row[j]), False])
    park.append(line)

for i in range(n):
    for j in range(m):
        if park[i][j][0]:
            if not park[i][j][1]:
                park[i][j][1] = True
                trees = island_size(park, i, j, n, m)
                res.append(trees)

if (len(res) <= k):
    for i in range(len(res)):
        sum += res[i]
    print(sum)
else:
    res.sort(reverse=True)
    for i in range(k):
        sum += res[i]
    print(sum)