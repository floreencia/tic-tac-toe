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
    try:
        position = int(input("Choose a position from 1 to 9: "))
    except ValueError: # not a number
        print("Invalid input! Please enter a number from 1 to 9.")
        return None
    
    if position >= 1 and position <= 9: # number but not in the right range
            return position
    else:
        print("Enter a number between 1 and 9 ")
        return None
    
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


print("Welcome to Tic-Tac-Toe!")

## initalise board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# board = ["X", "X", " ", "X" ,"O" ,"X" ,"O" ,"X" ,"O"]
print_board(board)

## Get input, check if position is taken, and update board
player = input("Are you playing X or O? ")
position = get_position() 

if position is not None:
    if board[position - 1] == " ":
        board[position - 1] = player
    else:
        print("That position is already occupied.")

print_board(board)

## check game status
if check_winner( player, board):
    print(f"{player} wins!")
elif board_is_full(board):
    print("It's a draw")
else:
    print("There is no winner yet")
