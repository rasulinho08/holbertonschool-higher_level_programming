def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):  # Check if idx is out of range
        return my_list  # Return the list unchanged if invalid index
    # Remove the element at the specified index using slicing
    del my_list[idx]
    return my_list

