from operator import truediv
import string
from tabnanny import check
from time import sleep
from tkinter.messagebox import NO
from turtle import right

MAX = 7
MIN = 0

chessPoint = {
    "A1": {"x": 0, "y": 0},
    "A2": {"x": 0, "y": 1},
    "A3": {"x": 0, "y": 2},
    "A4": {"x": 0, "y": 3},
    "A5": {"x": 0, "y": 4},
    "A6": {"x": 0, "y": 5},
    "A7": {"x": 0, "y": 6},
    "A8": {"x": 0, "y": 7},
    "B1": {"x": 1, "y": 0},
    "B2": {"x": 1, "y": 1},
    "B3": {"x": 1, "y": 2},
    "B4": {"x": 1, "y": 3},
    "B5": {"x": 1, "y": 4},
    "B6": {"x": 1, "y": 5},
    "B7": {"x": 1, "y": 6},
    "B8": {"x": 1, "y": 7},
    "C1": {"x": 2, "y": 0},
    "C2": {"x": 2, "y": 1},
    "C3": {"x": 2, "y": 2},
    "C4": {"x": 2, "y": 3},
    "C5": {"x": 2, "y": 4},
    "C6": {"x": 2, "y": 5},
    "C7": {"x": 2, "y": 6},
    "C8": {"x": 2, "y": 7},
    "D1": {"x": 3, "y": 0},
    "D2": {"x": 3, "y": 1},
    "D3": {"x": 3, "y": 2},
    "D4": {"x": 3, "y": 3},
    "D5": {"x": 3, "y": 4},
    "D6": {"x": 3, "y": 5},
    "D7": {"x": 3, "y": 6},
    "D8": {"x": 3, "y": 7},
    "E1": {"x": 4, "y": 0},
    "E2": {"x": 4, "y": 1},
    "E3": {"x": 4, "y": 2},
    "E4": {"x": 4, "y": 3},
    "E5": {"x": 4, "y": 4},
    "E6": {"x": 4, "y": 5},
    "E7": {"x": 4, "y": 6},
    "E8": {"x": 4, "y": 7},
    "F1": {"x": 5, "y": 0},
    "F2": {"x": 5, "y": 1},
    "F3": {"x": 5, "y": 2},
    "F4": {"x": 5, "y": 3},
    "F5": {"x": 5, "y": 4},
    "F6": {"x": 5, "y": 5},
    "F7": {"x": 5, "y": 6},
    "F8": {"x": 5, "y": 7},
    "G1": {"x": 6, "y": 0},
    "G2": {"x": 6, "y": 1},
    "G3": {"x": 6, "y": 2},
    "G4": {"x": 6, "y": 3},
    "G5": {"x": 6, "y": 4},
    "G6": {"x": 6, "y": 5},
    "G7": {"x": 6, "y": 6},
    "G8": {"x": 6, "y": 7},
    "H1": {"x": 7, "y": 0},
    "H2": {"x": 7, "y": 1},
    "H3": {"x": 7, "y": 2},
    "H4": {"x": 7, "y": 3},
    "H5": {"x": 7, "y": 4},
    "H6": {"x": 7, "y": 5},
    "H7": {"x": 7, "y": 6},
    "H8": {"x": 7, "y": 7},
}

X = ["A","B","C","D","E","F","G","H"]
Y = ["1","2","3","4","5","6","7","8"]

class ChessHorse:
    point = ""
    move = []
    def __init__(self, point) -> None:
        self.point = point
    
    def horseMove(self):
        self._moveUpLeft()
        self._moveUpRight()
        self._moveDownLeft()
        self._moveDownRight()
    
    def _moveUpLeft(self):
        movePoint = self.point
        for i in range(2):
            movePoint = chessGoUp(movePoint)
        if movePoint != -1:
            movePoint = chessGoLeft(movePoint)
        self.move.append(movePoint)
    
    def _moveUpRight(self):
        movePoint = self.point
        for i in range(2):
            movePoint = chessGoUp(movePoint)
        if movePoint != -1:
            movePoint = chessGoRight(movePoint)
        self.move.append(movePoint)
    
    def _moveDownRight(self):
        movePoint = self.point
        for i in range(2):
            movePoint = chessGoDown(movePoint)
            if movePoint == -1:
                break
        if movePoint != -1:
            movePoint = chessGoRight(movePoint)
        self.move.append(movePoint)
    
    def _moveDownLeft(self):
        movePoint = self.point
        for i in range(2):
            movePoint = chessGoDown(movePoint)
            if movePoint == -1:
                break
        if movePoint != -1:
            movePoint = chessGoLeft(movePoint)
        self.move.append(movePoint)

def chessGoUp(point):
    x = chessPoint.get(point)['x']
    y = chessPoint.get(point)['y']+1
    if y > MAX:
        return -1
    return getChessPoint(x,y)

def chessGoDown(point):
    x = chessPoint.get(point)['x']
    y = chessPoint.get(point)['y']-1
    if y < MIN:
        return -1
    return getChessPoint(x,y)

def chessGoLeft(point):
    x = chessPoint.get(point)['x']-1
    y = chessPoint.get(point)['y']
    if x < MIN:
        return -1
    return getChessPoint(x,y)

def chessGoRight(point):
    x = chessPoint.get(point)['x']+1
    y = chessPoint.get(point)['y']
    if x > MAX:
        return -1
    return getChessPoint(x,y)

def getChessPoint(x, y):
    guessedMin = 0
    guessedMax = 64
    targetX = x
    targetY = y
    breakEmergency = 0
    while guessedMax >= guessedMin:
        guessed = (guessedMin+guessedMax)//2
        point = list(chessPoint.keys())[guessed]
        guessX = chessPoint.get(point)['x']
        guessY = chessPoint.get(point)['y']
        if breakEmergency >= MAX:
            print("Searching Point Error, System \'BREAK EMERGENCY ACTIVE\'")
            return -1
        if guessX == targetX:
            if guessY == targetY:
                return(point)
            elif guessY > targetY:
                guessedMax = guessed
            else:
                guessedMin = guessed
        elif guessX > targetX:
            guessedMax = guessed
        else:
            guessedMin = guessed
        breakEmergency += 1


def horseScope(point):
    point = point
    pointMove = [point]
    chessMoveMap = {
        point: {}
    }
    tmpMoveMap = chessMoveMap

horseScope("A1")
# getChessPoint(0,0)
# 8
# 7
# 6
# 5
# 4
# 3  x   x
# 2  x
# 1  x
# y
# x  A   B   C   D   E   F   G   H

#* Set horsePoint = A1 <=> X[0]Y[0]