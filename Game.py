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
            
    
    def print_board(self):
        i = 0
        for i in range(len(self.board)):
            if (self.board[i]) < 10 :
                self.board[i]=" "+str(self.board[i])
            else:
                self.board[i]=str(self.board[i])
        print()
        print("            |12|  |11|  |10|   |9|    |8|   |7| ")
        print("+---------+-----+------+-----+------+-----+-----+---------+")
        print("|Opponent | " + str(self.board[12]) + "  | " + (self.board[11])
              + "   | " + (self.board[10]) + "  | " + (self.board[9])
              + "   | " + (self.board[8]) + "  | " + (self.board[7]) + "  |    You  |")
        print("| " + (self.board[13]) + "      |----+----+----+----+----+----+-------| " + (self.board[6]) + "      |")
        print("|         | " + (self.board[0]) + "  | " + (self.board[1])
              + "   | " + (self.board[2]) + "  | " + (self.board[3])
              + "   | " + (self.board[4]) + "  | " + (self.board[5]) + "  |         |")
        print("+---------+-----+------+-----+------+-----+-----+---------+")
        print("            |0|   |1|    |2|    |3|   |4|   |5|            ")
        for i in range(len(self.board)):
            self.board[i]=int(self.board[i])
def minmax(board, alpha, beta, player,depth = 10,):
    if depth == 0  or board.isterminal():
        return board.static_eval() , -1
    ## Maximaizer
    if player:
        maxEval = negative_infinity
        move = -1
        for i in range(7, 13, 1):
            if board.board[i] == 0: #skip holes that holds zero stones
                continue
            a = MancalaGame(board.board[:]) # child
            again = a.player_move(True,i)
            eval, _ = minmax( a, alpha, beta, again,depth-1)
            if maxEval < eval:
                move = i
            maxEval =max(eval,maxEval)
            alpha = max(alpha, maxEval)
            if alpha >= beta:
                break
        return maxEval, move

    ## Minimaizer
    else:
        mineval = postitive_infinity
        move = -1
        for i in range(0, 6, 1):
            if board.board[i] == 0: continue
            a = MancalaGame(board.board[:])
            again = a.player_move(False,i)
            eval, _ = minmax(a,  alpha, beta, (not again),depth-1 )
            if mineval > eval:
                move = i
            mineval = min(eval,mineval)
            beta = min(beta, mineval)
            if alpha >= beta:
                # print("breaking ", i)
                break
        return mineval, move



# if __name__ == "__main__":
#     game = MancalaGame([4,4,3,4,0,0,0,4,4,4,3,0,0,0])
#     game.print_board()
#     print(game.another_turn_opportunities())
#     print(game.another_turn_opportunities_for_opponenet())
#     print(game.static_eval())
#     print(game.stealing_opportunities())
#     print(game.stealing_opportunities_for_opponent())
#     # first = input("who plays first ? if you press y if opponent press o")
#     # while not( first == 'y' or first == 'o'):
#     #     first = input("you must choose who plays first ? if you press y if opponent press o")
#     # if first == 'y':
#     #     while (True):
#     #         if game.isterminal():
#     #             break
#     #         while True:
#     #             if game.isterminal():
#     #                 break
#     #             move = int(input("YOUR TURN "))
#     #             while not game.validate_move(move):
#     #                 move = int(input("YOUR TURN "))
#     #             t = game.player_move(False,move)
#     #             game.print_board()
#     #             if not t:
#     #                 break
#     #         while (True):
#     #             if game.isterminal():
#     #                 break
#     #             print("Opponent turn ")
#     #             _, move = minmax(game, negative_infinity, postitive_infinity, True, 10)
#     #             print('move-->', move)
#     #             t = game.player_move(True, move)
#     #             game.print_board()
#     #             if not t:
#     #                 break
#     #     print('GAME ENDED')
#     #     game.print_board()
#     #     game.who_won()
#     #
#     # if first == 'o':
#     #     while (True):
#     #         if game.isterminal():
#     #             break
#     #         while (True):
#     #             if game.isterminal():
#     #                 break
#     #             print("Opponent turn ")
#     #             _, k = minmax(game,  negative_infinity, postitive_infinity, True,10)
#     #             print('move-->', k)
#     #             t = game.player_move(True,k)
#     #             game.print_board()
#     #             if not t:
#     #                 break
#     #         while True:
#     #             if game.isterminal():
#     #                 break
#     #             h = int(input("YOUR TURN "))
#     #             while not game.validate_move(h):
#     #                 h = int(input("YOUR TURN "))
#     #             t = game.player_move(False,h)
#     #             game.print_board()
#     #             if not t: break
#     #     print('GAME ENDED')
#     #     game.print_board()
#     #     game.who_won()
