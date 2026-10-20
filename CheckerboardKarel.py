"""
File: CheckerboardKarel.py
Name: 
----------------------------
When finished, this program should
draw a checkerboard pattern using
beepers, as described in Assignment 1.

The solution should work correctly
for all of the sample worlds provided
in the starter folder.
"""

from karel.stanfordkarel import *


def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()


def step_back_check():
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
    else:
        turn_around()
        move()
        put_beeper()

def fill_odd_line():
    while front_is_clear(): #facing east
        put_beeper()
        move()
        if front_is_clear():
            move()
    step_back_check()
    turn_left()
    if front_is_clear():
        move()
    else:
        turn_right()

def fill_even_line():
    step_back_check()
    turn_left()
    while front_is_clear():  # facing west
        if on_beeper():
            move()
        else:
            move()
            put_beeper()
            move()
    step_back_check()
    turn_right()
    if front_is_clear(): #facing north
        move()
        turn_right()  #facing east

def main():
    while front_is_clear():
        fill_odd_line()
        fill_even_line()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
