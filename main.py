"""
Created on 4/24/2020

@author: erosales

Description of file:
"""
from FirstRoll import FirstRoll
from Player import Player

print(
"""
Welcome to Chutes And Ladders!
""")

players = input("How many people will be playing (1-4): ")

print("\nOkay! %s players will be playing." % players)

PLAYERS = dict()

FIRST_ROLLS = []

for i in range(1, int(players)+1):

    player_name = input("\nPlayer %s, what is your name: " % i)
    print("\n%s, please spin to determine the order of players." % player_name)
    spin = input("\nType in \"SPIN\" and press ENTER: ")

    if spin == 'SPIN':
        turn = FirstRoll()
        print("\n%s, you spun a %s." % (player_name, turn))

        if turn not in PLAYERS.keys():
            PLAYERS[turn] = Player(name=player_name, turn=turn)
            FIRST_ROLLS.append(int(turn))
        else:
            temp = turn
            while temp in PLAYERS.keys():
                turn = int(turn) - 1
                if turn not in PLAYERS.keys():
                    PLAYERS[turn] = Player(name=player_name, turn=str(turn))
                    FIRST_ROLLS.append(int(turn))
                    break

SORTED_PLAYERS = []

for i in sorted(FIRST_ROLLS):
    SORTED_PLAYERS.insert(0, PLAYERS[i])

VALUES = {
    1: 'First',
    2: 'Second',
    3: 'Third',
    4: 'Fourth'
}

for index, player in enumerate(SORTED_PLAYERS):
    player.turn = VALUES[index+1]
    print(f"\n{player.name} is {VALUES[index+1]}!")
