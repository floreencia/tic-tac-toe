#!/usr/bin/env python3

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

position = int(input("Choose a position from 1 to 9: "))

# check if there's a winner
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
    bottom_left_left = player
elif position == 8:
    bottom_middle = player
elif position == 9:
    bottom_right = player
else:
    print("That is not a valid position.")

# print board state
print("\n")
print(f" {top_left} | {top_middle} | {top_right}")
print("---+---+---")
print(f" {middle_left} | {middle_middle} | {middle_right}")
print("---+---+---")
print(f" {bottom_left} | {bottom_middle} | {bottom_right}")

print("\n")

