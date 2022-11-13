def por_bit_finder(first, second):
    num = first
    i = 0
    while num <= second:
        if not (first & 1):
            num += 2 ** i
        i += 1
        first = first >> 1

    return num - 2 ** (i - 1)


t = int(input())
nums = []
for i in range(t):
    first, second = input().split()
    nums.append([int(first), int(second)])

for i in range(t):
    print(por_bit_finder(nums[i][0], nums[i][1]))
