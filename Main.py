"""
Python-Uno/Main.py

This is the main game script for Uno in Python.

Author: Nathan "Nathcat" Baines
Date: 06/09/2021
"""


from Cards import *
import random
import sys


class TurnCounter:  # Object to track which player's turn it is
    def __init__(self, number_of_players):
        self.turn = 0
        self.__direction = 1  # Represents the direction of play
        self.__number_of_players = number_of_players - 1

    def next_turn(self):  # Move to the next player's turn
        self.turn += self.__direction

        if self.turn > self.__number_of_players:
            self.turn = 0

        elif self.turn < 0:
            self.turn = self.__number_of_players

    def change_direction(self):  # Toggle the direction of play
        if self.__direction == 1:
            self.__direction = -1
        else:
            self.__direction = 1


def generate_player_deck():  # Generate a random player deck
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


def can_play(card):  # Check if the parameter card can be played
    top_card = cards_played[-1]

    if card.colour == "RESET":  # Represents a black card, which can always be played
        return True
    else:
        return (top_card.colour == card.colour) or (top_card.number == card.number)


def choose_colour():  # Function to choose a colour, used when the +4 and colour switch cards are played
    c = {
        1: "B",
        2: "R",
        3: "G",
        4: "Y"
    }

    choice = None

    while choice not in list(c.keys()):
        choice = int(input("\n\nChoose a new colour:\n1. Blue\n2. Red\n3. Green\n4. Yellow\n\nEnter the number corresponding to your choice > "))

    return c[choice]


def check_for_win():  # Check if any player has won, if they have, exit the program
    for x in range(0, len(player_decks)):
        if len(player_decks[x]) == 0:
            print(f"\n\n\n\n\nPlayer {x} has won! Congrats! :)")
            sys.exit()


if __name__ == "__main__":
    deck = generate_deck()  # Get the full game deck

    number_of_players = int(input("How many players? > "))  # Get the number of players

    player_decks = [generate_player_deck() for i in range(number_of_players)]  # Generate decks for each player

    turn_counter = TurnCounter(number_of_players)  # Create the turn counter

    cards_played = [deck[0]]  # Add a card to the pile to start the game
    del deck[0]

    while True:  # Main game loop
        check_for_win()  # Check if a player has won

        print(f"\n--------------------\nIt's player {turn_counter.turn}'s turn!\n\n")

        print(str(cards_played[-1]) + '\n\n')  # Print the card at the top of the pile

        for card in player_decks[turn_counter.turn]:  # Print the player's deck
            print(str(card) + ", ", end="")

        while True:  # Enter command loop, will loop until the player enters a valid command
            command = input("\n\nEnter action > ").split(" ")

            if command[0] == "take":  # The player wants to take a card from the deck
                player_decks[turn_counter.turn].append(deck[0])
                del deck[0]
                turn_counter.next_turn()
                break

            elif command[0] == "play":  # The player wants to play a card, the index of the card they want to play is command[1]
                if can_play(player_decks[turn_counter.turn][int(command[1])]):  # Check if the chosen card can be played

                    if player_decks[turn_counter.turn][int(command[1])].number == "+2":  # If it's a +2 card, add 2 cards to the next player's deck
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]
                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]

                    elif player_decks[turn_counter.turn][int(command[1])].number == "+4":  # If it's a +4 card, add 4 cards to the next player's deck and choose a new colour
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]
                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]
                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]
                        player_decks[turn_counter.turn].append(deck[0])
                        del deck[0]

                        cards_played[-1].colour = choose_colour()

                    elif player_decks[turn_counter.turn][int(command[1])].number == "switch":  # If it's a colour switch card, choose a new colour
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                        cards_played[-1].colour = choose_colour()

                    elif player_decks[turn_counter.turn][int(command[1])].number == "reverse":  # If it's a reverse card, change the direction of play
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]

                        turn_counter.change_direction()
                        turn_counter.next_turn()

                    elif player_decks[turn_counter.turn][int(command[1])].number == "skip":  # If it's a skip card, skip the next player's turn
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]

                        turn_counter.next_turn()
                        turn_counter.next_turn()

                    else:  # If it's any other card, play the card and make no other action
                        cards_played.append(player_decks[turn_counter.turn][int(command[1])])
                        del player_decks[turn_counter.turn][int(command[1])]
                        turn_counter.next_turn()

                    break

                else:
                    print("You can't play that card here!")

            elif command[0] == "quit":  # Quit the game
                choice = None
                while choice not in ["y", "n"]:  # Ask if the player is sure they want to quit
                    choice = input("Are you sure? (y/n) > ").lower()

                    if choice not in ['y', 'n']:
                        print("That's not an option!")

                if choice == 'y':  # If they are sure, exit the program
                    sys.exit()

            else:  # Handle invalid commands
                print(f"Invalid command '{command[0]}'")
