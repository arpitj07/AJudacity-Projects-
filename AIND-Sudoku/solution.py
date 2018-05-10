
from utils import *
import collections
from itertools import *
from operator import or_
from functools import *

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
num1=8
num2=10
diagonal1= [boxes[num2*i] for i in range(9)]
diagonal2= [boxes[num1*i] for i in range(1,10)]
diagonal= [diagonal1,diagonal2]
unitlist = row_units + column_units + square_units +diagonal

unitlist = unitlist


units = extract_units(unitlist, boxes)
peers = extract_peers(units, boxes)


def naked_twins(values):

    """

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the naked twins eliminated from peers
   """
    num=[]
    twins=[]

    #finding boxes with 2 digit value
    for box in boxes:
        if len(values[box])==2:
            num.append(box)
    
    for box1 in num:
        for box2 in peers[box1]:
            if set(values[box1])==set(values[box2]):
                twins.append([box1,box2])

    #finding peers of the naked twins:
    for i in range(len(twins)):
        box1,box2=twins[i][0],twins[i][1]

        peers1,peers2= set(peers[box1]),set(peers[box2])
        naked_twins_peers= peers1.intersection(peers2)  
        for peer in naked_twins_peers:
            if len(values[peer])>1:
                for digit in values[box1]:
                    values = assign_value(values, peer, values[peer].replace(digit,''))



    return values





def eliminate(values):
    """
    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with the assigned values eliminated from peers
    """
    
    x = [s for s in values.keys() if len(values[s]) == 1]
    for s in x:
        digit = values[s]
        for peer in peers[s]:
            values[peer] = values[peer].replace(digit,'')
            
    return values





def only_choice(values):
    """
    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict
        The values dictionary with all single-valued boxes assigned

   
    """
    for unit in unitlist:
        for digit in cols:
            dp= [s for s in unit if digit in values[s]]
            if len(dp)==1:
                values[dp[0]]= digit            
    return values




def reduce_puzzle(values):
    """

    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary after continued application of the constraint strategies
        no longer produces any changes, or False if the puzzle is unsolvable 
    """
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        values= eliminate(values)
        #values= naked_twins(values)  
        # Your code here: Use the Only Choice Strategy
        values=only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([s for s in values.keys() if len(values[s]) == 0]):
            return False
    return values




def search(values):
    """
    Parameters
    ----------
    values(dict)
        a dictionary of the form {'box_name': '123456789', ...}

    Returns
    -------
    dict or False
        The values dictionary with all boxes assigned or False

  
    """
    values= reduce_puzzle(values)
   
    if values is False:
        return False
    if all(len(values[s])==1 for s in boxes):
        return values
    x,s=min((len(values[s]),s) for s in boxes if len(values[s])>1)
    for value in values[s]:
        new_game= values.copy()
        new_game[s]=value
        attempt= search(new_game)
        if attempt:
            return attempt



def solve(grid):
    """
    Parameters
    ----------
    grid(string)
        a string representing a sudoku grid.
        
        Ex. '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    Returns
    -------
    dict or False
        The dictionary representation of the final sudoku grid or False if no solution exists.
    """
    values = grid2values(grid)
    values = search(values)
    return values


if __name__ == "__main__":
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(grid2values(diag_sudoku_grid))
    result = solve(diag_sudoku_grid)
    display(result)

    try:
        import PySudoku
        PySudoku.play(grid2values(diag_sudoku_grid), result, history)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
