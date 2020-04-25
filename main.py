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

# total_players = dict()
#
# first_spins = []

for i in range(1, int(players)+1):
    player = create_player(i)

sort_players()
# print("Hello World")
#
#     player_name = input("\nPlayer %s, what is your name: " % i)
#     print("\n%s, please spin to determine the order of players." % player_name)
#     spin = input("\nType in \"SPIN\" and press ENTER: ")
#
#     if spin == 'SPIN':
#         turn = Spin()
#         print("\n%s, you spun a %s." % (player_name, turn))
#
#         if turn not in total_players.keys():
#             total_players[turn] = Player(name=player_name, turn=turn)
#             first_spins.append(int(turn))
#         else:
#             temp = turn
#             while temp in total_players.keys():
#                 turn = int(turn) - 1
#                 if turn not in total_players.keys():
#                     total_players[turn] = Player(name=player_name, turn=str(turn))
#                     first_spins.append(int(turn))
#                     break

# for i in sorted(first_spins):
#     SORTED_PLAYERS.insert(0, total_players[i])
#
# VALUES = {
#     1: 'First',
#     2: 'Second',
#     3: 'Third',
#     4: 'Fourth'
# }
#
# for index, player in enumerate(SORTED_PLAYERS):
#     player.turn = VALUES[index+1]
#     print(f"\n{player.name} is {VALUES[index+1]}!")

game = PlayGame(players=sorted_players)

game.run()

