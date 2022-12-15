#!/usr/bin/python3
"""6-peak module"""


def find_peak(list_of_integers):
    """files a peak in a list of unsorted integers

    Args:
        list_of_integers (list): list of integers
    """
    if len(list_of_integers) == 0:
        return None

    end = len(list_of_integers) - 1
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[end] > list_of_integers[end - 1]:
        return list_of_integers[end]

    mid = end // 2
    if (
        list_of_integers[mid] > list_of_integers[mid - 1]
        and list_of_integers[mid] > list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid+1])
    elif list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return list_of_integers[mid]
