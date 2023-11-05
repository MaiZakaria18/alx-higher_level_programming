#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        x = my_list[0]
        for max in my_list:
            if max > x:
                return max
