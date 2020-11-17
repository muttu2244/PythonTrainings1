list1 = [1, 89, 9, 10, 8, 90]

max = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])

for i in range(2, len(list1)):
    if list1[i] > max:
        secondmax = max
        max = list1[i]
    else:
        if list1[i] > secondmax:
            secondmax = list1[i]

print("Second highest number is : ", str(secondmax))