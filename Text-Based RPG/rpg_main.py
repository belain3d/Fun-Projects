# Text-Based RPG made by belain3d. Git Repo on https://github.com/belain3d/Fun-Projects/blob/master/Text-Based%20RPG/main.py #
from enum import Enum
from rpg_getters import *
from rpg_setters import *
import random

class Races(Enum):
    IMPOSTOR = "impostor"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

# Player Class

class Player:
    def __init__(self, pName, pRace: Races, pHealth=100, pArmorRate=10, pMagicka=100, pStamina=100, pAttack=12, pInvWeight=130):
        self.name = pName
        if not Races.has_value(pRace):
            raise ValueError(f"{pRace} is not a valid race")
        self.race = pRace
        self.health = pHealth
        self.armorRate = pArmorRate
        self.magicka = pMagicka
        self.stamina = pStamina
        self.attack = pAttack
        self.inventory = pInvWeight

inputName = input("Your name? ")
inputRace = input("Race? ")

plr = Player(inputName, inputRace.lower())