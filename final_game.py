import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import Menu
import random  #for generating random player symbol

root=tk.Tk() #creating root window
root.iconbitmap('tictac.ico') #setting icon for root window
root.resizable(False,False)
root.title('Tic Tac Toe Game') #setting title for root window

#define global variables
player1_symbol =None
player2_symbol = None
game_mode = None
current_player = None

#define game arena
'''b and states are matrices/lists with empty strings. b is used to display the symbols on the buttons and states is used to store the board state.
'''   
b = [] 
states = []

#Game window
'''It will create a window and when player clicks the button, 
it will call the callback function
'''
for i in range(3):
    row = []           #create a list to store the buttons
    state_row = []     #create a list to store the board state
    for j in range(3):
        button = tk.Button(text='', 
                           width=13, 
                           height=5, 
                           font=('Helvetica', 16, 'bold'),
                           bg='#ad8958', 
                           command=lambda r=i, c=j: callback(r, c))
        button.grid(row=i, column=j)
        row.append(button)
        state_row.append('') 
    b.append(row)
    states.append(state_row)

#create a callback function
'''r and c are the row and column of the button that is clicked
   if the game mode is person, then the player will play with another player
   if the game mode is AI, then the player will play with the computer
   '''
def callback(r, c):
    global game_mode,player1_symbol,player2_symbol,current_player

    if game_mode == 'person':
        if b[r][c]['text']=='': # if the button is empty
            b[r][c]['text'] = current_player #set the symbol of the current player
            states[r][c] = current_player # update the board state
            winner = check_for_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins")
                reset_game()
            elif check_for_tie():
                messagebox.showinfo("Game Over", "It's a tie")
                reset_game()
            else:
                current_player = player1_symbol if current_player == player2_symbol else player2_symbol #swap the symbols
    elif game_mode=='AI':
        player1_symbol= 'AI' #set the symbol of the AI
        player2_symbol = "YOU" #set the symbol of the player
            
        if b[r][c]['text']=='': # if the button is empty
            b[r][c]['text'] = player1_symbol if current_player == states[r][c] else player2_symbol #set the symbol of the current player
            states[r][c] = player2_symbol # update the board state
            winner = check_for_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins")
                reset_game()
            elif check_for_tie():
                messagebox.showinfo("Game Over", "It's a tie")
                reset_game()
            else:
                player1_symbol, player2_symbol = player2_symbol, player1_symbol #swap the symbols
                get_ai_move() #call the function to get the move of the AI
    else:
        messagebox.showinfo("Game Over", "Please select game mode")
        


#check winner
def check_for_winner():
    global states, b
    #check for rows and columns
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2] and states[i][0]!='':
            return states[i][0]
        if states[0][i]==states[1][i]==states[2][i] and states[0][i]!='':
            return states[0][i]
    #check for diagonals
    if states[0][0]==states[1][1]==states[2][2] and states[0][0]!='':
        return states[0][0]
    if states[0][2]==states[1][1]==states[2][0] and states[0][2]!='':
        return states[0][2]

    return None #if no winner

#check for tie/draw
def check_for_tie():
    for i in range(3):
        for j in range(3):
            if states[i][j]=='':
                return False #if there is an empty space, then it is not a tie
    return True

#define function for game mode 'person'
def play_with_person():
    global game_mode,player1_symbol,player2_symbol,current_player
    game_mode = 'person'
    reset_game()
     #get player names and symbols
    player1_name, player1_symbol, player2_name, player2_symbol = get_player_name()
    #set the current player
    current_player = random.choice([player1_symbol, player2_symbol])
   
    #display the message
    messagebox.showinfo("Game Start", f"Player 1 ({player1_name} plays with '{player1_symbol}' and Player 2 ({player2_name}) plays with '{player2_symbol}'. {current_player} will start the game")


#define function for game mode 'AI'
def play_with_ai():
    global game_mode
    game_mode = 'AI'
    reset_game()

