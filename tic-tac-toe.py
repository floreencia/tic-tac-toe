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


def get_postion():
    try:
        position = int(input("Choose a position from 1 to 9: "))
        return position
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 9.")
        return None
    
def check_winner(player, board):
    # check if player won
    for combination in winning_combinations:
        if (board[combination[0]] == player and
        board[combination[1]] == player and
        board[combination[2]] == player):
            return True
        
        return False


print("Welcome to Tic-Tac-Toe!")
player = input("Are you playing X or O? ")

# initalise board
board = ["X", "X", "X", "X" ,"X" ," " ," " ," " ," "]

print_board(board)

position = get_postion()

# update board with user input & check if position is taken
if position is not None:
    if 1 <= position <= 9:
        if board[position - 1] == " ":
            board[position - 1] = player
        else:
            print("That position is already occupied.")
    else:
        print("Invalid input. Please choose a position from 1 to 9.")

# print board state
print_board(board)


if check_winner( player, board):
    print(f"{player} wins!")
else:
    print("There is no winner yet")
