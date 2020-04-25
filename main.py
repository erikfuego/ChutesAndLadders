"""
Created on 4/24/2020

@author: erosales

Description of file:
"""
from clear_log import clear
from create_player import create_player
from play_game import PlayGame
from sort_players import sorted_players, sort_players

print(
"""
Welcome to Chutes And Ladders!
""")

valid_players = ['1', '2', '3', '4']

def _players():
    players = input("How many people will be playing (1-4): ")
    clear()
    return players


players = _players()

while players not in valid_players:
    print("\nThe value \"%s\" is invalid. Please try again." % players)
    players = _players()

print("\nOkay! %s players will be playing." % players)

for i in range(1, int(players)+1):
    player = create_player(i)

sort_players()

game = PlayGame(players=sorted_players)

game.run()

