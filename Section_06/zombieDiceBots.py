import zombiedice
from random import randint


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
        self.game_turn = 0

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the exact
        # roll information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1, 'rolls': [(
        # 'yellow', 'brains'), ('red', 'footsteps'), ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        self.game_turn += 1

        while diceRollResults is not None:
            # while not diceRollResults:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class RandomZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            if randint(0, 1) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break


class TwoShotZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        self.shotgun = 0
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            self.shotgun += diceRollResults['shotgun']

            if self.shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class TwoBrainZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        self.brains = 0
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            self.brains += diceRollResults['brains']
            if self.brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class D4Zombie:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun = 0
        rolls = randint(1, 4)
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            rolls -= 1
            shotgun += diceRollResults['shotgun']

            if rolls > 0 and shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class MoreGunsThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        shotgun, brains = 0, 0
        # print("Turn")
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            # print(shotgun, "shot", brains, "brains")
            if shotgun < brains:
                diceRollResults = zombiedice.roll()
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name="Random"),
    zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name="Stop at 2 Shotguns", minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name="Stop at 1 Shotgun", minShotguns=1),
    MyZombie(name="My Zombie Bot"),
    RandomZombie(name="Random Zombie"),
    TwoShotZombie(name="Two Shots Zombie"),
    TwoBrainZombie(name="Two Brains Zombie"),
    D4Zombie(name="D4 Zombie"),
    MoreGunsThanBrains(name="More Guns Than Brains Zombie")
    # Add any other zombie players here.
)
# Incomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=10000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
