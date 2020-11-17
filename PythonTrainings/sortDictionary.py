#sort by keys

def sortDictByKeys(mydict):
    for k,v in mydict.items():
        print(k + ':' + v)




#sort by values

if __name__ == '__main__':
    sortDictByKeys({"karnataka":"Bangalore", "TamilNadu":"Chennai", "Andhra":"Hyderabad"})