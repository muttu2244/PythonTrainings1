def reverseList(arr):
    for i in range(0,len(arr)):
        arr.insert(i,arr.pop())
    return (arr)

if __name__ == '__main__':
    print(reverseList([4,6,9,2]))