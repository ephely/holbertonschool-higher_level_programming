#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            final.append(div)
        except TypeError:
            print("wrong type")
            final.append(0)
        except ZeroDivisionError:
            print("division by 0")
            final.append(0)
        except IndexError:
            print("out of range")
            final.append(0)
    return final