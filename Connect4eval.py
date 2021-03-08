# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 19:12:12 2019

@author: mkolta
"""
import random;
from copy import copy, deepcopy

ROWS = 6
COLS = 7
NUM_MATCHES = 100;


def printBoard(B):
    for y in B:
        for x in y:
            print(x, end="")
        print()


def moveLegal(B, move):
    # is move on board
    if (move < 0 or move >= COLS):
        return False
    # is column full
    if (B[0][move] != 0):
        return False
    return True


def addChecker(B, move, playerTurn):
    for y in reversed(range(ROWS)):  # check if cells empty top to bottom
        if (B[y][move] == 0):
            B[y][move] = playerTurn
            return


# board
def won(B, move, playerTurn):
    moveY = 0
    for y in reversed(range(ROWS)):
        if (B[y][move] == 0):
            B[y][move] = playerTurn
            moveY = y;
            break
    # check horizontal
    for streak in range(4):
        numConnected = 0;
        for x in range(move - streak, move - streak + 4):
            if (x >= 0 and x < COLS):
                if (B[moveY][x] == playerTurn):
                    numConnected += 1;
                    if numConnected == 4:
                        return True

    # check vertical
    for streak in range(4):
        numConnected = 0;
        for y in range(moveY - streak, moveY - streak + 4):
            if (y >= 0 and y < ROWS):
                if (B[y][move] == playerTurn):
                    numConnected += 1;
                    if numConnected == 4:
                        return True

    # check diagonal lower left to upper right
    for streak in range(4):
        numConnected = 0;
        # print ((moveY -streak+4))
        for y in (range(moveY + streak, moveY + streak - 4, -1)):

            if (y >= 0 and y < ROWS and (move - y + moveY) >= 0 and (move - y + moveY) < COLS):
                # print ("y" , y ," x" , move-y + moveY)
                if (B[y][move - y + moveY] == playerTurn):
                    numConnected += 1;
                    if numConnected == 4:
                        # print ("diagonal win")
                        return True

    # check diagonal upper left to lower right
    for streak in range(4):
        numConnected = 0;

        for y in range(moveY - streak, moveY - streak + 4):
            # print ("y" , y ," x" , move+y-moveY )
            if (y >= 0 and y < ROWS and (move + y - moveY) >= 0 and (move + y - moveY) < COLS):
                if (B[y][move + y - moveY] == playerTurn):

                    numConnected += 1;
                    if numConnected == 4:
                        # print ("other diagonal win")
                        return True

    return False


# my weak evluation function
def c4eval(B, playerTurn):
    print("playerTurn: ", playerTurn)
    score = 0
    """ iterate through columns
    find topmost piece in each column
        if it is playerturn, add 1
            if there is a consecutive piece either below, 
            to the right, or right diagonal (up or down) add another 1
    """
    # iterate through columns
    for x in range(COLS):
        # check for playerTurn pieces in that row
        for y in range(ROWS):
            # if opponent piece is on top
            if (B[y][x] == (playerTurn % 2 + 1)):
                break
            elif B[y][x] == playerTurn:
                # print("y: ",y , "x: ",x)
                score += 1
                # check below
                if (y < (ROWS - 1) and (B[y + 1][x] == playerTurn)):
                    score += 1
                    # print('b')
                # check right
                if (x < (COLS - 1) and (B[y][x + 1] == playerTurn)):
                    score += 1
                    # print('r')
                # check lower diagonal
                if (y < (ROWS - 1) and x < (COLS - 1) and (B[y + 1][x + 1] == playerTurn)):
                    score += 1
                    # print('ld')
                # check upper diagonal
                if ((y > 0) and x < (COLS - 1) and (B[y - 1][x + 1] == playerTurn)):
                    score += 1
                    # print('ud')
                break

    print("evaluation score: ", score)


#####################################################
# main code starts here
playerTurn = 1;

# wins[0] = ties, wins[1] = player 1 wins, wins[2] = player 2 wins
wins = [0 for col in range(3)]
move = 0;
for game in range(NUM_MATCHES):
    if (game % 2 == 0):
        playerTurn = 1;
    else:
        playerTurn = 2;
    B = [[0 for col in range(COLS)] for row in range(ROWS)];  # create/reset board
    # add diagonal win

    # max number of turns is number of cells in game board
    for turn in range(ROWS * COLS):
        # pass board to the player (1 or 2)
        # receive move back from player
        if (playerTurn == 1):
            # pass board to player 1
            # example: move=AutobotsMiniMax(B, playerTurn)
            move = random.randint(0, COLS - 1)
            c4eval(deepcopy(B), playerTurn)
            # print (move)
        else:
            # pass board to player 2
            # example: move=BumblebeesMiniMax(B, playerTurn)
            move = random.randint(0, COLS - 1)

        # make sure move is legal, if not that player loses
        if (not (moveLegal(B, move))):
            playerTurn = playerTurn % 2 + 1
            wins[playerTurn] += 1;
            wins[0] -= 1;
            break;  # break out of for loop for turns
        # Add checker to board & check if won
        # f yes than increments wins for this player and reset
        if (won(B, move, playerTurn)):
            wins[playerTurn] += 1;
            playerTurn = playerTurn % 2 + 1
            wins[0] -= 1;
            break;  # break out of for loop for turns
        # if (won(B, ))
        playerTurn = playerTurn % 2 + 1
    # board is full or someone won
    wins[0] += 1;
    print("Game ", game, "turn ", turn)
    printBoard(B);

# display results
print("Player 1 won ", wins[1], " times")
print("Player 2 won ", wins[2], " times")
print("There were ", wins[0], " ties")
# change to other player
