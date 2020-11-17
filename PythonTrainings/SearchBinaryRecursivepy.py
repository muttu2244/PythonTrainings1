def bsearch(mylist,start,end,value):
    if (end < start):
        return (None)
    else:
        mid = (start + end) // 2
        if mylist[mid] > value:
            return (bsearch(mylist,start,mid-1,value))
        elif mylist[mid] < value:
            return (bsearch(mylist, mid+1,end,value))
        else:
            return (mid)


print(bsearch([3,6,9,15,18,24,30],0,7,6))

#print(bsearch([3,6,9,15,18,24,30],0,7,45))
