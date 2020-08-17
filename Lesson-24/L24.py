class Animal:
    def breath(self):
        print("Yes I'm breathing!")
class Terrestrial(Animal):
    def walkOnEarth(self):
        print("I am walking now...")
    def stayInWater(self):
        print("I cannot live in Water!")
class Aquatic(Animal):
    def stayInWater(self):
        print("I live in water...")
    def walkOnEarth(self):
        print("I cannot live on earth")
class Amphibian(Terrestrial,Aquatic):
    def walkOnEarth(self):
        Terrestrial.walkOnEarth(self)
        print("I love to walk!")
    def stayInWater(self):
        Aquatic.stayInWater(self)

## Main Program ##
# help(Amphibian)
myTurtle=Amphibian()
myTurtle.breath()
myTurtle.walkOnEarth()
myTurtle.stayInWater()


# myDog=Terrestrial()
# myDog.breath()
# myDog.walkOnEarth()
# myFish=Aquatic()
# myFish.breath()
# myFish.stayInWater()
# myFish.walkOnEarth()
