i = 1
while i <= 5:
    print i
    i += 1
    if i == 3:
        break
else:
    print 'Hit the While/Else Statement!'

'''
def find_index(to_search, target):
  for i, value in enumerate(to_search):
    if value == target:
      break
  else:
    return -1
  return i


my_list = ['Corey', 'Rick', 'John']
index_location = find_index(my_list, 'Steve')

print 'Location of target is index: {}'.format(index_location)

'''