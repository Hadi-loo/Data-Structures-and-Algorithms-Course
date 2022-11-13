def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

n = int(input())
hardwork = input().split()
teamwork = input().split()

sorted_hw = []
sorted_tw = []
sorted_sum = []

hw_sum = 0
tw_sum = 0

for i in range(n):

    x = int(hardwork[i])
    y = int(teamwork[i])
    hardwork[i] = [x, False]
    teamwork[i] = [y, False]

    sorted_hw.append((x, i))
    sorted_tw.append((y, i))
    sorted_sum.append((x + y, i))

    hw_sum += x
    tw_sum += y

merge_sort(sorted_sum)

k = 0
chosen = []
chosen_hw_sum = 0
chosen_tw_sum = 0

for i in range(n):

    if ((chosen_hw_sum > hw_sum - chosen_hw_sum) 
        and (chosen_tw_sum > tw_sum - chosen_tw_sum)):

        break


    elif ((chosen_hw_sum <= hw_sum - chosen_hw_sum) 
        and (chosen_tw_sum <= tw_sum - chosen_tw_sum)):

        chosen.append(sorted_sum[i][1])
        chosen_hw_sum += hardwork[sorted_sum[i][1]][0]
        chosen_tw_sum += teamwork[sorted_sum[i][1]][0]
        hardwork[sorted_sum[i][1]][1] = True
        teamwork[sorted_sum[i][1]][1] = True
        k += 1


    elif ((chosen_hw_sum > hw_sum - chosen_hw_sum) 
        and (chosen_tw_sum <= tw_sum - chosen_tw_sum)):

        merge_sort(sorted_tw)

        for j in range(n):
            if (chosen_tw_sum > tw_sum - chosen_tw_sum):
                break

            elif (teamwork[sorted_tw[j][1]][1] == False):
                chosen.append(sorted_tw[j][1])
                chosen_hw_sum += hardwork[sorted_tw[j][1]][0]
                chosen_tw_sum += teamwork[sorted_tw[j][1]][0]
                hardwork[sorted_tw[j][1]][1] = True
                teamwork[sorted_tw[j][1]][1] = True
                k += 1


    elif ((chosen_hw_sum <= hw_sum - chosen_hw_sum) 
        and (chosen_tw_sum > tw_sum - chosen_tw_sum)):

        merge_sort(sorted_hw)

        for j in range(n):
            if (chosen_hw_sum > hw_sum - chosen_hw_sum):
                break

            elif (hardwork[sorted_hw[j][1]][1] == False):
                chosen.append(sorted_hw[j][1])
                chosen_hw_sum += hardwork[sorted_hw[j][1]][0]
                chosen_tw_sum += teamwork[sorted_hw[j][1]][0]
                hardwork[sorted_hw[j][1]][1] = True
                teamwork[sorted_hw[j][1]][1] = True
                k += 1

print(k)
for i in range(k):
    print(chosen[i] + 1, end=" ")