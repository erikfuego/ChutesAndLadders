"""
Created on 4/24/2020

@author: erosales

Description of file: 
"""
from random import randint


class Player(object):

    def __init__(self, name, turn=0, position=0):

        self.name = name
        self.turn = turn
        self.position = position

    def spin(self):
        return randint(1, 6)