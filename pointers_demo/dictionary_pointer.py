dict1 = {'value': 11}
dict2 = dict1

print("Before dict2 update:")
print('dict1 = ', dict1)
print('dict2 = ', dict2)
print()
print('dict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))
print()

dict2['value'] = 22

print("After dict2 update:")
print('dict1 = ', dict1)
print('dict2 = ', dict2)
print()
print('dict1 points to: ', id(dict1))
print('dict2 points to: ', id(dict2))
print()

# Before dict2 update:
# dict1 =  {'value': 11}
# dict2 =  {'value': 11}
#
# dict1 points to:  4367252800
# dict2 points to:  4367252800
#
# After dict2 update:
# dict1 =  {'value': 22}
# dict2 =  {'value': 22}
#
# dict1 points to:  4367252800
# dict2 points to:  4367252800
########################################################################################################################
# dictionaries can be changed, integers were immutable, here as we can see if we change the value of a dictionary
# the value of the dictionary at the memory location will change
# now if we define another dict3 = {'value': 33} and make dict2= dict3 and dict1 = dict3
# then the original {'value': 22}in memory will have no pointers and then this will get removed by the garbage collector
########################################################################################################################
