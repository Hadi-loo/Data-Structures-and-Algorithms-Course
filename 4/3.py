a = input().split()
n = int(a[0])
m = int(a[1])
prisoners = n*[2]

relations = n*[]
for i in range(n):
    relations.append(n*[0])

cur = list(range(n-1,-1,-1))
is_possible = True
for k in range(m):
    a = input().split()
    i = int(a[0])
    j = int(a[1])
    relations[i-1][j-1] = 1
    relations[j-1][i-1] = 1

while ((len(cur) != 0) and (is_possible == True)):
    index = cur[-1]
    cur.pop()
    if (prisoners[index] == 2):
        prisoners[index] = 0
    for i in range(n):
        if (relations[i][index] == 1):
            if i in cur:
                cur.remove(i)
                cur.append(i)
            if (prisoners[index] == 0):
                if (prisoners[i] == 0):
                    is_possible = False
                    break
                elif (prisoners[i] == 1):
                    pass
                elif (prisoners[i] == 2):
                    prisoners[i] = 1
            elif (prisoners[index] == 1):
                if (prisoners[i] == 1):
                    is_possible = False
                    break
                elif (prisoners[i] == 0):
                    pass
                elif (prisoners[i] == 2):
                    prisoners[i] = 0

if not is_possible:
    print("No")
else:
    print("Yes")
    for i in range(n):
        print(prisoners[i], end=" ")