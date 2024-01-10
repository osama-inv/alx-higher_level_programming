#!/usr/bin/python3

def search_replace(list, fetch, to):
    neuveux_liste = [to if x == fetch else x for x in list]
    return neuveux_liste
