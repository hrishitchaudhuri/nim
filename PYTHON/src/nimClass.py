# -*- coding: utf-8 -*-
"""
nimClass.py
===============
Module containing class description for nim game.

@author: hrishit chaudhuri
@github: https://www.github.com/hrishitchaudhuri
"""
import functools
import random as rr

class nimGame:
    """
    A class to describe a nim game.
    """

    def __init__(self, heaps, player_turn):
        """
        nimGame constructor.

        Parameters
        ----------
        heaps : int
            Number of nim-heaps in game.
        player_turn : str
            Current player turn.

        Returns
        -------
        None.

        """
        
        self.heaps=heaps
        self.player_turn=player_turn
        self.max_height=0
    
    
    def nimSum(self):
        """
        Return Grundy number of nim game.

        Returns
        -------
        int
            Grundy number for game.

        """
        
        return functools.reduce(lambda s, t: s^t, self.heaps)
    
    
    def bestPlay(self):
        """
        Return best play for computer.

        Returns
        -------
        list
            Computer play in current turn.

        """
        
        ns=self.nimSum()
        bp=[]; play_ind=0
        
        for i in self.heaps:
                bp.append(i^ns)
        
        if ns != 0:
            for i in range(len(bp)):
                if bp[i] < self.heaps[i]:
                    play_ind=i
                    heap_play=bp[i]
                    break
        
        else:
            play_ind=rr.randint(0, len(bp)-1)
            while bp[play_ind]==0:
                play_ind=rr.randint(0, len(bp)-1)
            heap_play=rr.randint(0, bp[play_ind]-1)
        
        return [play_ind, self.heaps[play_ind]-heap_play]
    
    
    def isEndgame(self):
        """
        Return game state.

        Returns
        -------
        bool
            True if Grundy number of game = 0.

        """
        
        if list(filter(lambda x: x != 0, self.heaps)) != []:
            return False
        return True
