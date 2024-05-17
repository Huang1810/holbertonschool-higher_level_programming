#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = set()
    for num in my_list:
        uniques.add(num)
    return sum(uniques)
