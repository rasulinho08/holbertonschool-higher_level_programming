#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}:".format(i), a_dictionary[i])