#function for computer move
def get_ai_move():
    global player1_symbol, player2_symbol   #in this case, player1_symbol is the 'You' and player2_symbol is the 'AI' (swapped)
    best_score = float('-inf') #set the best score to the lowest possible score
    best_move = None #set the best move to None
    for i in range(3):
        for j in range(3):
            if states[i][j] == '': # if the board state is empty
                states[i][j] = player2_symbol #set the board state to the AI's symbol (the symbol has been swapped in the callback function)
                score = minimax(states, 0, False) #get the score of the board state, 0 represents the number of moves made so far
                states[i][j] = '' #reset the board state
                if score > best_score:
                    best_score = score
                    best_move = (i, j) #set the best move to the current move in the form row, column
    x, y = best_move # row= x, column= y
    b[x][y]['text'] = player2_symbol #set the button text to the 'AI' symbol
    states[x][y] = player2_symbol #set the board state to the AI's symbol
    winner = check_for_winner() # get the symbol of the winner
    if winner:
        messagebox.showinfo('Game Over', f'Player {winner} wins!')
        reset_game()
    elif check_for_tie():
        messagebox.showinfo('Game Over', 'The game is tied.')
        reset_game()
    else:
        player1_symbol, player2_symbol = player2_symbol, player1_symbol # swap the symbols of the players (now the player1_symbol is the 'AI' and player2_symbol is the 'You')


#implement the minimax algorithm for AI
def minimax(state, depth, maximizing_player):
    winner = check_for_winner()
    if winner == 'AI': #as the symbols have been swapped in the callback if the AI wins then return 1
        return 1
    elif winner == 'YOU': # if human player wins then return -1, -1 is a bad outcome for the AI
        return -1
    elif check_for_tie(): # if it's a tie then return 0
        return 0
    
    if maximizing_player: # if it's the AI's turn
        best_score = float('-inf') # set the best score to the lowest possible score, we are trying to maximize the score for AI, so begin from lowest possible score
        for i in range(3): 
            for j in range(3):
                if state[i][j]=='': # if the cell is empty
                    state[i][j] = 'AI' # make the move
                    score = minimax(state, depth +1, False) # call the minimax function recursively to get the score of the move, depth is the number of moves made so far, False means it's the human player's turn
                    state[i][j] = '' # undo the move
                    best_score = max(score, best_score) # update the best score, chooses the optimal max value
        return best_score
    else: # if it's the human player's turn
        best_score = float('inf') # set the best score to the highest possible score, minimize the score for humnan player
        for i in range(3):
            for j in range(3):
                if state[i][j]=='': # if the cell is empty
                    state[i][j] = 'YOU' # make the move, this time move for the human player
                    score = minimax(state, depth + 1, True) # call the minimax function recursively to get the score of the move, True means it's the AI's turn
                    state[i][j] = '' # undo the move
                    best_score = min(score, best_score) # update the best score, chooses the optimal min value
        return best_score

#reset the game
def reset_game():
    for i in range(3):
        for j in range(3):
            b[i][j]['text'] = ''
            states[i][j]=''


#get the players name for game mode 'person'
def get_player_name():
    global player1_symbol, player2_symbol,current_player
    player1_name=simpledialog.askstring("Input","Enter player 1 Name", parent=root)
    if player1_name:
        player1_symbol = player1_name[0].upper()
    else:
        player1_symbol = 'X'
    
    player2_name=simpledialog.askstring("Input","Enter player 2 Name", parent=root)
    if player2_name:
        player2_symbol = player2_name[0].upper()
    else:
        player2_symbol = 'O'
    return (player1_name, player1_symbol, player2_name, player2_symbol)

       

#create GUI elements for game modes

play_with_person_btn = tk.Button(text="Play with Person", bg = "blue", fg = "white", command= play_with_person)
play_with_ai_btn = tk.Button(text="Play with AI", bg = "blue", fg = "white", command= play_with_ai)
play_with_person_btn.grid(row=3,column=0)
play_with_ai_btn.grid(row=3,column=1) 
   

#create GUI elements for reset button

reset_btn = tk.Button(text="Reset game", bg = "red", fg = "white", command= reset_game)
reset_btn.grid(row=3,column=2)

#create the menu bar
menu_bar = Menu(root)
game_modes = Menu(menu_bar, tearoff=0)  
game_modes.add_command(label="Play with Person", command=play_with_person)
game_modes.add_command(label="Play with AI", command=play_with_ai)
menu_bar.add_cascade(label="Game Modes", menu=game_modes)

game_close = Menu(menu_bar, tearoff=0)
game_close.add_command(label="Reset game", command=reset_game)
game_close.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="Close", menu=game_close) #add the game menu to the menu bar

root.config(menu=menu_bar) #add the menu bar to the root window


root.mainloop()