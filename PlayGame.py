"""
Created on 4/25/2020

@author: erosales

Description of file: 
"""
from Board import EVENTS, BOARD
from Spin import Spin


class PlayGame(object):

    def __init__(self, players):

        self.players = players

    def run(self):

        running = True

        while running:
            for player in self.players:
                print("\n%s, it's your turn! Your current position is %s." % (player.name, player.position))
                value = input("\nPlease type in \"SPIN\" and press ENTER: ")
                if value == 'SPIN':
                    spin = Spin()
                    player.position += int(spin)
                    print(f"\nYou spun a {spin}! You moved up {spin} spaces to {player.position}.")
                    board = BOARD[player.position]
                    event = EVENTS[board[1]]
                    player.position = board[0]
                    print(event % player.position)
