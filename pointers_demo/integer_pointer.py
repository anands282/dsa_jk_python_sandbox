num1 = 11

num2 = num1

print("Before num2 is updated:")
print('num1: ', num1)
print('num2: ', num2)
print()
print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))
print()
######################################
# Expected output :
# Before num2 is updated:
# num1:  11
# num2:  11
#
# num1 points to:  4376701552
# num2 points to:  4376701552
#######################################

num2 = 22
print("after num2 is updated:")
print('num1: ', num1)
print('num2: ', num2)
print()
print("num1 points to: ", id(num1))
print("num2 points to: ", id(num2))
#######################################
# Expected output:
# num1:  11
# num2:  11
#
# num1 points to:  4307954288
# num2 points to:  4307954288
#
# after num2 is updated:
# num1:  11
# num2:  22
#
# num1 points to:  4307954288
# num2 points to:  4307954640
############################################################################################################################################################
# Integers are immutable, they cannot be changed, once we put a number 11 to a particular space in memory you cannot change it
# we can point num1 to another number in memory but cannot change 11
############################################################################################################################################################