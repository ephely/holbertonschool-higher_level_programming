#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    symmetric_diff = list(set(set_1) - set(set_2))
    print(symmetric_diff)
