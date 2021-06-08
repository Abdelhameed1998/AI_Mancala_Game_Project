import sys
sys.setrecursionlimit(10000)
from numpy import  inf
negative_infinity = -inf
postitive_infinity = inf



class MancalaGame():
    def __init__(self ,level,board = None, stealing = True):
        self.stealing = stealing
        self.level = str(level)
        if board!=None: # you want to start at certain board state
            self.board = board
        else:
            self.board=[4,4,4,4,4,4,0,4,4,4,4,4,4,0] # initial state



    def player_move(self,player,hole): #player = True or False

        playagain = False

        stones = self.board[hole]
        round = hole+1
        self.board[hole]=0
        # handle the other mancala for each player
        while stones > 0:
            if (player) and round == 6:       #player two  ==> 0-5
                round == 7
            if (not player) and round == 13:  #player one  ==> 0-5
                round = 0

            # round robin on the holes to add a stone
            self.board[round] = self.board[round]+1
            stones -=1

            if stones == 0:
                lasthole = round
            else: ## holes from 0 to 13
                round = round +1
                if round > 13 :
                    round = 0

        # handle turns
        if (not player) and round == 6 :
             playagain = True  # False

        elif player and round == 13:
            playagain = True # True

        # stealing  or not
        elif (not player) and self.stealing and self.board[lasthole] == 1 and lasthole < 6 :
            if self.board[12-lasthole] != 0:
                self.board[6] = self.board[6] +  self.board[lasthole] + self.board[12-lasthole]
                self.board[lasthole] = 0
                self.board[12-lasthole]=0


        elif player and self.stealing and self.board[lasthole] == 1 and lasthole > 6  :
            if self.board[12-lasthole] != 0:
                self.board[13] = self.board[13] +  self.board[lasthole] + self.board[12-lasthole]
                self.board[lasthole] = 0
                self.board[12-lasthole]=0

        return  playagain

    def possible_moves(self):
        possible_moves = 0
        for i, a in enumerate(self.board[7:13]):
            if a > 0:
                possible_moves+=1
        return  possible_moves

    def isterminal(self):
        player1side = 0
        player2side = 0
        for hole in range(6):
            player1side = player1side + self.board[hole]
            player2side = player2side + self.board[hole + 7]
        if (player1side == 0 or player2side == 0):
            self.board[6] = self.board[6] + player1side
            self.board[13] = self.board[13] + player2side
            for hole in range(6):
                self.board[hole] = 0
                self.board[12-hole] = 0
            return True
        return False



    def who_won(self):
        # who won
        if ( self.board[6] >  self.board[13]):
            print("You won") #player 1
        elif ( self.board[6] <  self.board[13]):
            print("AI won") # player2
        else:
            print("No one Win it is Draw ")
