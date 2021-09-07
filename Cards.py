"""
Python-Uno/Cards.py

This script contains classes for all the Uno cards,
these will be used by Python-Uno/Main.py.

Author: Nathan "Nathcat" Baines
Date: 06/09/2021
"""


colours = {
    "B": "\u001b[34m",
    "R": "\u001b[31m",
    "Y": "\u001b[33m",
    "G": "\u001b[32m",
    "RESET": "\u001b[0m"
}


class Card:  # Card parent class
    def __init__(self, colour, number):
        self.colour = colour
        self.number = number

    def __str__(self):
        return colours[self.colour] + str(self.number) + colours["RESET"]

    def __eq__(self, other):
        return (other.colour == self.colour) and (other.number == self.number)


# Blue cards


class B_0(Card):
    def __init__(self):
        super().__init__("B", 0)


class B_1(Card):
    def __init__(self):
        super().__init__("B", 1)


class B_2(Card):
    def __init__(self):
        super().__init__("B", 2)


class B_3(Card):
    def __init__(self):
        super().__init__("B", 3)


class B_4(Card):
    def __init__(self):
        super().__init__("B", 4)


class B_5(Card):
    def __init__(self):
        super().__init__("B", 5)


class B_6(Card):
    def __init__(self):
        super().__init__("B", 6)


class B_7(Card):
    def __init__(self):
        super().__init__("B", 7)


class B_8(Card):
    def __init__(self):
        super().__init__("B", 8)


class B_9(Card):
    def __init__(self):
        super().__init__("B", 9)


# Red cards


class R_0(Card):
    def __init__(self):
        super().__init__("R", 0)


class R_1(Card):
    def __init__(self):
        super().__init__("R", 1)


class R_2(Card):
    def __init__(self):
        super().__init__("R", 2)


class R_3(Card):
    def __init__(self):
        super().__init__("R", 3)


class R_4(Card):
    def __init__(self):
        super().__init__("R", 4)


class R_5(Card):
    def __init__(self):
        super().__init__("R", 5)


class R_6(Card):
    def __init__(self):
        super().__init__("R", 6)


class R_7(Card):
    def __init__(self):
        super().__init__("R", 7)


class R_8(Card):
    def __init__(self):
        super().__init__("R", 8)


class R_9(Card):
    def __init__(self):
        super().__init__("R", 9)


# Green cards


class G_0(Card):
    def __init__(self):
        super().__init__("G", 0)


class G_1(Card):
    def __init__(self):
        super().__init__("G", 1)


class G_2(Card):
    def __init__(self):
        super().__init__("G", 2)


class G_3(Card):
    def __init__(self):
        super().__init__("G", 3)


class G_4(Card):
    def __init__(self):
        super().__init__("G", 4)


class G_5(Card):
    def __init__(self):
        super().__init__("G", 5)


class G_6(Card):
    def __init__(self):
        super().__init__("G", 6)


class G_7(Card):
    def __init__(self):
        super().__init__("G", 7)


class G_8(Card):
    def __init__(self):
        super().__init__("G", 8)


class G_9(Card):
    def __init__(self):
        super().__init__("G", 9)


# Yellow cards


class Y_0(Card):
    def __init__(self):
        super().__init__("Y", 0)


class Y_1(Card):
    def __init__(self):
        super().__init__("Y", 1)


class Y_2(Card):
    def __init__(self):
        super().__init__("Y", 2)


class Y_3(Card):
    def __init__(self):
        super().__init__("Y", 3)


class Y_4(Card):
    def __init__(self):
        super().__init__("Y", 4)


class Y_5(Card):
    def __init__(self):
        super().__init__("Y", 5)


class Y_6(Card):
    def __init__(self):
        super().__init__("Y", 6)


class Y_7(Card):
    def __init__(self):
        super().__init__("Y", 7)


class Y_8(Card):
    def __init__(self):
        super().__init__("Y", 8)


class Y_9(Card):
    def __init__(self):
        super().__init__("Y", 9)


# Special cards


class R_add_2(Card):
    def __init__(self):
        super().__init__("R", "+2")


class B_add_2(Card):
    def __init__(self):
        super().__init__("B", "+2")


class Y_add_2(Card):
    def __init__(self):
        super().__init__("Y", "+2")


class G_add_2(Card):
    def __init__(self):
        super().__init__("G", "+2")


class add_4(Card):
    def __init__(self):
        super().__init__("RESET", "+4")


class switch_colour(Card):
    def __init__(self):
        super().__init__("RESET", "switch")


class R_reverse(Card):
    def __init__(self):
        super().__init__("R", "reverse")


class B_reverse(Card):
    def __init__(self):
        super().__init__("B", "reverse")


class Y_reverse(Card):
    def __init__(self):
        super().__init__("Y", "reverse")


class G_reverse(Card):
    def __init__(self):
        super().__init__("G", "reverse")


class R_skip(Card):
    def __init__(self):
        super().__init__("R", "skip")


class B_skip(Card):
    def __init__(self):
        super().__init__("B", "skip")


class G_skip(Card):
    def __init__(self):
        super().__init__("G", "skip")


class Y_skip(Card):
    def __init__(self):
        super().__init__("Y", "skip")


# Static functions


def generate_deck():  # Generates a full deck of all cards
    return [
        B_0(),
        B_1(),
        B_2(),
        B_3(),
        B_4(),
        B_5(),
        B_6(),
        B_7(),
        B_8(),
        B_9(),
        B_add_2(),
        B_reverse(),
        B_skip(),

        R_0(),
        R_1(),
        R_2(),
        R_3(),
        R_4(),
        R_5(),
        R_6(),
        R_7(),
        R_8(),
        R_9(),
        R_add_2(),
        R_reverse(),
        R_skip(),

        G_0(),
        G_1(),
        G_2(),
        G_3(),
        G_4(),
        G_5(),
        G_6(),
        G_7(),
        G_8(),
        G_9(),
        G_add_2(),
        G_reverse(),
        G_skip(),

        Y_0(),
        Y_1(),
        Y_2(),
        Y_3(),
        Y_4(),
        Y_5(),
        Y_6(),
        Y_7(),
        Y_8(),
        Y_9(),
        Y_add_2(),
        Y_reverse(),
        Y_skip(),

        add_4(),
        add_4(),
        switch_colour(),
        switch_colour()
    ]
