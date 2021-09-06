"""
Python-Uno/Main.py

This is the main game script for Uno in Python.

Author: Nathan "Nathcat" Baines
Date: 06/09/2021
"""


from Cards import *
import random


if __name__ == "__main__":
    player_1_deck = []
    player_2_deck = []

    deck = generate_deck()
