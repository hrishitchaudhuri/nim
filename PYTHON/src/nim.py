# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:58:59 2020

@author: hrishit chaudhuri
@github: https://www.github.com/hrishitchaudhuri
"""
import sys
import time

import nimClass as nc


def endMessage(game):
    """
    Print message at end of game.

    Parameters
    ----------
    game : nimGame
        Game initizalized with user specifications.

    Returns
    -------
    None.

    """
    
    if game.player_turn == "y":
        restart=input_start("You lost :(\nWould you like to play again? [Y/N] ")
        if restart=='y':
            startGame()
        else:
            sys.exit(0)
            
    else:
        restart=input_start("You won :)\nWould you like to play again? [Y/N] ")
        if restart=='y':
            startGame()
        else:
            sys.exit(0)


def int_error(func, *args):
    """
    Handle ValueErrors in int-returning functions. 

    Parameters
    ----------
    func : function
        Function for which a ValueError has to be handled.
    *args : tuple
        Arguments to the function.

    Returns
    -------
    None.

    """
    
    print("Please enter a valid integer.")
    func(*args)

    
def input_heaps():
    """
    Return user-input for setting number of nim-heaps. 

    Returns
    -------
    a : int
        Number of heaps in nim-game set by user.

    """
    
    try:
        a=int(input("Enter number of heaps: "))
        while a<=0: 
            a=int(input("Enter valid number of heaps: "))
    
    except ValueError:
        int_error(input_heaps)
    
    finally:
        return a


def input_heapsizes(a):
    """
    Return user-input for setting size of each nim-heap. 

    Parameters
    ----------
    a : int
        Number of heaps in nim-game.

    Returns
    -------
    heaps : list
        Array containing height of each nim-heap.

    """
    
    try:
        heaps=[]
        for i in range(a):
            heaps.append(int(input("Enter size of heap %d: " % i)))
    
    except ValueError:
        int_error(input_heapsizes, a)
    
    finally:
        return heaps
        

def input_start(ipstring):
    """
    Return user response to [Y/N] question. 

    Parameters
    ----------
    ipstring : str
        [Y/N] question to be asked to user.

    Returns
    -------
    player_turn : str
        [Y/N] response given by user.

    """
    
    try:        
        player_turn=input(ipstring)
        while player_turn.lower() not in ["y", "n"]:
            player_turn=input("Please enter a valid response. [Y/N]? ")
    
    except ValueError:
        print("Please enter valid string")
        input_start()
        
    finally:
        return player_turn

        
def heap_choice(game):
    """
    Return user-input to choose heap to play in. 

    Parameters
    ----------
    game : nimGame
        Game initialized with user specifications.

    Returns
    -------
    heap : int
        Heap which user chooses to draw coins from.

    """
    
    try:
        heap=int(input("Enter heap number to remove coins from: "))
        while heap not in range(0, len(game.heaps)):
            heap=int(input("Enter valid heap number: "))
    
    except ValueError:
        int_error(heap_choice, game)
    
    finally:
        return heap
    

def count_choice(heap, game):
    """
    Return user-input to choose number of coins to draw from heap.

    Parameters
    ----------
    heap : int
        Heap which user chooses to draw coins from.
    game : nimGame
        Game initialized with user specifications.

    Returns
    -------
    count : int
        Number of coins user chooses to draw from heap.

    """
    
    try:
        count=int(input("Enter number of coins to remove: "))
        while count not in range(1, game.heaps[heap]+1):
            count=int(input("Enter number in range: "))
        
    except ValueError:
        int_error(count_choice, heap, game)
        
    finally:
        return count
    

def getPlayer_turn(game):
    """
    Obtain and return user play.

    Parameters
    ----------
    game : nimGame
        Game initialized with user specifications.

    Returns
    -------
    list
        List containing player turn.

    """
    
    heap=heap_choice(game)
    count=count_choice(heap, game)
        
    return [heap, count]
    

def init_menu():
    """
    Set up menu for initializing nim game. 

    Returns
    -------
    game : nimGame
        Game initialized with user specifications.

    """
    
    a=input_heaps()
    print("")

    heaps=input_heapsizes(a)    
    print("")

    player_turn=input_start("Would you like to start? [Y/N]? ")
    print("")
    
    game=nc.nimGame(heaps, player_turn.lower())
    return game


def play_turn(game):
    """
    Instruct computer or player to play respective turn.

    Parameters
    ----------
    game : nimGame
        Game initialized with user specifications.

    Returns
    -------
    None.

    """
    
    if game.isEndgame():
        endMessage(game)
    
    if game.player_turn == "y":
        turn=getPlayer_turn(game)
        game.heaps[turn[0]]-=turn[1]
        print("You removed", turn[1], "from heap", turn [0])
        game.player_turn="n"
    
    else:
        turn=game.bestPlay()
        game.heaps[turn[0]]-=turn[1]
        print("\nComputer thinking...")
        time.sleep(2)
        print("Computer removed", turn[1], "from heap", turn[0])
        game.player_turn="y"


def draw_game(game):
    """
    Print current game state.

    Parameters
    ----------
    game : nimGame
        Game initialized with user specifications.

    Returns
    -------
    None.

    """
    
    print("Current game state: " + str(list(map(lambda x: "Heap " + str(x) + 
                                                " (*" + str(game.heaps[x]) +")", 
                                                [x for x in range(len(game.heaps))]))))


def startGame():
    """
    Start new nim game.

    Returns
    -------
    None.

    """
    
    game=init_menu()
    game.max_height=max(game.heaps)
    while True:
        draw_game(game)
        play_turn(game)