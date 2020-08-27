#!usr/bin/python3
"""
Created on Tue Aug 25 17:31:20 2020

@author: hrishit chaudhuri
@github: https://www.github.com/hrishitchaudhuri
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src/')))

import nim

def main():
    nim.startGame()
        
if __name__=='__main__':
    main()
