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
        return colours[self.colour] + self.number + colours["RESET"]


# Blue cards


class B_1:
    def __init__(self):
        super().__init__("B", 1)


class B_2:
    def __init__(self):
        super().__init__("B", 2)


class B_3:
    def __init__(self):
        super().__init__("B", 3)


class B_4:
    def __init__(self):
        super().__init__("B", 4)


class B_5:
    def __init__(self):
        super().__init__("B", 5)


class B_6:
    def __init__(self):
        super().__init__("B", 6)


class B_7:
    def __init__(self):
        super().__init__("B", 7)


class B_8:
    def __init__(self):
        super().__init__("B", 8)


class B_9:
    def __init__(self):
        super().__init__("B", 9)


# Red cards


class R_1:
    def __init__(self):
        super().__init__("R", 1)


class R_2:
    def __init__(self):
        super().__init__("R", 2)


class R_3:
    def __init__(self):
        super().__init__("R", 3)


class R_4:
    def __init__(self):
        super().__init__("R", 4)


class R_5:
    def __init__(self):
        super().__init__("R", 5)


class R_6:
    def __init__(self):
        super().__init__("R", 6)


class R_7:
    def __init__(self):
        super().__init__("R", 7)


class R_8:
    def __init__(self):
        super().__init__("R", 8)


class R_9:
    def __init__(self):
        super().__init__("R", 9)


# Green cards


class G_1:
    def __init__(self):
        super().__init__("G", 1)


class G_2:
    def __init__(self):
        super().__init__("G", 2)


class G_3:
    def __init__(self):
        super().__init__("G", 3)


class G_4:
    def __init__(self):
        super().__init__("G", 4)


class G_5:
    def __init__(self):
        super().__init__("G", 5)


class G_6:
    def __init__(self):
        super().__init__("G", 6)


class G_7:
    def __init__(self):
        super().__init__("G", 7)


class G_8:
    def __init__(self):
        super().__init__("G", 8)


class G_9:
    def __init__(self):
        super().__init__("G", 9)


# Yellow cards


class Y_1:
    def __init__(self):
        super().__init__("Y", 1)


class Y_2:
    def __init__(self):
        super().__init__("Y", 2)


class Y_3:
    def __init__(self):
        super().__init__("Y", 3)


class Y_4:
    def __init__(self):
        super().__init__("Y", 4)


class Y_5:
    def __init__(self):
        super().__init__("Y", 5)


class Y_6:
    def __init__(self):
        super().__init__("Y", 6)


class Y_7:
    def __init__(self):
        super().__init__("Y", 7)


class Y_8:
    def __init__(self):
        super().__init__("Y", 8)


class Y_9:
    def __init__(self):
        super().__init__("Y", 9)


# Special cards


class R_add_2:
    def __init__(self):
        super().__init__("R", "+2")


class B_add_2:
    def __init__(self):
        super().__init__("B", "+2")


class Y_add_2:
    def __init__(self):
        super().__init__("Y", "+2")


class G_add_2:
    def __init__(self):
        super().__init__("G", "+2")


class add_4:
    def __init__(self):
        super().__init__("RESET", "+4")


class switch_colour:
    def __init__(self):
        super().__init__("RESET", "switch")


class R_change:
    def __init__(self):
        super().__init__("R", "reverse")


class B_change:
    def __init__(self):
        super().__init__("B", "reverse")


class Y_change:
    def __init__(self):
        super().__init__("Y", "reverse")


class G_change:
    def __init__(self):
        super().__init__("G", "reverse")
