from Game import MancalaGame
from numpy import  inf
from time import time
neg_infinity = -inf
pos_infinity = inf

class Player():
    def __init__(self,player_turn):
        self.player_turn = player_turn # True =>player 1 False => player2

    def make_move(self,board):
        pass

    def turn(self):
        if type == True:
            print( 'AI turn')
        else:
            print( 'PLAYER  {} turn  '.format(self.player_turn))