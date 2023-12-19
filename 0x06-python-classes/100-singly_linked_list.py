#!/usr/bin/python3
""" Node class """
class Node:
    """ contents of the Node class """
    def __init__(self, data, next_node=None):
        """
        initializes node
        Args:
            data: private attribute
            next_node: private attribute
        """
        self.data = data
        self.next_node = next_node

    
    @property
    def data(self):
        """
        getter: gets the data attribute of a node created
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Args:
            value: sets data to value of int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        getter: gets the next node attribute of the node created
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Args:
            value: sets next_node if value is next_node or None
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    definition of singly linked list

    Args:
        head: private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):
        """
        initizes singly linked list
        Attributes:
            head: private
        """
        self.__head = None
    
    def __str__(self):
        """
        string representation of singly linked list neaded to print
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        inserts new nodes into singly linked list in sorted order
        
        Args:
            value: int fata for the node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return

