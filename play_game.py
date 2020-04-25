"""
Created on 4/25/2020

@author: erosales

Description of file: 
"""
from board import EVENTS, BOARD

class PlayGame(object):

    def __init__(self, players):

        self.players = players

    def run(self):

        running = True

        while running:
            for player in self.players:
                value = self._spin(player)
                if value == 'SPIN':
                    spin = player.spin()
                    self._valid_spin(player, spin)
                else:
                    print("\nWhoops! you typed in \"%s\"." % value)
                    value = self._spin(player)
                    while value != 'SPIN':
                        print("\nWhoops! you typed in \"%s\"." % value)
                        value = self._spin(player)
                    spin = player.spin()
                    self._valid_spin(player, spin)

    def _spin(self, player):
        print("\n%s, it's your turn! Your current position is %s." % (player.name, player.position))
        value = input("\nPlease type in \"SPIN\" and press ENTER: ")
        return value

    def _valid_spin(self, player, spin):
        if not (player.position + int(spin)) > 100:
            player.position += int(spin)
            print(f"\nYou spun a {spin}! You moved up {spin} spaces to {player.position}.")
            board = BOARD[player.position]
            event = EVENTS[board[1]]
            player.position = board[0]
            print(event % player.position)
            if player.position == 100:
                print(f"\n{(player.name).upper()} HAS WON THE GAME!!!")
                print("\nThanks for playing!")
                exit()
        else:
            print(f"\nYou spun a {spin}!")
            print(f"You need a {100 - player.position} to win the game or lower to move spaces.")