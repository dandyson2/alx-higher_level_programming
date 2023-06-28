#!/usr/bin/python3
"""Module that defines a node for a singly linked list"""


class Node:
    """"Defines a node"""

    def __init__(self, data, next_node=None):
        """Initializes the node with instance variables

        Args:
            data: the data to be stored in the node
            next_node: reference to the next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data attribute

        Args:
            value: the value to set as the data

        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets the next_node attribute

        Returns:
            The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the next node

        Args:
            value: the node to set as the next_node

        Raises:
            TypeError: if value is not a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""
        self.head = None

    def __str__(self):
        """Returns a string representation of the linked list"""
        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """Inserts a node in a sorted fashion

        Args:
            value: the value to be inserted on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
