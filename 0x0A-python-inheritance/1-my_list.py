#!/usr/bin/python3
"""Module 1-my_list

This Module contains a definition for MyList Class
"""


class MyList(list):
    """Custom List"""

    def print_sorted(self):
        """
        prints the list in ascending sort
        """
        print(sorted(self))
