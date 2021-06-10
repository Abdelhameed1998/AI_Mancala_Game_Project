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

class HumanPlayer(Player):
    type = False
    def make_move(self,board):
        move = int(input("Enter valid  Move: \n ").replace(" ",""))
        while not board.validate_move(move):
            move =int( input("Enter valid  Move: \n ").replace(" ",""))
        return  -1,int(move)

class AI_Player(Player):
    def __init__(self,turn):
        super().__init__(player_turn=turn)
        self.cutoff = 0
        self.depth = 0
        self.leaf_nodes=0
        self.leaf_eval=[]
    type = True

    def make_move(self , board, alpha =neg_infinity, beta=pos_infinity, player=True,depth = 12):
        if depth == 0  or board.isterminal():
            self.depth=depth
            self.cutoff = 0
            if depth ==0:
                self.leaf_nodes +=1
                self.leaf_eval.append(board.static_eval())
                return float(board.static_eval()) , -1
            else:
                return float(board.static_eval()) , -1

        ## Maximaizer
        if player:
            maxEval = neg_infinity
            move = -1
            for i in range(7, 13, 1):
                if board.board[i] == 0: #skip holes that holds zero stones
                    continue
                a = MancalaGame(board.board[:]) # child
                again = a.player_move(True,i)
                eval, _ = self.make_move( a, alpha, beta, again,depth-1)
                if maxEval < eval:
                    move = i
                maxEval =max(eval,maxEval)
                alpha = max(alpha, maxEval)
                if alpha >= beta:
                    self.cutoff +=1
                    break
            return float(maxEval), move

        ## Minimaizer
        else:
            mineval = pos_infinity
            move = -1
            for i in range(0, 6, 1):
                if board.board[i] == 0: continue
                a = MancalaGame(board.board[:])
                again = a.player_move(False,i)
                eval, _ = self.make_move(a,  alpha, beta, (not again),depth-1 )
                if mineval > eval:
                    move = i
                mineval = min(eval,mineval)
                beta = min(beta, mineval)
                if alpha >= beta:
                    self.cutoff +=1
                    break
            return float(mineval), move
    
    def iterative_deepening_move(self,time_limit,max_depth=11):
        depth=1
        bestmove = 7
        start_time=int(time())
        m=0
        while depth < max_depth and not(start_time >= int(time_limit)):
            m,bestmove = self.make_move(depth=depth)
            depth +=1
        return m,bestmove


>>>>>>> b60b7ef49e6214be3df0c963a2295395e60c72cd
