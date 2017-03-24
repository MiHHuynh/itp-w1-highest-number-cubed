"""This is the entry point of the program."""


def highest_number_cubed(limit):
    start = 0
    while start**3 < limit:
        start += 1
    return start-1
