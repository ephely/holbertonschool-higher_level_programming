#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght = len(my_list) - 1
    if idx < 0 or idx > lenght:
        return (my_list)
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
