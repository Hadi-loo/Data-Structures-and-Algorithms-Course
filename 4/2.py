import sys
sys.setrecursionlimit(10**5)

def shortest_path(pyramid, i, j, n, m):
    di = [0,-1,-1,-1,0,1,1,1]
    dj = [1,1,0,-1,-1,-1,0,1]
    rs = []
    for k in range(8):
        new_i = i + di[k]
        new_j = j + dj[k]
        if (new_i >= 0) and (new_j >= 0) and (new_i < n) and (new_j < m):
            rs.append(pyramid[new_i][new_j][1])
            pyramid[new_i][new_j][1] = True
        else:
            rs.append(True)

    paths = []
    for k in range(8):
        new_i = i + di[k]
        new_j = j + dj[k]
        if (new_i >= 0) and (new_j >= 0) and (new_i < n) and (new_j < m):
            if (pyramid[new_i][new_j][0] == "@"):
                #if not pyramid[new_i][new_j][1]:
                if not rs[k]:
                    #pyramid[new_i][new_j][1] = True
                    temp = shortest_path(pyramid, new_i, new_j, n, m)
                    #pyramid[new_i][new_j][1] = False
                    if temp != -1:
                        paths.append(temp)
        else:
            return 1
    if len(paths) == 0:
        return -1
    return 1 + min(paths)

a = input().split()
n = int(a[0])
m = int(a[1])
pyramid = []
start = []
for i in range(n):
    row = input()
    line = []
    for j in range(m):
        line.append([row[j], False])
        if row[j] == "$":
            start.append(i)
            start.append(j)
    pyramid.append(line)

pyramid[start[0]][start[1]][1] = True
res = shortest_path(pyramid, start[0], start[1], n, m)
print(res)