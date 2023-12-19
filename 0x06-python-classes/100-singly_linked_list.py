#!/usr/bin/python3
""" Node class """
class Node:
    """ contents of the Node class """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

        if isinstance(data, int) is not True:
            raise TypeError("data must be an integer")
        
        elif isinstance(next_node, Node) != True & next_node != None:
            raise TypeError("next_node must be a Node object")

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
            value:
         """
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
            value:
        """
        self.__next_node = value

""" SinglyLinkedList class """
class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    
    def __str__(self):
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
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

