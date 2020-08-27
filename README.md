# NimSim
Implementation of a Nim game for all you Sprague-Grundy stans.

### What is Nim?
Nim is an impartial game. More importantly, it's EVERY impartial game ever created (according to the Sprague-Grundy theorem). If you aren't acquainted with combinatorial game theory and the mathematics of nim, 'Winning Ways for Your Mathematical Plays' by Conway, Berkelamp and Guy is a great place to start! <br/> <br/>
An impartial game is one where both players have EXACTLY the same moves. This is different from, say, Chess or Othello, where black and white have different moves available to them according to the board's layout at a given point in time. Interestingly, according to the Sprague-Grundy theorem, EVERY impartial game imaginable can be converted to a nim game, and as you will see when trying to win against this simulator, NIM IS SOLVABLE. There definitely is a winning strategy involved, so while I'd normally say good luck, here, I say may the better mathematician win! <br/> <br/>

### How do I play Nim?
Players take turns removing objects from heaps. I refer to these 'objects' as 'coins', because that's what we traditionally use to play nim in real life. On a player's turn, they have the option to pick one of the heaps and remove a certain amount of coins from it. They can remove all the coins in the heap, too, if they wish, but they must remove at least one coin. The game ends when a player is unable to remove an object, and that player is termed the loser and is made to wear a "Crown of Shame" (but good luck making this program wear a crown). <br/> <br/>

### Running the program
At this moment, only a Python command line game is available. <br/> <br/>
To run Python, cd into "PYTHON" <br/>
`cd PYTHON/`
<br/><br/> Run the main file with Python 3.x <br/>
`python3 main.py`
<br/><br/> Make sure you have Python 3.x installed, this will not work with lower versions.
<br/><br/> Alternatively, you can directly execute it by changing its permissions on the shell <br/>
`chmod +x main.py`
<br/><br/> Run the executable using dotslash <br/>
`./main.py`

<br/><br/> Voila! You're all set! <br/> <br/>

### Future Work
I'm planning an implementation of this on the Love2D engine to create a better UI than the command line environment. Also, will probably add misere play as well as some other nim variants in the future.
