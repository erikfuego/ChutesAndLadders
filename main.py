"""
Created on 4/24/2020

@author: erosales

Description of file:
"""
from create_player import create_player
from play_game import PlayGame
from sort_players import sorted_players, sort_players

print(
"""
Welcome to Chutes And Ladders!
""")

players = input("How many people will be playing (1-4): ")

print("\nOkay! %s players will be playing." % players)

for i in range(1, int(players)+1):
    player = create_player(i)

sort_players()

game = PlayGame(players=sorted_players)

game.run()

