#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [replace if x is search else x for x in my_list]
    return new
