#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        is_multiple_of_2 = num % 2 == 0
        result.append(is_multiple_of_2)
    return result
