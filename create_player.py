"""
Created on 4/25/2020

@author: erosales

Description of file: 
"""
from clear_log import clear
from player import Player
# from main import total_players, first_spins

total_players = dict()

first_spins = []

def create_player(player_number):

        player_name = input("\nPlayer %s, what is your name: " % player_number)
        clear()
        _spin(player_name)

def _spin(player_name):
    print("\n%s, please spin to determine the order of players." % player_name)
    spin = input("\nType in \"SPIN\" and press ENTER: ")
    clear()

    if spin == 'SPIN':

        temp_player = Player(name=player_name)

        turn = temp_player.spin()

        print("\n%s, you spun a %s." % (player_name, turn))

        if turn not in total_players.keys():
            temp_player.turn = turn
            total_players[turn] = temp_player
            first_spins.append(int(turn))
        else:
            temp = turn
            while temp in total_players.keys():
                turn = int(turn) - 1
                if turn not in total_players.keys():
                    total_players[turn] = Player(name=player_name, turn=str(turn))
                    first_spins.append(int(turn))
                    break
    else:
        print("\nWhoops! you typed in \"%s\"." % spin)
        _spin(player_name)