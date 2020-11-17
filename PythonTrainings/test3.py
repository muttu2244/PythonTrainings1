''''''
# list1=[1,3,5,7,9,11,13]
# target_sum=22
#
# #for i in range(0,len(list1)):   #(0,7)
#
# for j in range(i+1, len(list1)): #(1,7)
#     if (list1[i] + list1[j]) == target_sum:    # (1
#         print(i, j)
#
#
#
# #1+3
# #3+5
# #5+7
# #7+9
# #9+11
# #11+13


def division(func):
    def inner(a, b):
        if (a < b):
            a, b = b, a
        return(func(a,b))
    return(inner)

@division
def mydiv(a,b):
    print (a/b)

mydiv(2,4)



