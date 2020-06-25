import random
class Dice:
    def __init__(self):
        self.__sideUp=1
    def roll(self):
        self.__sideUp=random.randint(1,6)
    def __str__(self):
        return str(self.__sideUp)

## Main Program ##
myDice=Dice()

for i in range(5):
    myDice.roll()
    myDice._Dice__sideUp=6
    print(myDice)
