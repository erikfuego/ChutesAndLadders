"""
Created on 4/25/2020

@author: erosales

Description of file: 
"""
from create_player import total_players, first_spins

sorted_players = []

def sort_players():
    for i in sorted(first_spins):
        sorted_players.insert(0, total_players[i])

    VALUES = {
        1: 'First',
        2: 'Second',
        3: 'Third',
        4: 'Fourth'
    }

    for index, player in enumerate(sorted_players):
        player.turn = VALUES[index + 1]
        print(f"\n{player.name} is {VALUES[index + 1]}!")