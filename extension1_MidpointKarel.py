"""
File: extension1_MidpointKarel.py
Name: 
----------------------------
When finished, this program should leave a beeper
on the corner closest to the midpoint of 1st Street.

If 1st Street has an even number of corners,
either of the two central corners is acceptable.
Karel may use additional beepers while searching
for the midpoint, but must remove them before stopping.

The world can be of any size, and you may assume
that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *

def turn_right(): #facing east
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def move_diagonal_01():
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()

def move_diagonal_02():
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
            turn_left()
        else:
            move()
            turn_right()

def move_east_and_check():
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
        else:
            move()
    turn_left() #facing north
    if front_is_clear():
        move()
        turn_left() #facing west

def move_west_and_check():
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            move()
        else:
            move()
    turn_right() #facing north
    if front_is_clear():
        move()
        turn_right()

def main():
    move_diagonal_01()
    turn_around()
    while front_is_clear(): #facing west
        move()
    else:
        turn_left()
    move_diagonal_01() #facing south
    turn_right()
    while front_is_clear(): #facing west
        move()
    else:
        turn_around() #facing east
    while front_is_clear():
        move_east_and_check()
        move_west_and_check()  #facing east




# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
