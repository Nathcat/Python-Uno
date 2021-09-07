"""
Python-Uno/Main.py

This is the main game script for Uno in Python.

Author: Nathan "Nathcat" Baines
Date: 06/09/2021
"""


# TODO: Make sure that black cards can always be played, ie bypass can_play check

from Cards import *
import random


class TurnCounter:
    def __init__(self, number_of_players):
        self.turn = 0
        self.__direction = 1
        self.__number_of_players = number_of_players - 1

    def next_turn(self):
        self.turn += self.__direction

        if self.turn > self.__number_of_players:
            self.turn = 1

    def change_direction(self):
        if self.__direction == 1:
            self.__direction = -1
        else:
            self.__direction = 1


def generate_player_deck():
    player = []
    while len(player) != 7:
        choice = None
        index = None
        while choice is None or choice in player:
            index = random.randint(0, len(deck))
            choice = deck[index]

        player.append(choice)
        del deck[index]

    return player


def can_play(card):
    top_card = cards_played[-1]

    return (top_card.colour == card.colour) or (top_card.number == card.number)


if __name__ == "__main__":
    deck = generate_deck()  # Get the full game deck

    number_of_players = int(input("How many players? > "))  # Get the number of players

    player_decks = [generate_player_deck() for i in range(number_of_players)]  # Generate decks for each player

    turn_counter = TurnCounter(number_of_players)  # Create the turn counter

    cards_played = [deck[0]]
    del deck[0]

    while True:
        print(f"\n--------------------\nIt's player {turn_counter.turn}'s turn!\n\n")

        print(str(cards_played[-1]) + '\n\n')


        for card in player_decks[turn_counter.turn]:
            print(str(card) + ", ", end="")

        while True:
            command = input("\n\nEnter action > ").split(" ")

            if command[0] == "take":
                player_decks[turn_counter.turn].append(deck[0])
                del deck[0]
                turn_counter.next_turn()
                break

            elif command[0] == "play":
                if can_play(player_decks[turn_counter.turn][int(command[1])]):

                    if player_decks[turn_counter.turn][int(command[1])].number == "+2":
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]
                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]

                    elif player_decks[turn_counter.turn][int(command[1])].number == "reverse":
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]

                        turn_counter.change_direction()
                        turn_counter.next_turn()

                    elif player_decks[turn_counter.turn][int(command[1])].number == "skip":
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]

                        turn_counter.next_turn()
                        turn_counter.next_turn()

                    else:
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                    break

            else:
                print(f"Invalid command '{command[0]}'")
