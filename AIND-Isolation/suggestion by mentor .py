"""
This library provides a Python implementation of the game Isolation.
Isolation is a deterministic, two-player game of perfect information in
which the players alternate turns moving between cells on a square grid
(like a checkerboard).  Whenever either player occupies a cell, that
location is blocked for the rest of the game. The first player with no
legal moves loses, and the opponent is declared the winner.
"""

# Make the Board class available at the root of the module for imports
from isolation import Board


 moves_own = len(game.get_legal_moves(player))
    moves_opp = len(game.get_legal_moves(game.get_opponent(player)))
    board = game.height * game.width
    moves_board = game.move_count / board
    if moves_board > 0.33:
        move_diff = (moves_own - moves_opp*2) 
    else:
        move_diff = (moves_own - moves_opp)

    pos_own = game.get_player_location(player)
    pos_opp = game.get_player_location(game.get_opponent(player))

    m_distance = abs(pos_own[0] - pos_opp[0]) + abs(pos_own[1] - pos_opp[1])



    return float(move_diff / m_distance)