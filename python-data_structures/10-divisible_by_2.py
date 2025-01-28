#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list with True or False for each element
    result = [num % 2 == 0 for num in my_list]
    return result

