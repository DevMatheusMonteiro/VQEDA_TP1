def greatest_number(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num
