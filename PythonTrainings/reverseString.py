def reverseString(mystring):
    newstring = ''
    for i in range(-1,-len(mystring)-1, -1):
        newstring += mystring[i]
        print(newstring)
    print(newstring)


if '__name__' == '__main__':
    reverseString('bangalore')