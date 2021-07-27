from sys import stdin
import math
import sys
import random


TILES_USED = 0 # records how many tiles have been returned to user
CELL_WIDTH = 3 # cell width of the scrabble board
SHUFFLE = False # records whether to shuffle the tiles or not

# inserts tiles into myTiles
def getTiles(myTiles):
    global TILES_USED
    while len(myTiles) < 7 and TILES_USED < len(Tiles):
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

# initialize n x n Board with empty strings
def initializeBoard(n):
    Board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append("")
        Board.append(row)

    return Board

# put character t before and after the string s such that the total length
# of the string s is CELL_WIDTH.
def getString(s,t):
    global CELL_WIDTH
    s = str(s)
    rem = CELL_WIDTH - len(s)
    rem = rem//2
    s = t*rem + s
    rem = CELL_WIDTH - len(s)
    s = s + t*rem
    return s

# print the Board on screen
def printBoard(Board):
    global CELL_WIDTH
    print("\nBoard:")
    spaces = CELL_WIDTH*" "
    board_str =  "  |" + "|".join(getString(item," ") for item in range(len(Board)))  +"|"
    line1 = "--|" + "|".join(getString("","-") for item in range(len(Board)))  +"|"

 
    print(board_str)
    print(line1)
    
    for i in range(len(Board)):
        row = str(i) + " "*(2-len(str(i))) +"|"
        for j in range(len(Board)):
            row += getString(Board[i][j]," ") + "|"
        print(row)
        print(line1)
        
    print()

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


validBoardSize = False
while not validBoardSize:
    BOARD_SIZE = input("Enter board size (a number between 5 to 15): ")
    if BOARD_SIZE.isdigit():
        BOARD_SIZE = int(BOARD_SIZE)
        if BOARD_SIZE >= 5 and BOARD_SIZE <= 15:
            validBoardSize = True
        else:
            print("Your number is not within the range.\n")
    else:
        print("Are you a little tipsy? I asked you to enter a number.\n")


Board = initializeBoard(BOARD_SIZE)
printBoard(Board)

myTiles = []
getTiles(myTiles)
printTiles(myTiles)

########################################################################
# Write your code below this
########################################################################


with open("dictionary.txt", "r+") as d:
    dic = d.readlines()
d.close()

dic = [i.strip('\n') for i in dic]

def checkWord(word):
    wordCount = len(word)

    for i in range(len(word)):
        if word[i].isalpha():
            wordCount = wordCount - 1
            if wordCount == 0:
                return True

def checkDict(word, boardSize, rowVal, colVal, direction):

    tempWord = word

    for i in dic:
        if tempWord.upper() == i.upper():
            return True



def checkTiles(word, boardSize, rowVal, colVal, direction):
    count = 0
    wordLength = len(word)
    tiles = myTiles[:]

    for j in range(len(word)):
        if wordLength == 0:
            tiles = myTiles[:]
        for i in range(len(myTiles)):
            if (word[count]).upper() == tiles[i]:
                tiles.append("")
                tiles.pop(i)
                wordLength -= 1
                count += 1
            if wordLength == 0:
                return True

            if (word[count]).upper() != tiles[i]:
                if direction == "V":
                    for k in range(rowVal + len(word) - 1, boardSize):
                        if Board[k][colVal] == "":
                            break
                        if Board[k][colVal] == word[count].upper():
                            wordLength -=1
                        if Board[rowVal][colVal] == word[count].upper():
                            wordLength -=1

                if direction == "H":
                    for y in range(colVal + len(word) - 1, boardSize):
                        if Board[rowVal][y] == "":
                            break
                        if Board[rowVal][y] == word[count].upper():
                            wordLength -=1
                        if Board[rowVal][colVal] == word[count].upper():
                            wordLength -=1

def checkBoardTiles(word, rowVal, colVal, direction, boardSize):

    wordLength = len(word)
    count  = 0
    countEmp = 0

    if (direction == "V"):
        if (rowVal + len(word) <= boardSize):
            for i in range(wordLength):
                if Board[rowVal + i][colVal] == word[i]:
                    count += 1
                if Board[rowVal + i][colVal] == "":
                    countEmp += 1;


            if (count >= 1 and (count + countEmp == wordLength)):
                return True

            else:
                return False


    if (direction == "H"):
        if (colVal + len(word) <= boardSize):
            for i in range(wordLength):
                if Board[rowVal][colVal + i] == word[i]:
                    count += 1
                if Board[rowVal][colVal + i] == "":
                    countEmp += 1;

            if (count >= 1 and (count + countEmp == wordLength)):
                return True

            else:
                return False

def removeTiles(word):

    count = 0
    wordLength = len(word)
    tiles = myTiles[:]

    for j in range(len(word)):
        for i in range(len(myTiles)):
            if word[count] == tiles[i]:
                tiles.append("")
                tiles.pop(i)
                count += 1
                wordLength -= 1
            if wordLength == 0:
                myTiles[:] = [item for item in tiles if item != '']
                return

def firstMove(word, rowVal, colVal, boardSize):

    if (col == int(bSize // 2) and row == int(bSize // 2)):

        if checkDict(word, boardSize, rowVal, colVal, orient):
            if checkTiles(word, boardSize, rowVal, colVal, orient):
                if (orient == "V"):
                    if (colVal + len(word) <= boardSize):
                        for i in range(len(word)):
                            Board[int(bSize // 2 + i)][int(bSize // 2)] = word[i]

                        printBoard(Board)
                        return True
                    else:
                        print("invlad move 10")
                        return False


                elif (orient == "H"):
                    if (rowVal + len(word) <= boardSize):
                        for i in range(len(word)):
                            Board[int(bSize // 2)][int(bSize // 2 + i)] = word[i]
                        printBoard(Board)
                        return True
                    else:
                        print("invl move 11")
                        return False

                else:
                    print("Invalid move8")
                    return False


            else:
                print("Invalid Move 2")
                return False

        else:
            print("Invalid Move 1")
            return False
    else:
        print("Invalid Move 5")
        return False

def otherMoves(word, rowVal, colVal, boardSize, direction):

    if checkDict(word, boardSize, rowVal, colVal, direction):
        if checkTiles(word, boardSize, rowVal, colVal, direction):
            if checkBoardTiles(word, rowVal, colVal, direction, boardSize):
                if (orient == "V"):
                    if(rowVal + len(word) <= boardSize): ###
                        for i in range(len(word)):
                            if (Board[row + i][col] == ""):
                                Board[row + i][col] = word[i]

                        printBoard(Board)
                        return True

                    else:
                        print("Invladi mov 9")
                        return False


                elif (orient == "H"):
                    if(colVal + len(word) <= boardSize):
                        for i in range(len(word)):
                            Board[row][col + i] = word[i]

                        printBoard(Board)
                        return True


                    else:
                        print("invl move 10")
                        return False

                else:
                    print("Invalid move7")
                    return False

            else:
                print("invlad move 22")
                return False
        else:
            print("Invalid Move 3")
            return False
    else:
        print("Invlaid Move 4")
        return False


count = 0
game = True


while (game):


    word = input("Enter your word: ").upper()

    location = input("Enter the location in row:col:direction")
    location = location.split(":")
    bSize = len(Board)

    row = int(location[0])
    col = int(location[1])
    orient = location[2]


    if count != 0:

        if otherMoves(word, row, col, bSize, orient):

            count += 1
            removeTiles(word)
            getTiles(myTiles)

    if count == 0:

        if firstMove(word, row, col, bSize):

            count += 1
            removeTiles(word)
            getTiles(myTiles)

    printTiles(myTiles)