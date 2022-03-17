# Text-Based RPG made by belain3d. Git Repo on https://github.com/belain3d/Fun-Projects/blob/master/Text-Based%20RPG/main.py #
from enum import Enum
from rpg_getters import *
from rpg_setters import *

class Races(Enum):
    ALTMER = "altmer"
    ARGONIAN = "argonian"
    BOSMER = "bosmer"
    BRETON = "breton"
    DUNMER = "dunmer"
    IMPERIAL = "imperial"
    KHAJIIT = "khajiit"
    NORD = "nord"
    ORC = "orc"
    REDGUARD = "redguard"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

# Player Class

class Player:
    def __init__(self, pName, pRace: Races, pHealth=100, pArmorRate=10, pMagicka=100, pStamina=100, pAttack=12, pInvWeight=130):
        self.name = pName
        if not Races.has_value(pRace):
            print(f"RaceError: Race '{pRace}' is not a valid race.")
        self.race = pRace
        self.health = pHealth
        self.armorRate = pArmorRate
        self.magicka = pMagicka
        self.stamina = pStamina
        self.attack = pAttack
        self.inventory = pInvWeight
 

confirmation = ""
while confirmation != "y":
    inputName = input("What is your name? ")

    for i in Races:
        print(i.value, end=" ")

    inputRace = input("\nWhat race are you? ")
    plr = Player(inputName, inputRace.lower())
    print(f"""
    Your character's name: {plr.name}
    Your character's race: {plr.race}
    Your character's health: {plr.health}
    Your character's stamina: {plr.stamina}
    Your character's magicka: {plr.magicka}
    Your character's carry weight: {plr.inventory}
    """)
    confirmation = input("Are you sure this is the character you wanted? (y/n)")
