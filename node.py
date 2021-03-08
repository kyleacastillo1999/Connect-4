"""
Created with Pycharm
Author: Kyle Castillo
Date: 03/08/2021
Contact: kylea.castillo1999@gmail.com
"""

"""
A node class that keeps track of:
North, South, East, West, and diagonals.
The player_id of the position:
0 - open
1 - player 1
2 - player 2
"""


class C4Node:
    # Constructor
    def __init__(self, node_id):
        """
        :param node_id: 0, 1, 2, corresponding to open, player 1, and player 2
        """
        self.n_id = node_id
        self.__north = None
        self.__south = None
        self.__west = None
        self.__east = None
        self.__n_west = None
        self.__n_east = None
        self.__s_west = None
        self.__s_east = None

    def set_north(self, north):
        self.__north = north

    def set_south(self, south):
        self.__south = south

    def set_west(self, west):
        self.__west = west

    def set_east(self, east):
        self.__east = east

    def set_n_west(self, n_west):
        self.__n_west = n_west

    def set_n_east(self, n_east):
        self.__n_east = n_east

    def set_s_west(self, s_west):
        self.__s_west = s_west

    def set_s_east(self, s_east):
        self.__s_east = s_east

    def get_north(self):
        return self.__north

    def get_south(self):
        return  self.__south

    def get_west(self):
        return self.__west

    def get_east(self):
        return self.__east

    def get_n_west(self):
        return self.__n_west

    def get_n_east(self):
        return self.__n_east

    def get_s_east(self):
        return self.__s_east

    def get_s_west(self):
        return self.__s_west

    def get_n_id(self):
        return self.n_id
