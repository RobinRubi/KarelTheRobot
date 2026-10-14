"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At the start, this program does nothing.

Your task is to add the necessary code
to guide Karel to walk to the door of its house,
pick up the newspaper (represented by a beeper),
and then return to its original position
in the upper-left corner of the house.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def move_to_newspaper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

def go_home_and_read_newspaper():
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()



def main():
    move_to_newspaper()
    go_home_and_read_newspaper()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)