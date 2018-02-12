"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
from isolation import *
#from __init__ import *
from random import randint


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)
   

def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    my_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(my_moves - (2*opp_moves))

   


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout












class MinimaxPlayer(IsolationPlayer):
   

    def get_move(self, game, time_left):
        
        self.time_left = time_left
        best_move = (-1, -1)

        try:
            return self.minimax(game,self.search_depth)

        except SearchTimeout:
            pass  
        return best_move

    def minimax(self, game, depth):


        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        best_score = float("-inf")
        if not game.get_legal_moves():
            return (-1,-1)
        best_move= game.get_legal_moves()[0]
            
        for m in game.get_legal_moves():
        
        
            v = self.min_value(game.forecast_move(m),depth - 1)
            if v > best_score:
                best_score = v
                best_move = m
            
        return best_move 
        
        

    def terminal_test(self,game,depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth==0:
            return True
        else:
            return False

    def min_value(self,game,depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(self,game):
            return self.score(game,self)
            
        if not game.get_legal_moves(): 
            return self.score(game,self)

        v= float('inf')
        for m in game.get_legal_moves():
            v= min(v,self.max_value(game.forecast_move(m),depth -1))
        return v  
            
    def max_value(self,game,depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(self,game):
            return self.score(game,self)

        if not game.get_legal_moves(): 
            return self.score(game,self)    
            

        v= float('-inf')
        for m in game.get_legal_moves():
            v= max(v,self.min_value(game.forecast_move(m),depth -1))
        return v 


        
            
        

            


             






    
        


class AlphaBetaPlayer(IsolationPlayer):
    

    def get_move(self, game, time_left):
        
        self.time_left = time_left
        best_move = (-1, -1)
        if not  game.get_legal_moves():
            return best_move
        dep=1
        

        try:
            while True:

                best_move= self.alphabeta(game,dep)
                dep+=1
            #return self.alphabeta(game, self.search_depth)

        except SearchTimeout:
            pass

        return best_move         

    def terminal_test(self,game,depth,alpha=float('-inf'),beta=float('inf')):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
            
        return depth==0
                

    def min_value(self,game,depth,alpha=float('-inf'),beta=float('inf')):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(self,game):
                return self.score(game,self,alpha,beta)

        v= float('inf')
        for m in game.get_legal_moves():
            v= min(v,self.max_value(game.forecast_move(m),depth -1,alpha,beta))
            if v <=alpha:
                return v

            beta= min(beta,v)
        return v  
            
    def max_value(self,game,depth,alpha=float('-inf'),beta=float('inf')):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if self.terminal_test(self,game):
            return self.score(game,self)

        v= float('-inf')
        for m in game.get_legal_moves():
            v= max(v,self.min_value(game.forecast_move(m),depth -1,alpha,beta))
            if v>= beta:
                return v

            alpha=max(alpha,v)
                
        return v            


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
       
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

    
        best_score = float("-inf")
        best_move = game.get_legal_moves()[0]
        if not game.get_legal_moves():
            return (-1,-1)

        for m in game.get_legal_moves():
            v = self.min_value(game.forecast_move(m),depth -1,alpha,beta)
            if v > best_score:
                best_score = v                   
                best_move = m
                
            aplha=max(alpha,best_score)
            

        return best_move 


        

        
        
