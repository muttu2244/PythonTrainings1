
arr = [4,9,1,8,2,5,6]

for i in range(0,len(arr)):
    print(str(i) + ':' + str(arr[i]))
    for j in range(i):
        print(str(j) + ':' + str(arr[j]))
        if (arr[j] > arr[j+1]):
            print(str(arr[j]) + ':' + str(arr[j+1]))
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
        print("+++++++++++++++++++++++++++++++++++++++\n")
    print(arr)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

print("*******************************************\n")
print(arr)
print("*******************************************\n")