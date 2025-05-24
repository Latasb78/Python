# ZombieDiceBots.py
print("Name:Lata.S.B",
       "USN:1AY24AI060",
       "Section:'O'")
import zombiedice

class CautiousBot:
    """Stops after getting 1 brain"""
    def _init_(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roller = zombiedice.roll()  # First roll
        brains = 0

        while dice_roller is not None:
            for die in dice_roller:
                if die['brain']:
                    brains += 1
            if brains >= 1:
                break  # Stop after 1 brain
            dice_roller = zombiedice.roll()  # Roll again

class RiskyBot:
    """Keeps rolling until 2 shotguns"""
    def _init_(self, name):
        self.name = name

    def turn(self, game_state):
        shotguns = 0
        dice_roller = zombiedice.roll()
        
        while dice_roller is not None:
            for die in dice_roller:
                if die['shotgun']:
                    shotguns += 1
            if shotguns >= 2:
                break  # Too dangerous
            dice_roller = zombiedice.roll()