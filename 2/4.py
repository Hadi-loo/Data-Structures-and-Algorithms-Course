s = input()
members = s.split(",")
s = input()
gpmembers = s.split(",")
for i in range(len(members)):
    if members[i] in gpmembers:
        members[i] = '1'
    else:
        members[i] = '0'

count = 0
for i in range(len(members)):
    if members[i] == '1':
        if i != len(members) - 1:
            if members[i + 1] == '1':
                continue
            else:
                count += 1
        else:
            count += 1

print(count)
