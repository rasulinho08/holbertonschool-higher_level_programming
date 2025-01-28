def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None

    # Initialize the first element as the maximum
    max_val = my_list[0]

    # Iterate through the list to find the maximum
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val

