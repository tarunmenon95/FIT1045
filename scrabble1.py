import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7  and TILES_USED < len(Tiles):
        myTiles.append(Tiles[TILES_USED])
        TILES_USED += 1


# prints tiles and their scores
def printTiles(myTiles):
    tiles = ""
    scores = ""
    for letter in myTiles:
        tiles += letter + "  "
        thisScore = getScore(letter)
        if thisScore > 9:
            scores += str(thisScore) + " "
        else:
            scores += str(thisScore) + "  "

    print("\nTiles : " + tiles)
    print("Scores: " + scores)

# gets the score of a letter
def getScore(letter):
    for item in Scores:
        if item[0] == letter:
            return item[1]



scoresFile = open('scores.txt')
tilesFile = open('tiles.txt')

# read scores from scores.txt and insert in the list Scores
Scores = []
for line in scoresFile:
    line = line.split()
    letter = line[0]
    score = int(line[1])
    Scores.append([letter,score])
scoresFile.close()

# read tiles from tiles.txt and insert in the list Tiles
Tiles = []
for line in tilesFile:
    line= line.strip()
    Tiles.append(line)
tilesFile.close()

# decide whether to return random tiles
rand = input("Do you want to use random tiles (enter Y or N): ")
if rand == "Y":
    SHUFFLE = True
else:
    if rand != "N":
        print("You did not enter Y or N. Therefore, I am taking it as a Yes :P.")
        SHUFFLE = True
        
if SHUFFLE:
    random.shuffle(Tiles)


myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################

#########Create Dictionary List#############

with open("dictionary.txt", "r+") as d:
    dic = d.readlines()
d.close()

dic = [i.strip('\n') for i in dic]

############################################




#Word checker

def checkWord(w):
    if w.isalpha() == True:
        return True


def checkDict(w):
    for i in dic:
        if w.lower() == i.lower():
            return True





def checkTiles(w):
    count = 0
    wordLength = len(w)
    tiles = myTiles[:]
    t = False

    for j in range(len(w)):
        if wordLength == 0:
            tiles = myTiles[:]
        for i in range(len(myTiles)):
            if (w[count]).upper() == tiles[i]:
                tiles.append("")
                tiles.pop(i)
                wordLength -= 1
                count += 1
            if wordLength == 0:
                return True



###



wordValid = False

while wordValid == False:

    word = input("Enter your word here: ")

    if checkWord(word) == True:

        if checkDict(word) == True:

            if checkTiles(word) == True:
                print("Cool, this is a valid word\n")
                wordValid = True
            else:
                print("This word cannot be made using the tiles\n")

        else:
            print("I have never heard of this word\n")
    else:
        print ("Only use English Letters\n")













