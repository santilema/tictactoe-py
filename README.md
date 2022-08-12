# Santi's TicTacToe
## How to use
1. run execution.py (numpy and pygame libraries are required for this)
2. By default the game mode is PvP
    That can be changed with the following keys:
   - Press **1** to enter PvE mode against AI
   - Press **2** to enter PvE mode against Random-Moves-Bot
   - Press **0** to go back to PvP
3. By pressing **r** you can restart the game at any time

## Edit style and experience
In the execution file there are several properties which can be modified.
Some are merely visual (colors and sizes).
Others can modify the experience and objective of the game (like adjusting the grid size)
    Notice: by adjusting grid_size you are not playing TicTacToe anymore, but "n in line". 
    For example: if grid_size = 4 then you need to accomplish 4 marks in a row/column/diagongal to win

## Sources
All the code is original, but some parts of the logic behind the Unbeatable Algorithm is adapted from this article of GeeksforGeeks,
Minimax algorithm in Game Theory:
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/
