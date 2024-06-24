def sorted_squared_brute_force(array):
    squared_array = [x*x for x in array].sort()
    return squared_array

def sorted_squared(array):
    len_array = len(array)
    left_pointer = 0
    right_pointer = len_array - 1
    squared_array = [0] * len_array
    for i in reversed(range(len_array)):
        if array[left_pointer]**2 > array[right_pointer]**2:
            squared_array[i] = array[left_pointer]**2
            left_pointer += 1
        else:
            squared_array[i] = array[right_pointer]**2
            right_pointer -= 1
    return squared_array


sq = sorted_squared([-3,-1,1,2,4])


