#!/usr/bin/env python3

## functions

def print_board( top_left, top_middle, top_right,
                middle_left, middle_middle, middle_right,
                bottom_left, bottom_middle, bottom_right):
    print(f" {top_left} | {top_middle} | {top_right}")
    print("---+---+---")
    print(f" {middle_left} | {middle_middle} | {middle_right}")
    print("---+---+---")
    print(f" {bottom_left} | {bottom_middle} | {bottom_right}")


def get_postion():
    try:
        position = int(input("Choose a position from 1 to 9: "))
        return position
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 9.")
        return None
    

print("Welcome to Tic-Tac-Toe!")
player = input("Are you playing X or O? ")

# initalise board
top_left = ' '
top_middle = ' '
top_right = ' '

middle_left = ' '
middle_middle = ' '
middle_right = ' '

bottom_left = ' '
bottom_middle = ' '
bottom_right = ' '

print_board(top_left, top_middle, top_right,
                middle_left, middle_middle, middle_right,
                bottom_left, bottom_middle, bottom_right)

position = get_postion()

# update board with user input
if position == 1:
    top_left = player
elif position == 2:
    top_middle = player
elif position == 3:
    top_right = player
elif position == 4:
    middle_left = player
elif position == 5:
    middle_middle = player
elif position == 6:
    middle_right = player
elif position == 7:
    bottom_left = player
elif position == 8:
    bottom_middle = player
elif position == 9:
    bottom_right = player
else:
    print("That is not a valid position.")

# print board state
print_board(top_left, top_middle, top_right,
                middle_left, middle_middle, middle_right,
                bottom_left, bottom_middle, bottom_right)

print("\n")

# check if player won
if top_left == player and top_middle == player and top_right == player:
    print(player, "wins!")
elif middle_left == player and middle_middle == player and middle_right == player:
    print(player, "wins!")
elif bottom_left == player and bottom_middle == player and bottom_right == player:
    print(player, "wins!")
elif top_left == player and middle_left == player and bottom_left == player:
    print(player, "wins!")
elif top_middle == player and middle_middle == player and bottom_middle == player:
    print(player, "wins!")
elif top_right == player and middle_right == player and bottom_right == player:
    print(player, "wins!")
elif top_left == player and middle_middle == player and bottom_right == player:
    print(player, "wins!")
elif top_right == player and middle_middle == player and bottom_left == player:
    print(player, "wins!")
else:
    print(f"Player {player} hasn’t won.\n")