"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code to guide Karel
to build stone columns that are five beepers tall
on each appropriate avenue, as described in Assignment 1.

Karel should finish on the last avenue at 1st Street, facing east.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def turn_back():
    for i in range(2):
        turn_left()

def move_4():
    for i in range(4):
        move()

def fix_pillar():
    turn_left()
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if not on_beeper():
        put_beeper()


def go_back_to_the_bottom():
    turn_back()
    while front_is_clear():
        move()
    turn_left()

def to_other_pillars():
    if front_is_clear():
        move_4()
    else:
        turn_left

def main():
    while front_is_clear():
        fix_pillar()
        go_back_to_the_bottom()
        to_other_pillars()
    # fix_pillar()
    # go_back_to_the_bottom()
    # to_other_pillars()
    # fix_pillar()
    # go_back_to_the_bottom()
    # to_other_pillars()
    # fix_pillar()
    # go_back_to_the_bottom()
    # to_other_pillars()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
