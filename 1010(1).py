'''
This is the first in a series of 1010 puzzles.

You are given a grid of width W and height H. Each cell is either empty, represented as a dot ".", or filled, represented with a hash "#".

You are allowed to place a 2x2 block in the grid wherever it will fit (i.e., all of those 2x2 cells are empty).

You must find a place for your 2x2 block to completely fill as many rows and columns and report how many rows and columns you can clear.
Input
Line 1: An integer W for the width of the game board.
Line 2: An integer H for the height of the game board.
Next H lines: A string of W characters, either . or #.
Output
N: the maximum number of columns and rows that could be completed by placing a 2x2 block on the given grid, or 0 if there is no place for your 2x2 block.
Constraints
3 ≤ W ≤ 10
3 ≤ H ≤ 10
The grid will never already have any completed rows or columns.
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = int(raw_input()) #width
h = int(raw_input()) #hight

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

grid = []
for i in xrange(h):
    grid.append(raw_input())

def block(grid): 
    ind = []
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == '.':
                if grid[i][j+1] == '.':
                    if grid[i+1][j] == '.':
                        if grid[i+1][j+1] == '.':
                            ind.append((i,j))
    return ind
    
def get_row(row):
    return grid[row]
    
def get_col(col):
    column = ''
    for i in range(h):
        column += grid[i][col]        
    return column
    
def fill_row(row, col):
    r = get_row(row)
    r_without_block = ''
    if len(r) > col+1:
        r_without_block = r[:col] + r[col+2:]
    else:
        r_without_block = r[:col]
    return r_without_block
    
def fill_col(row, col):
    c = get_col(col)
    c_without_block = ''
    if len(c) > row+1:
        c_without_block = c[:row] + c[row+2:]
    else:
        c_without_block = c[:row]
    return c_without_block
       
n = 0
for i in block(grid):
    num = 0
    if '.' not in fill_row(i[0], i[1]):
        num += 1
    if '.' not in fill_row(i[0]+1, i[1]):
        num += 1
    if '.' not in fill_col(i[0], i[1]):
        num += 1
    if '.' not in fill_col(i[0], i[1]+1):
        num += 1
    if num > n:
        n = num

print n
