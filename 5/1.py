def is_divisor(s, i):
    ssize = len(s)
    for k in range (0, ssize):
        if (s[k] != s[k%i]):
            return False
    return True

[x,y] = input().split()
X = len(x)
Y = len(y)
count = 0

if (X > Y):
    sstr = y
    ssize = Y
    lstr = x
    lsize = X
else:
    sstr = x
    ssize = X
    lstr = y
    lsize = Y

for i in range(1, ssize+1):
    if ((ssize % i == 0) and (lsize % i == 0)):        
        if (sstr[0:i] == lstr[0:i]):            
            if ((is_divisor(sstr, i)) and (is_divisor(lstr, i))):
                count += 1
     
print(count)