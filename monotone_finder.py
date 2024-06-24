def monotonic_array(array):
    if len(array) <= 1:
        return True
    decreasing, increasing = True
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False

    return increasing or decreasing
