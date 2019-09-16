from enum import Enum
import random


# Direction Enum used to check the different direction of line winner
class Picture(Enum):
    dobble = 0
    clown = 1
    yinyang = 2
    babybottle = 3
    cat = 4
    Scissors = 5
    flower = 6
    leaf = 7
    dragon = 8
    clock = 9
    drop = 10
    hammer = 11
    igloo = 12
    ghost = 13
    bomb = 14
    stain =15
    musicnote = 16
    spider = 17
    fire = 18
    Carrot = 19
    body = 20
    skelton = 21
    sun = 22
    NoEntry = 23
    Turtle = 24
    crayon = 25
    exclamationsign = 26
    questionsign = 27
    leafred= 28
    cheese = 29
    Bird = 30
    Cible = 31
    Glasses = 32
    cactus = 33
    Eye =34
    Clock = 35
    lamp = 36
    flange = 37
    Car = 38
    freeze = 39

class clsGame:
    # constructor of Game , initialize the local variables
    # Matrixarray is multiple array of list [[],[],[]]
    # FreePlaces is the list of the free place in the array , needed for computer player whitch choose his random number in this list
    def __init__(self):
        self.Card = []

    # initialize the matrix according to the size of matrix from the configuration
    def InitMatrix(self):
        PictureCount = 0
        while PictureCount < 9 :
            randomPicture = self.GetRandomFreePlace()
            if randomPicture not in self.Card:
                self.Card.append(randomPicture)
                PictureCount += 1

    def GetCard(self):
        return self.Card

    def PrintCard(self):
        print (self.Card)

    # Return a couple of position x,y get from freeplace array , when the position in the list is get by random function
    def GetRandomFreePlace(self):
        x= random.randint(1,len(Picture)- 1)
        return Picture(x -1).name



