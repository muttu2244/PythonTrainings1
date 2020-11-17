
def primeornot(n):
    for i in range(2,n):
        if (n % i) == 0:
            print("Given num is not prime")
            break
    else:
        print ("Given number is prime")


primeornot(19)