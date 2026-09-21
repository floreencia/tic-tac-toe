#!/usr/bin/env python3

## functions
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")


def get_position():
    while True:
      try:
        position = int(input("Choose a position from 1 to 9: "))
      except ValueError:
        print("Please enter a number from 1 to 9.")
        continue

      if position < 1 or position > 9 or board[position - 1] != " ":
        print("Invalid input, enter a number between 1 and 9")        
      else:
        return position

    
def check_winner(player, board):
    # check if player won
    for combination in winning_combinations:
        if (board[combination[0]] == player and
        board[combination[1]] == player and
        board[combination[2]] == player):
            return True
        
    return False
    
def board_is_full(board):
    for position in board:
        if position == " ":
            return False

    return True

## initalise board
board = [" ", " ", " ", 
         " ", " ", " ", 
         " ", " ", " "]


print("Welcome to Tic-Tac-Toe!")
print_board(board)

player_name = input("Player X, what's your name? ")
players = {"X": player_name}
player_name = input("Player O, what's your name? ")
players["O"] = player_name
# print(f"{players["X"]}, {players["O"]}")

current_player = "X"
game_is_running = True

while game_is_running: 
    print(players[current_player] + "'s turn")

    ## Get input, check if position is taken, and update board
    position = get_position() 

    if position is not None:
        if board[position - 1] == " ":
            board[position - 1] = current_player
        else:
            print("That position is already occupied.")

    print_board(board)

    ## check game status
    if check_winner( current_player, board):
        print(f"{current_player} wins!")
        game_is_running = False
    elif board_is_full(board):
        print("It's a draw")
        game_is_running = False
    else:
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
