import random
import copy
import itertools
import math
import gomoku
import time



class Node:
    def __init__(self, board, last_move, valid_moves, color, parent=None):
        self.board = board
        self.valid_moves = valid_moves
        self.children = []
        self.parent = parent
        self.color = color
        self.last_move = last_move
        self.visits = 0
        self.Q = 0

    def UCB1(self, constant=1.4):
        return ((self.Q/self.visits)+constant*(math.sqrt(2*math.log(self.parent.visits))/self.visits))

    def findSpotToExpand(self, nRoot):
        # print("explaning", nRoot)
        # if this node is terminal, end
        # print("findspot")
        if len(nRoot.valid_moves) == 0:
            return nRoot
        # # if there are nodes to make
        if len(nRoot.children) < len(nRoot.valid_moves):
            game = gomoku.gomoku_game(19, nRoot.board)
            move = nRoot.valid_moves[len(nRoot.children)]
            game.move(move)
            NewNode = Node(nRoot.board, move, nRoot.valid_moves, nRoot.color)
            NewNode.parent = nRoot
            nRoot.children.append(NewNode)
            return NewNode
        if len(nRoot.children) >= len(nRoot.valid_moves):
            # print(id(nRoot))
            # print(nRoot.children[1].valid_moves)
            bestc = nRoot.best_child(nRoot)
            # print("CALLING with",  len(nRoot.children))
            # print("VMS",  len(nRoot.valid_moves))
            return self.findSpotToExpand(bestc)

    def best_child(self, daddynode):
        if len(daddynode.children) > 0:
            best_node = daddynode.children[0]
            for node in daddynode.children:
                if node.UCB1() > best_node.UCB1():
                    # print("Evaluating : ",best_node.last_move, node.UCB1(), " vs ", best_node.UCB1())
                    best_node = node
                    print(best_node, " with ", best_node.UCB1(), " with move ", best_node.last_move)
            return best_node


class finnff:
    """This class specifies a player that just does random moves.
    The use of this class is two-fold: 1) You can use it as a base random roll-out policy.
    2) it specifies the required methods that will be used by the competition to run
    your player
    """

    def id(self):
        """Please return a string here that uniquely identifies your submission e.g., "name (student_id)" """
        return "finnff 1745799"

    def __init__(self, black_=True):
        """Constructor for the player."""
        self.colour = black_
        self.s0 = None
        self.leaf = None

    def new_game(self, black_):
        """At the start of each new game you will be notified by the competition.
        this method has a boolean parameter that informs your agent whether you
        will play black or white.
        """
        self.reset = True
        self.colour = black_
        self.s0 = None
        self.leaf = None

            

    def rollout(self, leafnode):
        if leafnode is not None:
            # print("rolling out: ")
            # lm = leafnode.last_move
            simgame = gomoku.gomoku_game(19, leafnode.board)
            while leafnode.valid_moves:
                candidate = random.choice(leafnode.valid_moves)
                lm = candidate
                # print(candidate)
                simgame.move(candidate)
                leafnode.valid_moves.remove(candidate)
                if simgame.check_win(lm):
                    return 1.0
                if len(simgame.valid_moves()) == 0:
                    # print("DRAW")
                    return 0.5
                else:
                    return 0
            return 0
        else:
            print("LEAFNOTE IS NONE ??????????????????/")

    def backupval(self, value, noden):
        turn = False
        while noden is not None:
            noden.visits += 1
            if turn:
                noden.Q += value
            else:
                noden.Q += value
            turn = True
            noden = noden.parent

    def move(self, board, last_move, valid_moves, max_time_to_move=1000):
        """This is the most important method: the agent will get:
        1) the current state of the board
        2) the last move by the opponent
        3) the available moves you can play (this is a special service we provide ;-) )
        4) the maximimum time until the agent is required to make a move in milliseconds [diverging from this will lead to disqualification].
        """
        startime = time.time_ns()
        currtime = time.time_ns()
        s0 = Node(board, last_move, valid_moves, self.colour)
        if(self.colour and self.reset):
            self.reset = False
            # print("RESET")
            return(9,9)
        # while (currtime<startime+(max_time_to_move*1000)):
        for i in range(0, 179):
            leaf = s0.findSpotToExpand(s0)
            val = self.rollout(leaf)
            self.backupval(val, leaf)
        currtime = time.time_ns()

        if(leaf is None):
            return()

        # print("best posible move: ", leaf.last_move)
        if (leaf.last_move is None):
            print(s0.valid_moves)
            # return(10,10)
        else:
            return (leaf.last_move)
