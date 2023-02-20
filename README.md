# Tic Tac Toe Game
This is a simple implementation of the classic Tic Tac Toe game using Python and the Tkinter library for the GUI. The game can be played by two players taking turns to place X and O symbols OR custom symbols generated based on the uppercase letter of the players name on a 3x3 grid until one player manages to get three symbols in a row (horizontally, vertically, or diagonally) or the grid is filled with symbols and no winner is declared.

## Table of Contents
* [Demo](#demo)
* [Code Explained](#code-explained)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Demo
![Tic Tac Toe Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDg2ZTA2MmIxZDgwMWVhZGY4Y2MzOTM0YmUyYjYyODQwNGU1NzA3NCZjdD1n/xN3sqMYDnR9LLeU3ZA/giphy.gif)

## Code Explained
List has been created to store the buttons and button states. The callback function is used to get the clicks and update the button. I have implemented 2 game modes i.e. Human players and AI vs Human player. 
 ```python
 #Human vs Human
  def play_with_person 
  this function gets the symbols and callback updates the buttons. Random is used to decide who will start the game.
```
```python
#Human vs AI
  The minimax algorithm has been used to backtrack the moves and find the best move for AI. 
  
  winner = check_for_winner()
    if winner == 'AI': #as the symbols have been swapped in the callback if the AI wins then return 1
        return 1
    elif winner == 'YOU': # if human player wins then return -1, -1 is a bad outcome for the AI
        return -1
    elif check_for_tie(): # if it's a tie then return 0
        return 0
    The Minimax algorithm is a recursive algorithm that works by examining all possible moves that a player can make and then choosing the move that maximizes the player's chances of winning, while minimizing the opponent's chances of winning.
```


## Installation
To run the game, you will need to have Python 3 installed on your machine, as well as the Tkinter library (which should be included with most Python installations). You can clone this repository to your local machine using the following command:

> Another way: Download the setup file and run it. It will install the game on your machine.

## Clone this repository
```bash
git clone https://github.com/sk394/tictactoe_1.git
```
## Usage
To start the game, simply run the tic_tac_toe.py script from the command line or download the setup file and install on windows.

## Copy code
> python tic_tac_toe.py

The game will open in a new window, and you can start playing by clicking on the buttons to place your symbols on the grid. The game will automatically switch between player turns and check for a winner after each move. You can restart the game at any time by clicking the "Restart" button.

## Contributing
If you find any bugs or issues with the game, or if you have ideas for new features or improvements, feel free to open an issue or pull request in this repository.

## License
This project is licensed under the MIT License - see the license file for details.