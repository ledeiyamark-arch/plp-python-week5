import math


def tables_needed(people, seats_per_table):
    return math.ceil(people / seats_per_table)


def welcome(name):
    return f"Welcome, {name}!"