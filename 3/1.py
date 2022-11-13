h, n = input().split()
n = int(n)
h = int(h)


def counter(first, last, height, left_first, n):
    if height == 0:
        return 0

    if (n < (first+last)/2):
        if left_first:
            return 1 + counter(first, (first+last)//2, height-1, False, n)
        return 2**(height) + counter(first, (first+last)//2, height-1, False, n)
    else:
        if left_first:
            return 2**(height) + counter((first+last)//2+1, last, height-1, True, n)
        return 1 + counter((first+last)//2+1, last, height-1, True, n)


print(counter(1, 2**h, h, True, n))
