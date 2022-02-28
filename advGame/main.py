from enum import Enum
import random

print("We welcome you to this adventure game!\nThis program was made by belain3d")

class Races(Enum):
    KHAJIIT = "Khajiit"
    ARGONIAN = "Argonian"
    WOODELF = "Woodelf"
    DARKELF = "Darkelf"
    HIGHELF = "Highelf"
    BRETON = "Breton"
    IMPERIAL = "Imperial"
    NORD = "Nord"
    ORC = "Orc"
    REDGUARD = "Redguard"

class character:
    def __init__(self, name: str, race: Races, septim = 0) -> None:
        self.name = name
        self.race = race
        self.money = septim
        pass

chrHealth = 100
chrName = False
chrRace = False
chrStarterMoney = False
playerCharacter = False

confirmation = ""
while confirmation != "y":

    
    if confirmation == "n" or playerCharacter == False:
        chrName = input(f"What is your name? ")
        chrRace = input("What race are you? ")
        if chrRace in Races.name:
            pass
        chrStarterMoney = int(input("How much septims do you own? "))
        playerCharacter = character(chrName, chrRace, chrStarterMoney)

        print(f"""
        Your name is: {playerCharacter.name}
        Your race is: {playerCharacter.race}
        You have this much money: {playerCharacter.money}
        """)
        confirmation = str(input("Is this the character you want? y/n"))