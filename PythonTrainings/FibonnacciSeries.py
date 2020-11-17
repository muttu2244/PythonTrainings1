#Fibonnacci series are
#0, 1, 2, 3, 5, 8, 13, 21
#n is the given number to find first n number of fib series
#Ex: n=7, means first 7 fib series (that is: 0, 1, 1, 2, 3, 5, 8, 13)

def fib(n):
    first = 0
    second = 1
    print("Fibonnacci series are : ")
    print(first)
    print(second)

    for i in range(2,n+1):
        curr = first + second
        print(curr)
        first = second
        second = curr

fib(20)


