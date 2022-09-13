#!/usr/bin/python3
"""Module 100-singly_lined_list

This Module contains an definition for Node and SinglyLinkedList class
"""


class Node:
    """A class that represents a node in a linked list"""

    def __init__(self, data, next_node=None):
        """initialize Node class

        Args:
            data (int): the data to be stored
            next_node (Node, optional): the next node. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """the data property

        Returns:
            int: the data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """the data setter

        Args:
            value (int): the value to be set

        Raises:
            TypeError: raised if the data in not an integer
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """the next node

        Returns:
            Node: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter

        Args:
            value (Node): the next node object

        Raises:
            TypeError: raised if next_node is not an Node object
        """
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class that represents a singly linked list"""

    def __init__(self):
        """Initializes a singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a value to a linked list in ascending order

        Args:
            value (int): value of hte node
        """
        if self.__head is None:
            self.__head = Node(value)
        else:
            if self.__head.data > value:
                self.__head = Node(value, self.__head)
            else:
                temp = self.__head
                while temp is not None:
                    if temp.next_node is None:
                        temp.next_node = Node(value)
                        return
                    elif temp.next_node.data > value:
                        temp.next_node = Node(value, temp.next_node)
                        return
                    temp = temp.next_node

    def __str__(self):
        """string representation of the singly linked list

        Returns:
            str: string for printing
        """
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node

        return "\n".join(values)
