"""
Created on 4/24/2020

@author: erosales

Description of file: 
"""

class Player(object):

    def __init__(self, name, turn, position=None):

        self.name = name
        self.turn = turn
        self.position = position
