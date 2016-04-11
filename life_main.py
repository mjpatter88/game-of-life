from life import Life
import os
import sys
import time
from ast import literal_eval

filename = sys.argv[1] if len(sys.argv) >= 2 else 'beacon.txt'
width = int(sys.argv[2]) if len(sys.argv) >= 3 else 6
height = int(sys.argv[3]) if len(sys.argv) >= 4 else 6
speed = int(sys.argv[4]) if len(sys.argv) >= 5 else 4

starting_cells = []
with open(filename, 'r') as in_file:
    for line in in_file.readlines():
        if line[0] == '(':
            starting_cells.append(literal_eval(line))

life = Life(starting_cells)
live_char = '+'

if os.name == 'nt':
    clear_command = 'cls'
else:
    clear_command = 'clear'

for x in range(1000):
    os.system(clear_command)
    board = life.next(width, height)
    for row in board:
        for col in row:
            if col:
                print(live_char, end='')
            else:
                print(' ', end='')
        print()
    print("\n\nIteration: {}".format(x))
    time.sleep(1.0/speed)
